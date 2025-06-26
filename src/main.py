# Copyright (c) 2025 Salvador Lucas Domiciano de Oliveira
# This software is licensed under the MIT License.
# See the LICENSE file in the root directory for more information.

from typing import NoReturn

import structlog
from dotenv import load_dotenv

from src.agent.graph import build_agent_graph

log = structlog.get_logger()


def run_console_agent() -> NoReturn:
    load_dotenv()
    agent = build_agent_graph()

    log.info("agent.start", message="Rapid Assistant is ready (Tool Calling mode)")
    log.info("agent.instruction", message="Type 'exit' to quit")

    user_id = input("Enter your user ID: ").strip()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            log.info("agent.exit", message="Goodbye!")
            break

        response = agent.invoke({"input": user_input, "user_id": user_id})
        final_output = response.get("final_output")

        if final_output:
            log.info("agent.response", answer=final_output)


if __name__ == "__main__":
    run_console_agent()
