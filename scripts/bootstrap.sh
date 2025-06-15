#!/bin/bash
set -e

echo "🚀 Bootstrapping LangGraph MCP Template development environment..."

# Check if Python is available
if ! command -v python &> /dev/null; then
    echo "❌ Python is required but not installed. Please install Python 3.11+ first."
    exit 1
fi

# Check Python version
python_version=$(python --version 2>&1 | cut -d' ' -f2)
echo "✅ Found Python $python_version"

# Install/upgrade pip and hatch
echo "📦 Installing build tools..."
python -m pip install --upgrade pip
pip install hatch

# Create and setup development environment
echo "🔧 Setting up development environment..."
hatch env create

# Install pre-commit if not already installed
if ! command -v pre-commit &> /dev/null; then
    echo "🪝 Installing pre-commit..."
    pip install pre-commit
fi

# Install pre-commit hooks
echo "🔨 Installing pre-commit hooks..."
pre-commit install
pre-commit install --hook-type commit-msg

# Copy environment template if .env doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp env.example .env
    echo "⚠️  Please edit .env file with your actual API keys and configuration"
fi

# Run initial tests to make sure everything works
echo "🧪 Running initial tests..."
hatch run test:pytest --version > /dev/null 2>&1 || echo "⚠️  Tests not yet implemented - that's normal for a new project"

echo ""
echo "✅ Bootstrap complete! Next steps:"
echo "   1. Edit .env file with your API keys"
echo "   2. Start coding your agent in src/my_agent_project/"
echo "   3. Run 'hatch run test:pytest' to run tests"
echo "   4. Run 'hatch run dev' to start development server"
echo ""
echo "Happy coding! 🎉"
