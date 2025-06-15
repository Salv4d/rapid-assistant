from src.agent.nodes import call_tool, call_rag

def execute_step(state):
    decision = state.get("next")

    if decision == "tool":
        return call_tool(state)
    
    if decision == "search":
        return call_rag(state)
    
    return {
        **state,
        "final_output": f"Unknown decision type: '{decision}'"
    }