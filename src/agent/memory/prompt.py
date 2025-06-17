from langchain.prompts import ChatPromptTemplate

def build_contextual_prompt(history: list, user_input: str, system_message: str = None) -> ChatPromptTemplate:
    system = system_message or "You are a helpful and concise assistant."

    return ChatPromptTemplate.from_messages(
        [("system", system)] + history + [("user", user_input)]
    )