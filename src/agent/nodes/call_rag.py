from src.agent.memory.base import add_ai_message, add_user_message, get_history
from src.agent.memory.prompt import build_contextual_prompt
from src.rag.query_engine import build_qa_chain

def call_rag(state):
    question = state["input"]
    add_user_message(question)

    prompt = build_contextual_prompt(
        history=get_history(),
        user_input=question,
        system_message="You are an intelligent assistant that answers user questions using relevant documents.",
    )

    chain = build_qa_chain()

    rag_result = chain.invoke({"query": prompt.format()})

    add_ai_message(rag_result.get("result", ""))

    return {
        **state,
        "source_documents": rag_result.get("source_documents", []),
        "final_output": rag_result.get("result", "No answer was returned by the RAG chain.")
    }