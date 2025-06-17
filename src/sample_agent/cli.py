"""Command-line interface for the sample agent."""

import argparse
import json
import os
import sys
from pathlib import Path
from langsmith import trace
import structlog
from uv_agentic.logging_config import configure_logging

from . import greet
from .config import settings

configure_logging(json=os.getenv("LOG_FORMAT") == "json")
logger = structlog.get_logger()
RUN_ID = os.getenv("RUN_ID")


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
    if RUN_ID:
        log_path = Path(f"{RUN_ID}.jsonl")
        with log_path.open("a", encoding="utf-8") as f:
            json.dump({"event": message}, f)
            f.write("\n")


if __name__ == "__main__":
    main()
