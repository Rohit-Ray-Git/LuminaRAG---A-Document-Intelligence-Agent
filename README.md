# LuminaRAG - A Document Intelligence Agent

LuminaRAG is a scalable, modular Retrieval-Augmented Generation (RAG) agent that enables intelligent question answering, summarization, and reasoning over your documents and web content. It combines local document retrieval, real-time web search, and advanced LLMs for comprehensive, context-aware answers.

## Features
- 📄 Ingest and query PDFs, web pages, and more
- 🔍 Hybrid retrieval: semantic + keyword search
- 🤖 LLM-powered reasoning (OpenAI, Gemini, etc.)
- 🌐 Web search fallback for up-to-date answers
- 🗂️ Modular, extensible architecture
- 🛡️ User authentication and document management (planned)

## Folder Structure
```
app/
  ui/           # Streamlit or frontend code
  agents/       # Agent logic and orchestration
  retrieval/    # RAG, vector DB, and search logic
  utils/        # Utilities and helpers
 data/
  uploads/      # Uploaded documents
  vector_db/    # Vector database files
 tests/         # Unit and integration tests
.env            # Environment variables
.gitignore      # Git ignore rules
README.md       # Project documentation
```

## Getting Started
1. Clone the repo
2. Install dependencies (`pip install -r requirements.txt`)
3. Set up your `.env` file
4. Run the app (`streamlit run app/ui/main.py`)

## License
MIT 