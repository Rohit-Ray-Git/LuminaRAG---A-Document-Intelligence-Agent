import streamlit as st
from app.retrieval.vectorstore import VectorStore
from app.retrieval.ingest import process_pdf
from app.utils.deepseek_llm import call_deepseek_r1
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()
# Set Google API key for embedding model
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
# DeepSeek API key is loaded in the utils module as needed

st.set_page_config(page_title="LuminaRAG - A Document Intelligence Agent", page_icon="📄")

st.title("LuminaRAG - A Document Intelligence Agent")
st.markdown("""
LuminaRAG is an intelligent agent for document question answering, summarization, and reasoning. Upload your documents and ask questions to get context-aware answers!
""")

# --- Session State Initialization ---
if "history" not in st.session_state:
    st.session_state["history"] = []
if "uploaded_files" not in st.session_state:
    st.session_state["uploaded_files"] = []
if "processed_files" not in st.session_state:
    st.session_state["processed_files"] = []

# --- Embedding Model and Vector Store Initialization ---
EMBEDDING_MODEL = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
VECTOR_DB_PATH = "./vector_db"
COLLECTION_NAME = "luminarag_docs"

vector_store = VectorStore(persist_directory=VECTOR_DB_PATH, collection_name=COLLECTION_NAME, embedding_function=EMBEDDING_MODEL)

# --- File Upload and Ingestion ---
st.header("Upload Documents")
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)
if uploaded_files:
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
        else:
            st.info(f"Already processed: {file.name}")

# --- User Query Input ---
st.header("Ask a Question")
prompt = st.text_input("Enter your question:")

# --- Display Chat History ---
st.header("Chat History")
for msg in st.session_state["history"]:
    st.write(f"**{msg['role'].capitalize()}:** {msg['content']}")

# --- Retrieval and DeepSeek LLM Answer Generation ---
if prompt:
    st.session_state["history"].append({"role": "user", "content": prompt})
    docs, metadatas = vector_store.query(prompt, n_results=5)
    if docs:
        context = "\n\n".join([doc for doc in docs[0]]) if isinstance(docs[0], list) else "\n\n".join(docs)
        answer = call_deepseek_r1(prompt, context)
    else:
        answer = call_deepseek_r1(prompt, "")
    st.session_state["history"].append({"role": "assistant", "content": answer})
    st.write(f"**Assistant:** {answer}") 