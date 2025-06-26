from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import BaseMessage

memory = InMemoryChatMessageHistory()


def get_history() -> list[BaseMessage]:
    return memory.messages


def add_user_message(content: str) -> None:
    memory.add_user_message(content)


def add_ai_message(content: str) -> None:
    memory.add_ai_message(content)


def clear() -> None:
    memory.clear()
