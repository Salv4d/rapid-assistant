#
# Copyright (c) 2025 Salvador Lucas Domiciano de Oliveira
#
# This software is licensed under the MIT License.
# See the LICENSE file in the root directory for more information.

from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def talk_to_llm(question):
    print(f"Asking LLM: '{question}'")
    answer = llm.invoke(question)
    print(f"LLM Response: '{answer.content}'")

if __name__ == "__main__":
    print("Welcome to your AI assistant!")
    print("Type 'exit' to stop the conversation.")

    while True:
        user_question = input("You: ")
        if user_question.lower() == 'exit':
            print('Goodbye!')
            break

        talk_to_llm(user_question)