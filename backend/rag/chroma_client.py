import chromadb
from chromadb.utils import embedding_functions
from rag.embeddings import get_embedding

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="marketing_knowledge"
)