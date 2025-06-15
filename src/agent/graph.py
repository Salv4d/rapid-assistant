from typing import TypedDict, Optional
from langgraph.graph import StateGraph
from src.agent.nodes import execute_step, finalize, plan, receive_input

class ToolAgentState(TypedDict, total=False):
    input: str
    next: Optional[str]
    tool_call: Optional[dict]
    rag_result: Optional[str]
    source_documents: Optional[list]
    final_output: Optional[str]


def build_tool_agent():
    builder = StateGraph(ToolAgentState)
    builder.add_node("receive_input", receive_input)
    builder.add_node("plan", plan)
    builder.add_node("execute_step", execute_step)
    builder.add_node("finalize", finalize)

    builder.set_entry_point("receive_input")
    builder.add_edge("receive_input", "plan")
    
    builder.add_edge("plan", "execute_step")

    builder.add_edge("execute_step", "finalize")
    builder.set_finish_point("finalize")

    return builder.compile()
