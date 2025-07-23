import sys
import os
import asyncio
import streamlit as st
from dotenv import load_dotenv

# App paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Set event loop policy for Windows
if sys.platform.startswith('win'):
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    except Exception:
        pass

# Load environment variables
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# DeepSeek + Embedding + VectorDB
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.retrieval.vectorstore import VectorStore
from app.retrieval.ingest import process_pdf
from app.utils.deepseek_llm import call_groq_deepseek, filter_think_tags

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Set up Google Embeddings and Vector Store
EMBEDDING_MODEL = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
VECTOR_DB_PATH = "./vector_db"
COLLECTION_NAME = "luminarag_docs"
vector_store = VectorStore(
    persist_directory=VECTOR_DB_PATH,
    collection_name=COLLECTION_NAME,
    embedding_function=EMBEDDING_MODEL
)

# Streamlit Page Config
st.set_page_config(page_title="LuminaRAG - Ask Your Document", layout="centered")

# Optional Styling
st.markdown("""
<style>
body {
    background-color: #0d1117;
    color: white;
}
h1, h2, h3, h4 {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "processed_files" not in st.session_state:
    st.session_state["processed_files"] = []
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "user_question" not in st.session_state:
    st.session_state["user_question"] = ""

# ---------- Sidebar: Chat History ----------
with st.sidebar:
    st.markdown("## 📂 Chat History")
    if st.session_state["chat_history"]:
        for i, item in enumerate(st.session_state["chat_history"], 1):
            st.markdown(f"**{i}.** ❓ {item['question']}<br>👉 {item['answer']}", unsafe_allow_html=True)
    else:
        st.info("No chat history yet.")
    st.markdown("---")
    if st.button("🧹 Clear History"):
        st.session_state["chat_history"] = []
        st.success("Chat history cleared!")

# ---------- Title ----------
st.markdown("""
<h1 style="text-align: center; font-size: 2.5rem;">
📄 LuminaRAG - Ask Your Document
</h1>
""", unsafe_allow_html=True)

# ---------- Upload PDFs ----------
uploaded_files = st.file_uploader("Upload PDF files here 👇", type=["pdf"], accept_multiple_files=True)
if uploaded_files:
    with st.spinner("Processing and indexing uploaded files..."):
        for file in uploaded_files:
            if file.name not in st.session_state["processed_files"]:
                docs = process_pdf(file)
                if docs:
                    ids = [f"{file.name}-{i}" for i in range(len(docs))]
                    texts = [doc.page_content for doc in docs]
                    metadatas = [doc.metadata for doc in docs]
                    vector_store.add_documents(docs=texts, metadatas=metadatas, ids=ids)
                    st.session_state["processed_files"].append(file.name)
                    st.success(f"Ingested and indexed: {file.name}")
                else:
                    st.error(f"Failed to process: {file.name}")

# ---------- Ask a Question ----------
if st.session_state["processed_files"]:
    with st.container():
        st.markdown("""
        <div style="background-color:#161b22; padding: 2rem; border-radius: 20px; box-shadow: 0 0 20px rgba(255,255,255,0.05);">
            <h3 style="text-align:center;">💬 Ask a Question</h3>
        </div>
        """, unsafe_allow_html=True)

        question = st.text_input("Enter your question:", key="user_question", label_visibility="collapsed")

        if st.button("🔍 Get Answer") and question.strip() != "":
            with st.spinner("Generating answer..."):
                docs, _ = vector_store.query(question, n_results=5)
                flat_docs = [doc for sublist in docs for doc in sublist]
                context = "\n\n".join(flat_docs)
                answer = call_groq_deepseek(question, context)
                clean_answer = filter_think_tags(answer)

            st.success(clean_answer)

            # Save to chat history
            st.session_state.chat_history.append({
                "question": question,
                "answer": clean_answer
            })

            # Clear input and rerun
            st.session_state.user_question = ""
            st.rerun()
else:
    st.info("👆 Upload a PDF to ask questions.")

# ---------- Footer ----------
st.markdown("""
<div style='text-align: center; margin-top: 2rem; font-size: 1.1rem; color: #9ca3af;'>
    LuminaRAG is a Retrieval-Augmented Generation (RAG) agent that answers your questions using your
    documents and the latest AI models. Upload PDFs, ask questions, and get smart, context-aware answers!
    <br><br>✨
</div>
""", unsafe_allow_html=True)
