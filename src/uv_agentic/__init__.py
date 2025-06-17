from .logging_config import configure_logging
import os

configure_logging(json=os.getenv("LOG_FORMAT") == "json")
