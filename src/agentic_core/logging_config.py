"""Logging utilities for agentic projects.

This module defines helper functions for configuring structured logging.
It uses the ``structlog`` package to emit either JSON or console formatted
logs. Call :func:`configure_logging` early in your application's entry
point to initialize logging for the process.
"""

from __future__ import annotations

import logging
import sys

import structlog


def configure_logging(json: bool = False) -> None:
    """Configure structlog based logging.

    Parameters
    ----------
    json : bool, optional
        Emit logs as JSON if ``True``. Otherwise use a console renderer.
    """
    timestamper = structlog.processors.TimeStamper(fmt="iso")
    processors = [
        timestamper,
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]
    if json:
        processors += [structlog.processors.JSONRenderer()]
    else:
        processors += [structlog.dev.ConsoleRenderer()]

    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    )
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
