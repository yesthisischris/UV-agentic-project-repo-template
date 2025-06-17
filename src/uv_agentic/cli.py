"""Command-line interface for the uv-agentic sample."""

import argparse
from . import greet


def main() -> None:
    """Run the CLI."""
    parser = argparse.ArgumentParser(description="Sample agent CLI.")
    parser.add_argument("name", help="Name to greet.")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
