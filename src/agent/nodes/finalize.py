from src.agent.memory import should_store_with_llm, store_memory


def finalize(state):
    user_id = state.get("user_id", "anonymous")
    user_input = state.get("input", "")
    output = state.get("final_output", "")

    print(f"\n✅ Current User Id: {user_id} Final output:")
    print(f"{output}")

    if state.get("tool_call"):
        print("\n🔧 Tool used:")
        print(f"  - name: {state['tool_call'].get('tool', '[unknown]')}")
        print(f"  - input: {state['tool_call'].get('tool_input', {})}")

    if state.get("source_documents"):
        print("\n📚 Retrieved documents:")
        for i, doc in enumerate(state["source_documents"]):
            source = doc.metadata.get("source", "unknown")
            preview = doc.page_content.strip().replace("\n", " ")[:120]
            print(f"  [{i+1}] {source}: {preview}...")

    if user_id.lower() == "anonymous" or not output:
        return state

    store, text_to_store = should_store_with_llm(user_input, output)

    if store:
        print("New memory stored:", text_to_store)
        store_memory(user_id, text_to_store)

    return state
