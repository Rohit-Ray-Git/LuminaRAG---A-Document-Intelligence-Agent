# LuminaRAG - A Document Intelligence Agent

**LuminaRAG** is a modern, professional Retrieval-Augmented Generation (RAG) agent that enables intelligent question answering, summarization, and reasoning over your documents and web content. It combines local document retrieval, real-time LLMs, and a beautiful chat UI for a seamless user experience.

---

## 🚀 Features
- **PDF Ingestion:** Upload and index your own PDF documents for private, context-aware Q&A.
- **RAG Pipeline:** Combines vector search with LLMs for accurate, grounded answers.
- **Modern Chat UI:** Clean, centered interface with sidebar chat history and instant feedback.
- **Groq/DeepSeek LLM Integration:** Fast, high-quality answers using the latest cloud LLMs.
- **Session History:** All conversations are stored and viewable in the sidebar.
- **Spinner Feedback:** Visual spinners for document processing and answer generation.
- **Easy Customization:** Modular codebase for rapid extension and improvement.

---

## 🛠️ Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Rohit-Ray-Git/LuminaRAG---A-Document-Intelligence-Agent.git
   cd LuminaRAG - A Document Intelligence Agent
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv luminarag-venv
   .\luminarag-venv\Scripts\activate  # On Windows
   # or
   source luminarag-venv/bin/activate   # On Mac/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up your `.env` file:**
   - Add your API keys for Google Generative AI and Groq:
     ```env
     GOOGLE_API_KEY=your-google-api-key
     GROQ_API_KEY=your-groq-api-key
     ```
5. **Run the app:**
   ```sh
   streamlit run app/ui/main.py
   ```

---

## 💡 Usage
- **Upload PDFs:** Use the upload area to add your documents.
- **Ask Questions:** Type your question and get instant, context-aware answers.
- **View History:** All Q&A pairs are saved in the sidebar for review.
- **Clear History:** Use the sidebar button to reset your chat.

---

## 📁 Folder Structure
```
LuminaRAG - A Document Intelligence Agent/
├── app/
│   ├── retrieval/         # PDF processing and vector store logic
│   ├── utils/             # LLM and helper utilities
│   └── ui/                # Streamlit UI code
├── vector_db/             # Chroma vector database files
├── requirements.txt       # Python dependencies
├── .env                   # API keys and config (not committed)
├── README.md              # Project documentation
└── ...
```

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
MIT 