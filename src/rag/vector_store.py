from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.config import (
    COLLECTION_NAME_MEMORY,
    COLLECTION_NAME_RAG,
    VECTORSTORE_PATH,
    EMBEDDING_MODEL,
    DEVICE,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

def get_embedding_function():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": DEVICE}
    )

def get_text_splitter():
    return RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

def get_rag_vectorstore():
    return Chroma(
        persist_directory=VECTORSTORE_PATH,
        collection_name=COLLECTION_NAME_RAG,
        embedding_function=get_embedding_function()
    )

def get_memory_vectorstore():
    return Chroma(
        persist_directory=VECTORSTORE_PATH,
        collection_name=COLLECTION_NAME_MEMORY,
        embedding_function=get_embedding_function()
    )

def create_vectorstore_from_documents(documents):
    return Chroma.from_documents(
        documents=documents,
        embedding=get_embedding_function(),
        persist_directory=VECTORSTORE_PATH,
        collection_name=COLLECTION_NAME_RAG,
    )

