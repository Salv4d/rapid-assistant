from src.rag.query_engine import get_llm

def should_store_with_llm(user_input: str, ai_output: str) -> bool:
    """Ask the LLM wheter this interaction should be store as long-term memory."""

    llm = get_llm()
    prompt = f"""
You are helping manage an AI assistant's long-term memory.

Decide if the following exchange should be remembered as important.

User said:
\"\"\"{user_input}\"\"\"

AI responded:
\"\"\"{ai_output}\"\"\"

Should this be stored in long-term memory? Answer only with 'yes' or 'no'.
    """.strip()

    response = llm.invoke(prompt).content.strip().lower()
    return response.startswith('y')