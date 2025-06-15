#
# Copyright (c) 2025 Salvador Lucas Domiciano de Oliveira
#
# This software is licensed under the MIT License.
# See the LICENSE file in the root directory for more information.

from dotenv import load_dotenv
load_dotenv()

from src.rag.query_engine import ask

def talk_to_agent(question):
    result = ask(question)

    answer = result["result"]
    sources = result.get("source_documents", [])
    print(f"\n Answer: \n{answer}")

    if sources:
        print("Retrieved documents:")
        for i, doc in enumerate(sources):
            print(f"  - [{i+1}] {doc.metadata.get('source', 'no metadata')}")

if __name__ == "__main__":
    print("Rag assistant is ready!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        talk_to_agent(user_input)