from src.rag.query_engine import get_llm

def plan(state):
    llm = get_llm()
    question = state["input"]

    prompt = f"""
You are a smart planner. Decide whether to use a TOOL or SEARCH to answer this question.

Question: "{question}"

Respond only with "tool" or "search".
"""
    decision = llm.invoke(prompt).content.strip().lower()

    return {
        **state,
        "next": "tool" if "tool" in decision else "search"
    }