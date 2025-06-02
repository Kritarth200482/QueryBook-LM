from pathlib import Path
import os
import sys
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_qdrant import QdrantVectorStore
from getpass import getpass

load_dotenv()

# loading the environment variables from the .env file

if not os.getenv("QDRANT_URL"):
    qdrant = getpass("Enter your Qdrant URL: ")
    os.environ["QDRANT_URL"] = qdrant

if not os.getenv("QDRANT_API_KEY") and not os.getenv("QDRANT_API_KEY_FILE"):
    api_key = getpass("Enter your Qdrant API KEY: ")
    os.environ["QDRANT_API_KEY"] = api_key

if not os.getenv("GOOGLE_API_KEY"):
    api_key = getpass("Enter your Google API KEY: ")
    os.environ["GOOGLE_API_KEY"] = api_key

pdf_path = Path(__file__).parent / "Course Structure and Curriculum B Tech Programme ECED.pdf"
if not pdf_path.exists():
    print("Pdf file not found")
    print("Please make sure the file is in the same directory as this script")
    sys.exit(1)

print("Loading pdf file")

__loader__ = PyPDFLoader(file_path=str(pdf_path))
documents = __loader__.load()

print("Splitting the documents into chunks")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_docs = text_splitter.split_documents(documents=documents)

print("Creating embeddings")

embedders = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

print("Creating vector store")

vector_store = QdrantVectorStore.from_documents(
    documents=split_docs,
    embedding=embedders,
    url="http://localhost:6333",
    collection_name="learning_langchain",
)

print("Ingestion Complete")

print("Setting Up retriever")

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

print("Initializing LLMs")

llm = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    temperature=0.1,
)

def ask_question(question):
    print(f"Question: {question}")
    print("Searching for relevant documents from the pdf...")

    relevant_docs = retriever.get_relevant_documents(question)
    context_parts = []

    for i, doc in enumerate(relevant_docs):
        page_num = doc.metadata.get("page", "Unknown")
        page_content = doc.page_content
        context_parts.append(
            f"Document {i+1}:\nPage: {page_num}\nContent: {page_content}\n"
        )

    full_context = "\n".join(context_parts)

    system_prompt = f"""
You are a helpful assistant that answers questions based on the provided context.
The context is from a PDF document. Use the information to answer the question.
If you don't know the answer, say "I don't know".

Context:
{full_context}

Question: {question}
Answer:
"""

    response = llm.invoke(system_prompt)
    print(f"Answer: {response.content}")

    print("\n📋 Source Pages:")
    for i, doc in enumerate(relevant_docs):
        page_num = doc.metadata.get('page', 'Unknown')
        preview = doc.page_content[:100] + "..." if len(doc.page_content) > 100 else doc.page_content
        print(f"  {i+1}. Page {page_num}: {preview}")

    return {
        'answer': response.content,
        'source_documents': relevant_docs,
        'context': full_context
    }

if __name__ == "__main__":
    print("\n🎉 RAG AI Agent is ready!")
    print("🌐 You can view your collection at: http://localhost:6333/dashboard")

    # Example questions
    example_questions = [
        "What is the course structure of B Tech Programme ECED?",
        "What are the different program categories available?",
        "What are the credit requirements for the program?",
        "What subjects are taught in the first semester?"
    ]

    print("\n🔥 Example Questions:")
    for i, q in enumerate(example_questions, 1):
        print(f"{i}. {q}")

    # Interactive mode
    print("\n" + "="*50)
    print("💬 Interactive Mode - Type 'quit' to exit")
    print("="*50)

    while True:
        user_question = input("\n🗣️ Ask your question: ").strip()

        if user_question.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break

        if user_question:
            try:
                ask_question(user_question)
            except Exception as e:
                print(f"❌ Error: {e}")
        else:
            print("⚠️ Please enter a valid question.")
            
