from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import ChatMessageHistory

memory = ConversationBufferMemory(return_messages=True)

def get_history() -> list:
    return memory.chat_memory.messages

def add_user_message(content: str):
    memory.chat_memory.add_user_message(content)

def add_ai_message(content: str):
    memory.chat_memory.add_ai_message(content)

def clear():
    memory.clear()