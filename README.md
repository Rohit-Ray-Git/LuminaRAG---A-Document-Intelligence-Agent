# LuminaRAG - A Document Intelligence Agent 🚀🦾

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-ff4b4b?logo=streamlit)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**LuminaRAG** is a next-generation, Retrieval-Augmented Generation (RAG) platform for intelligent question answering, summarization, and reasoning over your documents and the web. It features:

- 🧠 **Local & Cloud LLMs** (DeepSeek, Groq, Gemini)
- 📄 **PDF Ingestion & Indexing**
- 🔍 **Vector Search with ChromaDB**
- 💬 **Modern Chat UI (Streamlit)**
- 🌐 **Web Search Fallback**
- 🧩 **Modular, Extensible Codebase**

---

## ✨ Key Features

- **PDF Ingestion:** Upload and index your own PDF documents for private, context-aware Q&A.
- **RAG Pipeline:** Combines vector search with LLMs for accurate, grounded answers.
- **Web Search Fallback:** If your docs can't answer, fallback to live web search and Gemini summarization.
- **Modern Chat UI:** Clean, centered interface with sidebar chat history and instant feedback.
- **Session History:** All conversations are stored and viewable in the sidebar.
- **Easy Customization:** Modular codebase for rapid extension and improvement.
- **DeepSeek Reasoning Agent:** A separate, advanced agent for local RAG and web reasoning.

---

## 🏗️ Tech Stack

- **Python 3.10+**
- **Streamlit** (UI)
- **ChromaDB** (Vector DB)
- **LangChain** (Document parsing, chunking)
- **Google Generative AI** (Embeddings, Gemini)
- **Groq/DeepSeek LLMs** (Cloud LLM answers)
- **Agno** (Agentic AI for DeepSeek Reasoning Agent)
- **BeautifulSoup** (Web scraping)

---

## 🗂️ Folder Structure

```
LuminaRAG - A Document Intelligence Agent/
├── app/
│   ├── retrieval/         # PDF processing & vector store logic (vectorstore.py, ingest.py)
│   ├── utils/             # LLM, web search, and summarizer utilities
│   └── ui/                # Streamlit UI (main.py)
├── vector_db/             # Chroma vector database files (auto-generated)
├── deepseek_reasoning_ai_agent.py # Standalone DeepSeek Reasoning Agent
├── requirements.txt       # Python dependencies
├── .env                   # API keys and config (not committed)
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
├── *.pdf                  # Example/test documents
└── ...
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```sh
git clone https://github.com/Rohit-Ray-Git/LuminaRAG---A-Document-Intelligence-Agent.git
cd LuminaRAG - A Document Intelligence Agent
```

### 2. Create and activate a virtual environment
```sh
python -m venv luminarag-venv
./luminarag-venv/Scripts/activate  # On Windows
# or
source luminarag-venv/bin/activate   # On Mac/Linux
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Set up your `.env` file
Create a `.env` file in the root directory with your API keys:
```env
GOOGLE_API_KEY=your-google-api-key
GROQ_API_KEY=your-groq-api-key
```

### 5. Run the main app
```sh
streamlit run app/ui/main.py
```

### 6. (Optional) Run the DeepSeek Reasoning Agent
```sh
streamlit run deepseek_reasoning_ai_agent.py
```

---

## 💡 Usage
- **Upload PDFs:** Use the upload area to add your documents.
- **Ask Questions:** Type your question and get instant, context-aware answers.
- **Web Search:** Enable fallback for web search if your docs can't answer.
- **View History:** All Q&A pairs are saved in the sidebar for review.
- **Clear History:** Use the sidebar button to reset your chat.

---

## 🧬 How It Works

1. **PDF Upload:** Drag and drop your PDFs. The app extracts, chunks, and embeds the content.
2. **Vector Search:** Your question is embedded and matched against document vectors using ChromaDB.
3. **LLM Answering:** The most relevant chunks are sent to a cloud LLM (DeepSeek via Groq) for a grounded answer.
4. **Web Fallback:** If no answer is found, optionally search the web and summarize with Gemini.
5. **Chat UI:** All interactions are managed in a modern, responsive Streamlit interface.

---

## 🧩 Main Modules

- `app/ui/main.py` — Streamlit UI, chat logic, PDF upload, and Q&A
- `app/retrieval/vectorstore.py` — ChromaDB vector store wrapper
- `app/retrieval/ingest.py` — PDF parsing and chunking
- `app/utils/deepseek_llm.py` — Groq/DeepSeek LLM API integration
- `app/utils/web_search.py` — DuckDuckGo web search utility
- `app/utils/gemini_summarizer.py` — Gemini-based web result summarization
- `deepseek_reasoning_ai_agent.py` — Standalone agentic RAG app (with Agno, Ollama, Gemini, ChromaDB)

---

## 📦 Dependencies

Key packages (see `requirements.txt` for full list):
- `streamlit`, `langchain`, `chromadb`, `langchain-google-genai`, `agno`, `ollama`, `openai`, `google-generativeai`, `python-dotenv`, `PyPDF2`, `PyPDF`, `requests`, `beautifulsoup4`

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements
- [Streamlit](https://streamlit.io/)
- [ChromaDB](https://www.trychroma.com/)
- [LangChain](https://www.langchain.com/)
- [Groq](https://groq.com/)
- [Google Generative AI](https://ai.google/)
- [Agno](https://github.com/agnodice/agno)

---

> Made with ❤️ for document intelligence and AI research! 