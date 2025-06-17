import logging, structlog, sys


def configure_logging(json: bool = False) -> None:
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
