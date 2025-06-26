from typing import Any

import structlog

log = structlog.get_logger()


def receive_input(state: dict[str, Any]) -> dict[str, Any]:
    log.info("input_received", input=state.get("input"))
    return state
