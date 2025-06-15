import subprocess


def test_cli_main():
    result = subprocess.run(["python", "-m", "uv_agentic.cli", "World"], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, World!"
