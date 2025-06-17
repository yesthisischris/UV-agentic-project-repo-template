import os
import structlog
import pytest
from agentic_core.logging_config import configure_logging

@pytest.fixture(autouse=True, scope="session")
def _configure_test_logging():
    """Configure console logging for the test session."""
    os.environ.pop("LOG_FORMAT", None)
    configure_logging(json=False)
    structlog.reset_defaults()
