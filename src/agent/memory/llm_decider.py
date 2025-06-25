import json
import re
from typing import Optional
from src.rag.query_engine import get_llm

def should_store_with_llm(user_input: str, ai_output: str) -> tuple[bool, str | None]:
    """Ask the LLM whether to store, and what to store, from the user/AI interaction."""
    llm = get_llm()
    
    prompt = f"""
You are managing long-term memory for an AI assistant.

Your goal is to identify persistent user-specific preferences or facts,
such as how the user likes to receive answers, their goals, communication style, or values.

DO NOT store general facts, trivia, or facts about the world.

Respond in JSON with the following format:
{{
  "store": true or false,
  "preference": "<short sentence to store, or null>"
}}

User said:
\"\"\"{user_input}\"\"\"

AI responded:
\"\"\"{ai_output}\"\"\"
    """.strip()

    try:
        response = llm.invoke(prompt).content.strip()

        parsed = safe_parse_json(response)
        return parsed.get("store", False), parsed.get("preference")
    except Exception as e:
        print(f"[WARN] Failed to parse LLM memory response: {e}")
        return False, None
    
def safe_parse_json(text: str) -> Optional[dict]:
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    return json.loads(match.group())