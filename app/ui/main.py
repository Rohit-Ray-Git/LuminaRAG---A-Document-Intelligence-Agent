import streamlit as st

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

# --- File Upload ---
st.header("Upload Documents")
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)
if uploaded_files:
    for file in uploaded_files:
        if file.name not in st.session_state["uploaded_files"]:
            st.session_state["uploaded_files"].append(file.name)
            st.success(f"Uploaded: {file.name}")

# --- User Query Input ---
st.header("Ask a Question")
prompt = st.text_input("Enter your question:")

# --- Display Chat History ---
st.header("Chat History")
for msg in st.session_state["history"]:
    st.write(f"**{msg['role'].capitalize()}:** {msg['content']}")

# --- Placeholder for Answer ---
if prompt:
    # TODO: Integrate retrieval and agent logic here
    answer = f"[Placeholder] Answer to: {prompt}"
    st.session_state["history"].append({"role": "user", "content": prompt})
    st.session_state["history"].append({"role": "assistant", "content": answer})
    st.write(f"**Assistant:** {answer}") 