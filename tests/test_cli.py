import subprocess
import os


def test_cli_main(tmp_path):
    env = os.environ.copy()
    env["LOG_FORMAT"] = "json"
    env["RUN_ID"] = str(tmp_path / "run")
    result = subprocess.run([
        "python",
        "-m",
        "sample_agent.cli",
        "World",
    ], capture_output=True, text=True, env=env)
    assert result.returncode == 0
    assert "Hello, World" in result.stdout
