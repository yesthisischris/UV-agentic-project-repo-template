FROM python:3.12-slim-bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -s /bin/bash vscode

# Set working directory
WORKDIR /workspace

# Install Python dependencies
COPY requirements.txt* pyproject.toml ./
RUN pip install --upgrade pip && \
    pip install hatch pre-commit

# Switch to non-root user
USER vscode

# Set default shell
SHELL ["/bin/bash", "-c"]
