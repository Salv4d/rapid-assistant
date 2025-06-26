from typing import Any

import structlog

from src.agent.memory import should_store_with_llm, store_memory

log = structlog.get_logger()


def finalize(state: dict[str, Any]) -> dict[str, Any]:
    user_id = state.get("user_id", "anonymous")
    user_input = state.get("input", "")
    output = state.get("final_output", "")

    log.info("finalize.output", user_id=user_id, output=output)

    if state.get("tool_call"):
        log.info(
            "finalize.tool_used",
            tool=state["tool_call"].get("tool", "[unknown]"),
            input=state["tool_call"].get("tool_input", {}),
        )

    if state.get("source_documents"):
        previews = []
        for i, doc in enumerate(state["source_documents"]):
            source = doc.metadata.get("source", "unknown")
            preview = doc.page_content.strip().replace("\n", " ")[:120]
            previews.append({"index": i + 1, "source": source, "preview": preview})

        log.info("finalize.rag_docs", documents=previews)

    if user_id.lower() == "anonymous" or not output:
        return state

    store, text_to_store = should_store_with_llm(user_input, output)

    if store:
        log.info("finalize.memory_stored", text=text_to_store)
        store_memory(user_id, text_to_store)

    return state
