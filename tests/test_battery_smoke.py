from unittest.mock import patch
import subprocess
import os


def test_battery_smoke():
    """Run the CLI with network calls mocked."""
    with patch("requests.get") as mock_get:
        env = os.environ.copy()
        env["LOG_FORMAT"] = "text"
        result = subprocess.run([
            "python",
            "-m",
            "sample_agent.cli",
            "World",
        ], capture_output=True, text=True, env=env)
        assert result.returncode == 0
        assert "Hello, World" in result.stdout
        mock_get.assert_not_called()
