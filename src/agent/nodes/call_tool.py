from src.agent.memory.base import add_ai_message, add_user_message, get_history
from src.agent.memory.prompt import build_contextual_prompt
from src.agent.tool_registry import TOOLS
from src.rag.query_engine import get_llm


def call_tool(state):
    question = state["input"]
    add_user_message(question)

    prompt = build_contextual_prompt(
        history=get_history(),
        user_input=question,
        system_message="You are a helpful AI that decides when and how to use tools to answer questions.",
    )

    llm = get_llm().bind_tools(TOOLS)

    tool_response = (prompt | llm).invoke({})
    add_ai_message(tool_response.content)

    tool_call = tool_response.tool_calls[0] if tool_response.tool_calls else None

    if not tool_call:
        return {
            **state,
            "final_output": "No tool was suggested by the model.",
        }

    tool_name = tool_call["name"]
    tool_input = tool_call["args"]

    for tool in TOOLS:
        if tool.name == tool_name:
            try:
                result = tool.func(**tool_input)
                return {
                    **state,
                    "tool_call": {"tool": tool_name, "tool_input": tool_input},
                    "final_output": result,
                }
            except Exception as e:
                return {
                    **state,
                    "final_output": f"Error while executing tool '{tool_name}': {e!s}",
                }

    return {
        **state,
        "final_output": f"Tool '{tool_name}' not found",
    }
