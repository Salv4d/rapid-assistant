from src.agent.memory import (
    add_ai_message,
    add_user_message,
    build_contextual_prompt,
    get_history,
)
from src.rag.query_engine import get_llm


def plan(state):
    question = state["input"]
    add_user_message(question)

    prompt = build_contextual_prompt(
        get_history(),
        question,
        system_message="""
You are a smart planner. Decide whether to use a TOOL or SEARCH to answer this question.
Respond only with "tool" or "search".
""",
    )

    llm = get_llm()

    decision = (prompt | llm).invoke({}).content.strip().lower()

    add_ai_message(decision)

    return {
        **state,
        "next": "tool" if "tool" in decision else "search",
    }
