
def finalize(state):
    print("[finalize] state:", state)

    return {
        "answer": state["result"],
        "tool_userd": state.get("tool_used"),
        "source_documents": state.get("source_documents", [])
    }
