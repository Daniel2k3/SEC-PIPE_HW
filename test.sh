#!/bin/bash
set -e

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip pytest

echo "Running tests for the pythonHW..."

# Run tests using pytest
pytest CI_HW.py