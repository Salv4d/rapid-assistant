from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from src.config import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    COLLECTION_NAME_MEMORY,
    COLLECTION_NAME_RAG,
    DEVICE,
    EMBEDDING_MODEL,
    VECTORSTORE_PATH,
)


def get_embedding_function():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": DEVICE},
    )


def get_text_splitter():
    return RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )


def get_rag_vectorstore():
    return Chroma(
        persist_directory=VECTORSTORE_PATH,
        collection_name=COLLECTION_NAME_RAG,
        embedding_function=get_embedding_function(),
    )


def get_memory_vectorstore():
    return Chroma(
        persist_directory=VECTORSTORE_PATH,
        collection_name=COLLECTION_NAME_MEMORY,
        embedding_function=get_embedding_function(),
    )


def create_vectorstore_from_documents(documents):
    return Chroma.from_documents(
        documents=documents,
        embedding=get_embedding_function(),
        persist_directory=VECTORSTORE_PATH,
        collection_name=COLLECTION_NAME_RAG,
    )


def get_rag_retriever():
    """Returns a retriever for the RAG knowledge base.
    Useful when you want to inject context before sending to the LLM.
    """
    return get_rag_vectorstore().as_retriever()


def get_user_profile_retriever(search_kwargs={}):
    """Returns a retriever for long-term user memory.
    This can be used to personalize the assistant at the start of a session.
    """
    return get_memory_vectorstore().as_retriever(search_kwargs=search_kwargs)
