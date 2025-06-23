from pydantic import BaseModel
from langchain.tools import tool
from src.agent.memory import retrieve_memory

class RetrieveMemoryInput(BaseModel):
    user_id: str
    query: str

@tool("retrieve_user_memory", args_schema=RetrieveMemoryInput)
def get_user_memory(user_id: str, query: str) -> str:
    """
    Search the user's long-term memory for information related to the query.

    Use this tool when you want to recall facts, preferences, or statements the user made in the past.
    Always provide the user_id and a query describing what you're trying to remember.
    """
    documents = retrieve_memory(user_id, query)

    if not documents:
        return "No relevant memory found."
    
    return "\n---\n".join(doc.page_content for doc in documents)