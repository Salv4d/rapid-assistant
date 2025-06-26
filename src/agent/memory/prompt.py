from langchain.prompts import ChatPromptTemplate


def build_contextual_prompt(
    history: list,
    user_input: str,
    system_message: str = None,
    long_term_memory: str = None,
) -> ChatPromptTemplate:
    system = system_message or "You are a helpful and concise assistant."

    messages = [("system", system)]

    if long_term_memory:
        messages.append(
            (
                "system",
                f"The following information is from the user's long-term memory:\n{long_term_memory.strip()}",
            ),
        )

    messages += history + [("user", user_input)]

    return ChatPromptTemplate.from_messages(messages)
