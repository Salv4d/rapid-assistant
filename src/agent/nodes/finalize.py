
def finalize(state):
    print("\n✅ Final output:")
    print(f"{state.get('final_output', '[no output]')}")

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

    return state