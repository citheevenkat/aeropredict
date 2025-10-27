#!/bin/bash

# AeroPredict Setup Script
# Automates installation and initialization

set -e  # Exit on error

echo "================================================================================"
echo "  🛫 AeroPredict - Installation & Setup"
echo "================================================================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
echo "🔍 Checking Python installation..."
if command -v python3 &>/dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo -e "${GREEN}✓${NC} Python $PYTHON_VERSION found"
else
    echo -e "${RED}✗${NC} Python 3 is not installed"
    echo "Please install Python 3.8 or higher from https://python.org"
    exit 1
fi

# Check pip
echo ""
echo "🔍 Checking pip installation..."
if command -v pip3 &>/dev/null; then
    PIP_VERSION=$(pip3 --version 2>&1 | awk '{print $2}')
    echo -e "${GREEN}✓${NC} pip $PIP_VERSION found"
else
    echo -e "${RED}✗${NC} pip3 is not installed"
    echo "Installing pip..."
    python3 -m ensurepip --upgrade
fi

# Install dependencies
echo ""
echo "📦 Installing Python dependencies..."
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt --quiet
    echo -e "${GREEN}✓${NC} Dependencies installed successfully"
else
    echo -e "${YELLOW}⚠${NC}  requirements.txt not found, skipping dependency installation"
fi

# Check for existing database
echo ""
echo "🗄️  Checking database..."
if [ -f "aeropredict.db" ]; then
    echo -e "${YELLOW}⚠${NC}  Database already exists"
    read -p "Do you want to recreate it? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm aeropredict.db
        echo -e "${GREEN}✓${NC} Old database removed"
    else
        echo -e "${YELLOW}⚠${NC}  Keeping existing database"
    fi
fi

# Initialize system
echo ""
echo "🚀 Initializing AeroPredict system..."
python3 aeropredict_system.py

# Check if successful
if [ $? -eq 0 ]; then
    echo ""
    echo "================================================================================"
    echo -e "  ${GREEN}✅ INSTALLATION COMPLETE!${NC}"
    echo "================================================================================"
    echo ""
    echo "📚 Quick Start:"
    echo ""
    echo "  1. View system report:"
    echo "     python3 aeropredict_system.py"
    echo ""
    echo "  2. Run interactive demo:"
    echo "     python3 aeropredict_demo.py"
    echo ""
    echo "  3. Open web dashboard:"
    echo "     open AeroPredict_Demo.html"
    echo ""
    echo "  4. Browse database:"
    echo "     python3 view_database.py"
    echo ""
    echo "  5. View configuration:"
    echo "     python3 config.py"
    echo ""
    echo "================================================================================"
    echo "  📖 Documentation: README.md"
    echo "  🐛 Issues: https://github.com/yourusername/aeropredict/issues"
    echo "================================================================================"
    echo ""
else
    echo ""
    echo "================================================================================"
    echo -e "  ${RED}✗ INSTALLATION FAILED${NC}"
    echo "================================================================================"
    echo ""
    echo "Please check the error messages above and try again."
    echo "If the problem persists, please open an issue on GitHub."
    echo ""
    exit 1
fi
