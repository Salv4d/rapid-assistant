from typing import TypedDict, Optional, Any
from langgraph.graph import StateGraph
from src.agent.nodes import call_tool, call_rag, finalize, plan
from src.rag.query_engine import get_llm
from src.agent.tool_registry import TOOLS

class ToolAgentState(TypedDict, total=False):
    input: str
    next: Optional[str]
    tool_call: Optional[dict]
    rag_result: Optional[str]
    source_documents: Optional[list]
    final_output: Optional[str]


def build_tool_agent():
    graph = StateGraph(ToolAgentState)
    graph.add_node("plan", plan)
    graph.add_node("call_tool", call_tool)
    graph.add_node("call_rag", call_rag)
    graph.add_node("finalize", finalize)

    graph.set_entry_point("plan")

    graph.add_conditional_edges(
        "plan",
        lambda state: state["next"],
        {
            "tool": "call_tool",
            "search": "call_rag"
        }
    )

    graph.add_edge("call_tool", "finalize")
    graph.add_edge("call_rag", "finalize")

    graph.set_finish_point("finalize")

    return graph.compile()
