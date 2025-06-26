from typing import Any

import structlog
from langchain.schema.runnable import RunnableParallel

from src.agent.rag_retriever import rag_retriever
from src.agent.user_profile import load_user_profile

log = structlog.get_logger()

combined_context = RunnableParallel(
    {
        "user_context": load_user_profile,
        "rag_docs": rag_retriever,
    },
)


def enrich_context(state: dict[str, Any]) -> dict[str, Any]:
    """Node that enriches the state with both user preferences and relevant documents."""
    context = combined_context.invoke(state)

    log.info("enrich_context.user", user_context=context["user_context"])
    log.info("enrich_context.rag_docs", doc_count=len(context["rag_docs"]))

    return {
        **state,
        **context,
    }
