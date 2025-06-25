from langchain.schema.runnable import RunnableParallel
from src.agent.rag_retriever import rag_retriever
from src.agent.user_profile import load_user_profile

combined_context = RunnableParallel({
    "user_context": load_user_profile,
    "rag_docs": rag_retriever
})

def enrich_context(state: dict) -> dict:
    """
    Node that enriches the state with both user preferences and relevant documents.
    """
    context = combined_context.invoke(state)

    print("User context:", context["user_context"])
    print("RAG docs found:", len(context["rag_docs"]))

    return {
        **state,
        **context
    }