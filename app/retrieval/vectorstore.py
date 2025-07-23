import chromadb
from chromadb.config import Settings
from typing import List, Dict, Any

class VectorStore:
    def __init__(self, persist_directory: str, collection_name: str, embedding_function):
        """
        Initialize the Chroma vector database and collection.
        """
        self.client = chromadb.PersistentClient(path=persist_directory, settings=Settings(allow_reset=True))
        self.collection_name = collection_name
        self.embedding_function = embedding_function
        try:
            self.collection = self.client.get_collection(name=collection_name)
        except Exception:
            self.collection = self.client.create_collection(name=collection_name)

    def add_documents(self, docs: List[str], metadatas: List[Dict[str, Any]], ids: List[str]):
        """
        Add documents and their metadata to the vector store.
        """
        self.collection.add(documents=docs, metadatas=metadatas, ids=ids)

    def query(self, query_text: str, n_results: int = 5):
        """
        Retrieve the most similar documents to the query text.
        """
        results = self.collection.query(query_texts=[query_text], n_results=n_results)
        return results.get('documents', []), results.get('metadatas', []) 