"""Command-line interface for the sample agent."""

import argparse
import sys
from langsmith import trace
import structlog

from . import greet
from .config import settings

structlog.configure(
    processors=[lambda _logger, _name, event_dict: event_dict["event"]],
    logger_factory=structlog.PrintLoggerFactory(file=sys.stdout),
)
logger = structlog.get_logger()


def main() -> None:
    """Run the CLI."""
    parser = argparse.ArgumentParser(description="Sample agent CLI.")
    parser.add_argument("name", help="Name to greet.")
    args = parser.parse_args()

    if settings.langsmith_api_key:
        with trace(
            "greet",
            "chain",
            metadata={"langsmith_api_key": settings.langsmith_api_key},
        ):
            message = greet(args.name)
    else:
        message = greet(args.name)

    logger.info(message)


if __name__ == "__main__":
    main()
