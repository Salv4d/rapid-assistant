from typing import Any

import structlog

from src.agent.memory import (
    add_ai_message,
    add_user_message,
    build_contextual_prompt,
    get_history,
)
from src.agent.tool_registry import TOOLS
from src.rag.query_engine import get_llm

log = structlog.get_logger()


def call_tool(state: dict[str, Any]) -> dict[str, Any]:
    question = state["input"]
    add_user_message(question)

    system_message = (
        "You are a helpful AI that decides when and how to use tools to answer "
        "questions."
    )

    prompt = build_contextual_prompt(
        history=get_history(),
        user_input=question,
        system_message=system_message,
    )

    llm = get_llm().bind_tools(TOOLS)

    log.info("call_tool.invoke_llm", question=question, tool_count=len(TOOLS))

    tool_response = (prompt | llm).invoke({})
    add_ai_message(tool_response.content)

    tool_call = tool_response.tool_calls[0] if tool_response.tool_calls else None

    if not tool_call:
        log.info("call_tool.no_tool_suggested")
        return {
            **state,
            "final_output": "No tool was suggested by the model.",
        }

    tool_name = tool_call["name"]
    tool_input = tool_call["args"]

    log.info("call_tool.tool_selected", tool=tool_name, args=tool_input)

    for tool in TOOLS:
        if tool.name == tool_name:
            try:
                result = tool.func(**tool_input)
            except Exception as e:
                log.exception("call_tool.execution_error", tool=tool_name, error=str(e))
                return {
                    **state,
                    "final_output": f"Error while executing tool '{tool_name}': {e!s}",
                }
        else:
            log.info("call_tool.success", result_preview=str(result)[:80])
            return {
                **state,
                "tool_call": {"tool": tool_name, "tool_input": tool_input},
                "final_output": result,
            }

    log.warning("call_tool.tool_not_found", requested=tool_name)
    return {
        **state,
        "final_output": f"Tool '{tool_name}' not found",
    }
