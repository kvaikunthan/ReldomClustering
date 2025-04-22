#!/bin/bash

echo "Setting up Conda env"

# Check for conda
if ! command -v conda &> /dev/null; then
    echo "Conda is not installed. Please install Miniconda or Anaconda first."
    exit 1
fi

# Create the environment
conda env create -f environment.yml

# Activate message (can't auto-activate from a script)
echo ""
echo "Environment created"
echo "Run: conda activate analogy"