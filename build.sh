#!/bin/bash
set -e

echo "Building the sample project..."
# Install dependencies

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip pytest

# Run the Python script to check if it works
python3 CI_HW.py

# Check for PEP 8 compliance
echo "Checking for PEP 8 compliance..."
pycodestyle CI_HW.py --max-line-length=100