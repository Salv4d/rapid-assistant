from langchain.tools import tool


@tool
def calculate(expression: str) -> str:
    """Evaluate a math expression like '3 + 2 * 7'."""
    try:
        return str(eval(expression, {"__builtins__": {}}))
    except Exception as e:
        return f"Error: {e}"
