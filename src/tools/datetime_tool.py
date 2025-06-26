from datetime import datetime

from langchain.tools import tool


@tool
def get_current_time(input: str) -> str:
    """Returns the current UTC date and time."""
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
