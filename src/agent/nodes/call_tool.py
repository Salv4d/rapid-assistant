from src.rag.query_engine import get_llm
from src.agent.tool_registry import TOOLS


def call_tool(state):
    question = state["input"]
    
    llm = get_llm().bind_tools(TOOLS)
    tool_response = llm.invoke(question)

    tool_call = tool_response.tool_calls[0] if tool_response.tool_calls else None

    if not tool_call:
        return {
            **state,
            "final_output": "No tool was suggested by the model."
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
                    "final_output": result
                }
            except Exception as e:
                return {
                    **state,
                    "final_output": f"Error while executing tool '{tool_name}': {str(e)}"
                }

    return {
        **state,
        "final_output": f"Tool '{tool_name}' not found"
    }
