from langchain.schema.runnable import RunnableLambda

from src.rag.vector_store import get_user_profile_retriever


def get_user_profile(state: dict) -> str:
    """Retrieve the user profile based on the user_id in the input state"""
    user_id = state.get("user_id", "anonymous")

    retriever = get_user_profile_retriever(
        search_kwargs={"filter": {"user_id": user_id}},
    )

    query = "user preferences"
    results = retriever.invoke(query)

    return "\n".join(doc.page_content for doc in results)


load_user_profile = RunnableLambda(get_user_profile)
