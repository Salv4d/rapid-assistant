#
# Copyright (c) 2025 Salvador Lucas Domiciano de Oliveira
#
# This software is licensed under the MIT License.
# See the LICENSE file in the root directory for more information.

from dotenv import load_dotenv
load_dotenv()

from src.agent.graph import build_agent_graph
agent = build_agent_graph()

if __name__ == "__main__":
    print("Rapid Assistant is ready (Tool Calling mode).")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        agent.invoke({"input": user_input})
