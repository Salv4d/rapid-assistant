from langchain.tools import tool

@tool
def get_user_memory(input: str) -> str:
    """(Stub) Retrieves a stored user memory — for future long-term memory use."""
    return "User memory system is not implemented yet."
