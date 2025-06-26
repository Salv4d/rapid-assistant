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


def call_rag(state: dict[str, Any]) -> dict[str, Any]:
    question = state["input"]
    user_context = state.get("user_context", "")
    rag_docs = state.get("rag_docs", [])

    log.info("call_rag.start", question=question, doc_count=len(rag_docs))

    add_user_message(question)

    context_str = "\n".join(doc.page_content for doc in rag_docs)

    system_message = (
        "You are a helpful and intelligent assistant that answers user questions "
        "using relevant documents.\n Always follow the user's preferences when "
        "formatting and writing your response.\n User preferences:\n"
        f"{user_context.strip()}"
    )

    prompt_template = build_contextual_prompt(
        history=get_history(),
        user_input=question,
        system_message=system_message,
        long_term_memory=context_str,
    )

    llm = get_llm()
    prompt = prompt_template.format()

    response = llm.invoke(prompt)

    log.info(
        "call_rag.response",
        tokens=len(prompt),
        output_preview=response.content[:60],
    )

    add_ai_message(response.content)

    return {
        **state,
        "final_output": response.content,
        "source_documents": rag_docs,
    }
