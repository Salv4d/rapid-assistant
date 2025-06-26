import logging

import structlog


def setup_logging() -> None:
    logging.basicConfig(
        format="%(message)s",
        stream=None,
        level=logging.INFO,
    )

    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ],
    )
