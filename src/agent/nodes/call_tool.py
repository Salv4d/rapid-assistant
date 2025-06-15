from langchain_core.utils.function_calling import convert_to_openai_tool
from src.rag.query_engine import get_llm, build_qa_chain
from src.agent.tool_registry import TOOLS

openai_tools = [convert_to_openai_tool(t) for t in TOOLS]
llm = get_llm().bind_tools(openai_tools)

def call_tool(state):
    question = state["input"]
    tool_response = llm.invoke(question)

    tool_call = tool_response.tool_calls[0] if tool_response.tool_calls else None

    if not tool_call:
        rag_chain = build_qa_chain()
        rag_result = rag_chain.invoke({"query": question})
        return {
            **state,
            "agent_outcome": str(tool_response),
            "final_output": rag_result["result"],
            "source_documents": rag_result.get("source_documents", [])
        }

    tool_name = tool_call["name"]
    tool_input = tool_call["args"]

    for tool in TOOLS:
        if tool.name == tool_name:
            result = tool.func(**tool_input)
            return {
                **state,
                "tool_call": {"tool": tool_name, "tool_input": tool_input},
                "final_output": result
            }

    return {
        **state,
        "final_output": f"Tool '{tool_name}' not found"
    }
