from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from datetime import datetime
import tempfile


def process_pdf(uploaded_file):
    """
    Extracts and splits text from an uploaded PDF file and returns chunked documents with metadata.
    Args:
        uploaded_file: A file-like object (Streamlit uploader)
    Returns:
        List[Document]: List of chunked Document objects with metadata
    """
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            loader = PyPDFLoader(tmp_file.name)
            documents = loader.load()

        for doc in documents:
            doc.metadata.update({
                "source_type": "pdf",
                "file_name": uploaded_file.name,
                "timestamp": datetime.now().isoformat()
            })

        return split_texts(documents)
    except Exception as e:
        print(f"PDF processing error: {str(e)}")
        return []

def split_texts(documents, chunk_size=1000, chunk_overlap=200):
    """
    Splits documents into manageable text chunks.
    Args:
        documents: List of Document objects
        chunk_size: Size of each chunk
        chunk_overlap: Overlap between chunks
    Returns:
        List[Document]: Chunked Document objects
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    split_docs = text_splitter.split_documents(documents)
    return [Document(page_content=chunk.page_content, metadata=chunk.metadata) for chunk in split_docs if chunk.page_content.strip()] 