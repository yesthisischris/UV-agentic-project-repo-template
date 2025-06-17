from unittest.mock import patch
import subprocess


def test_battery_smoke():
    """Run the CLI with network calls mocked."""
    with patch("requests.get") as mock_get:
        result = subprocess.run([
            "python",
            "-m",
            "sample_agent.cli",
            "World",
        ], capture_output=True, text=True)
        assert result.returncode == 0
        assert result.stdout.strip() == "Hello, World!"
        mock_get.assert_not_called()
