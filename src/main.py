from dotenv import load_dotenv
load_dotenv()

from src.agent.graph import build_tool_agent

agent = build_tool_agent()


def talk_to_agent(question: str):
    result = agent.invoke({"input": question})

    print("\n🧠 Answer:")
    print(result.get("final_output", "[no output]"))

    if result.get("tool_call"):
        print("\n🔧 Tool used:")
        print(f"  - name: {result['tool_call']['tool']}")
        print(f"  - input: {result['tool_call']['tool_input']}")


if __name__ == "__main__":
    print("Rapid Assistant is ready (Tool Calling mode).")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        talk_to_agent(user_input)
