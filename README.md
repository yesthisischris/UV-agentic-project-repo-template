# UV-agentic-project-repo-template

Template repository for Umbra Versa agentic AI projects.

## Project structure

```
├── src/            # project code
├── tests/          # unit tests
├── docs/           # documentation
└── .github/        # CI configuration
```

## Getting started
1. Create a virtual environment and install the project in editable mode:
   ```bash
   python -m pip install -e .
   ```
2. Run tests:
   ```bash
   pytest -q
   ```

## Security guidelines
Secrets should never be committed to the repository. Use environment variables
or a `.env` file excluded from version control for credentials.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for
more information.
