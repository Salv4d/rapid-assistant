from langchain_core.documents import Document

from src.rag.vector_store import get_memory_vectorstore


def store_memory(user_id: str, content: str):
    document = Document(
        page_content=content,
        metadata={"user_id": user_id},
    )
    vectorstore = get_memory_vectorstore()
    vectorstore.add_documents([document])


def retrieve_memory(user_id: str, query: str, k: int = 3):
    vectorstore = get_memory_vectorstore()
    results = vectorstore.similarity_search_with_score(
        query,
        k=k,
        filter={"user_id": user_id},
    )

    return [document for document, _ in results]
