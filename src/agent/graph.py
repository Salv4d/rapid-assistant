from typing import TypedDict, Optional
from langgraph.graph import StateGraph
from src.agent.nodes import call_rag, call_tool, finalize, plan, receive_input

class AgentState(TypedDict, total=False):
    input: str
    next: Optional[str]
    tool_call: Optional[dict]
    rag_result: Optional[str]
    source_documents: Optional[list]
    final_output: Optional[str]
    user_id: Optional[str]

def route_next_step(state: AgentState) -> str:
    return state.get("next", "finalize")

def build_agent_graph():
    builder = StateGraph(AgentState)

    builder.add_node("receive_input", receive_input)
    builder.add_node("plan", plan)
    builder.add_node("call_tool", call_tool)
    builder.add_node("call_rag", call_rag)
    builder.add_node("finalize", finalize)

    builder.set_entry_point("receive_input")
    builder.add_edge("receive_input", "plan")
    
    builder.add_conditional_edges(
        "plan",
        path=route_next_step,
        path_map={
            "tool": "call_tool",
            "search": "call_rag"
        }
    )

    builder.add_edge("call_tool", "finalize")
    builder.add_edge("call_rag", "finalize")
    builder.set_finish_point("finalize")

    return builder.compile()
