from typing import TypedDict, Optional, Any
from langgraph.graph import StateGraph
from src.rag.query_engine import get_llm
from src.agent.tool_registry import TOOLS
from src.agent.nodes.call_tool import call_tool

class ToolAgentState(TypedDict):
    input: str
    agent_outcome: Optional[str]
    tool_call: Optional[dict]
    final_output: Optional[str]

def build_tool_agent():
    graph = StateGraph(ToolAgentState)
    graph.add_node("call_tool", call_tool)
    graph.set_entry_point("call_tool")
    graph.set_finish_point("call_tool")
    return graph.compile()
