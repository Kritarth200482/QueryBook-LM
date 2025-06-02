# QueryBook-LM
.

📘 QueryBookLM
QueryBookLM is a lightweight Retrieval-Augmented Generation (RAG) AI agent that allows you to ask natural language questions about any PDF document (like a curriculum, brochure, or guidebook) and receive detailed, accurate answers grounded in the content. Built using LangChain, Google Gemini Pro, and Qdrant, it combines semantic search and generative AI to simulate contextual document comprehension.

# Tech Stack

->Python 3.10+	Base programming language

->LangChain	Framework for building LLM-powered applications

->Google Generative AI	For generating embeddings and answers (Gemini Pro + embedding-001)

->Qdrant	Vector database used to store and retrieve text chunks

->Docker


🚀 Features
📄 PDF Ingestion: Automatically loads and parses PDF documents.

✂️ Recursive Text Chunking: Splits text into smart overlapping chunks to retain semantic meaning.

🧠 Embeddings with Google GenAI: Creates vector embeddings using models/embedding-001.

💾 Vector Storage in Qdrant: Stores and retrieves vectorized chunks efficiently.

🧾 Context-Aware Answering: Answers your questions using only the content from the document.

🔎 Citations Included: Returns page numbers and matched text chunks as sources.

💬 Interactive CLI: Chat with your PDF directly from the terminal.

🔐 Environment-secured API keys using a .env file.

# How to Run Locally (Step-by-Step)
🛠️ This section helps you set up QueryBookLM on your local machine.

📁 1. Copy the Code and Your PDF
Create a folder and paste the main.py file into it.

Place the PDF you want to ask questions about in the same folder.

Open that folder in Visual Studio Code (or any code editor).

Update line 28 in main.py to reflect your PDF file name:

pdf_path = Path(__file__).parent / "your-document-name.pdf"
📄 2. Create a .env File
In the same folder, create a .env file and add the following content:


GOOGLE_API_KEY=your_google_genai_api_key
QDRANT_API_KEY=your_qdrant_api_key   # Leave blank if running locally without authentication
QDRANT_URL=http://localhost:6333
📦 3. Install Required Dependencies
Make sure you have Python 3.10+ installed. Then install the required packages:


pip install langchain langchain-google-genai langchain-community langchain-qdrant qdrant-client python-dotenv
🧠 4. Start Qdrant (Local Vector DB)
If you don’t already have Qdrant running locally, start it via Docker:


docker run -p 6333:6333 qdrant/qdrant
🔁 This runs Qdrant on http://localhost:6333 as defined in your .env.

▶️ 5. Run the Script
Now, run the project using:

python main.py
You’ll see a prompt like:

🎉 RAG AI Agent is ready!
🗣️ Ask your question:
Type questions such as:

📂 Project Structure

QueryBookLM/
├── main.py              # Main script
├── your-document.pdf    # PDF you want to query
├── .env                 # API keys and config
└── README.md
⚙️ How It Works (Simplified Flow)
Load → Reads your PDF file with PyPDFLoader.

Chunk → Splits the text into overlapping chunks.

Embed → Embeds those chunks using Google’s embedding model.

Store → Stores them in a local Qdrant vector store.

Retrieve → Finds the most relevant chunks to your query.

Generate → Uses Gemini Pro to generate answers using those chunks only.

Respond → Returns clean answers with citations.



Prompt Gemini ➝ Custom prompt includes the retrieved context + user query.

Generate Answer ➝ LLM generates a helpful response based strictly on context.

