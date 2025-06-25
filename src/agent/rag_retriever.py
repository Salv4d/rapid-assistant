from xml.dom.minidom import Document
from langchain.schema.runnable import RunnableLambda
from src.rag.vector_store import get_rag_retriever

_preloaded_rag_retriever = get_rag_retriever()

def run_rag_retriever(state: dict) -> list[Document]:
    return _preloaded_rag_retriever.invoke(state["input"])

rag_retriever = RunnableLambda(run_rag_retriever)