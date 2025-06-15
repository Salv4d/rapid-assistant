import os

VECTORSTORE_PATH = os.getenv("VECTORSTORE_PATH", "data/vectorstore")
COLLECTION_NAME = os.getenv("VECTORSTORE_COLLECTION", "faq")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 300))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
DEVICE = os.getenv("EMBEDDING_DEVICE", "cpu")
ACTIVE_LLM_PROVIDER = os.getenv("ACTIVE_LLM_PROVIDER", "gemini")
