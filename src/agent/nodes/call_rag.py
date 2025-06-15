from src.rag.query_engine import build_qa_chain

def call_rag(state):
    question = state["input"]
    chain = build_qa_chain()

    rag_result = chain.invoke({"query": question})

    return {
        **state,
        "source_documents": rag_result.get("source_documents", []),
        "final_output": rag_result["result"]
    }