from typing import Any

import structlog

from src.agent.memory import (
    add_ai_message,
    add_user_message,
    build_contextual_prompt,
    get_history,
)
from src.rag.query_engine import get_llm

log = structlog.get_logger()


def plan(state: dict[str, Any]) -> dict[str, Any]:
    question = state["input"]
    add_user_message(question)

    system_message = (
        "You are a smart planner. Decide whether to use a TOOL or SEARCH to answer "
        "this question."
        'Respond only with "tool" or "search".'
    )

    prompt = build_contextual_prompt(
        get_history(), question, system_message=system_message
    )

    llm = get_llm()

    decision = (prompt | llm).invoke({}).content.strip().lower()
    add_ai_message(decision)

    next_step = "tool" if "tool" in decision else "search"

    log.info("plan.decision", question=question, decision=decision, next=next_step)

    return {**state, "next": next_step}
