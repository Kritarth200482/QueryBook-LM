# QueryBook-LM
.

📘 QueryBookLM
QueryBookLM is a lightweight Retrieval-Augmented Generation (RAG) AI agent that allows you to ask natural language questions about a PDF document (like a curriculum or technical manual) and receive detailed, context-aware answers. Powered by Google Gemini Pro, LangChain, and Qdrant, it combines vector search and generative AI to simulate document understanding.

🚀 Features
📄 PDF Ingestion: Uploads and parses PDF documents using LangChain’s PyPDFLoader.

✂️ Smart Chunking: Splits content into overlapping chunks using recursive text splitting for better semantic understanding.

🧠 Embeddings Generation: Creates embeddings using Google’s Generative AI Embedding model (models/embedding-001).

📦 Vector Storage with Qdrant: Stores chunk embeddings in a Qdrant vector database for efficient semantic search.

❓ Query Answering: Retrieves the most relevant document chunks based on user queries and uses Gemini Pro to generate answers using that context.

📑 Contextual Answering with Sources: Returns answers with page numbers and references to the original PDF content.

💬 Interactive CLI: Asks questions in an interactive command-line session with example prompts.

🔐 Secure API Access: Uses environment variables for Google API key management.

✅ How to Run Locally (Step-by-Step)
💡 This section will help you copy, configure, and run QueryBookLM in your local machine.

🧾 1. Copy the Code & PDF
Open any folder on your system and paste the main.py code file into it.

Place your desired PDF (e.g., my-document.pdf) in the same folder.

Open the folder in VS Code or any Python editor.

IMPORTANT: In main.py, update line 28 with your PDF file name:

python
Copy
Edit
pdf_path = Path(__file__).parent / "my-document.pdf"
📦 2. Install Required Dependencies
Ensure you're using Python 3.10 or above. Then install the following packages:

bash
Copy
Edit
pip install langchain langchain-google-genai langchain-community langchain-qdrant qdrant-client
🧠 3. Start Qdrant (Vector Database)
If you haven't already, start Qdrant locally using Docker:

bash
Copy
Edit
docker run -p 6333:6333 qdrant/qdrant
Alternatively, you can install it natively: https://qdrant.tech/documentation/quick-start

🔐 4. Set Your Google Generative AI Key
When you run the script, it will prompt:

vbnet
Copy
Edit
Enter your Google API key:
Paste your Google API key here to proceed.

▶️ 5. Run the Project
bash
Copy
Edit
python main.py
You'll see:

arduino
Copy
Edit
🎉 RAG AI Agent is ready!
🗣️ Ask your question:
Ask questions like:

What are the subjects in the first semester?

What are the credit requirements?

What are the course categories?

📂 Project Structure
graphql
Copy
Edit
QueryBookLM/
│
├── main.py                    # Main Python script for running the RAG pipeline
├── my-document.pdf            # Your target PDF file
└── README.md                  # This documentation
🧠 How It Works
Load PDF ➝ Using PyPDFLoader.

Split Text ➝ With overlap-aware chunking (RecursiveCharacterTextSplitter).

Generate Embeddings ➝ Using GoogleGenerativeAIEmbeddings.

Store in Qdrant ➝ As vector embeddings for efficient similarity search.

Retrieve Context ➝ Top-k (default 4) chunks using semantic similarity.

Prompt Gemini ➝ Custom prompt includes the retrieved context + user query.

Generate Answer ➝ LLM generates a helpful response based strictly on context.

