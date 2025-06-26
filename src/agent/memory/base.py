from langchain_core.chat_history import InMemoryChatMessageHistory

memory = InMemoryChatMessageHistory()


def get_history() -> list:
    return memory.messages


def add_user_message(content: str):
    memory.add_user_message(content)


def add_ai_message(content: str):
    memory.add_ai_message(content)


def clear():
    memory.clear()
