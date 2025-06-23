from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

from src.rag.vector_store import get_rag_vectorstore
from src.config import ACTIVE_LLM_PROVIDER


def get_llm():
    """Factory for selecting the active LLM provider."""
    if ACTIVE_LLM_PROVIDER == "gemini":
        return ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    else:
        raise ValueError(f"Unsupported LLM provider: {ACTIVE_LLM_PROVIDER}")


def build_qa_chain():
    """Builds a RAG chain using the configured vector store and LLM."""
    retriever = get_rag_vectorstore().as_retriever()
    llm = get_llm()

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
