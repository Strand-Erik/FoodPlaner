#!/bin/bash

# Define the environment name and requirements file
ENV_NAME="venv"
REQUIREMENTS_FILE="requirements.txt"

# Check if the virtual environment already exists
if [ ! -d "$ENV_NAME" ]; then
    # Create a virtual environment
    echo "Creating a virtual environment named $ENV_NAME..."
    python3 -m venv $ENV_NAME
    echo "Virtual environment $ENV_NAME created."
else
    echo "Virtual environment $ENV_NAME already exists."
fi

# Activate the virtual environment
echo "Activating the virtual environment..."
source $ENV_NAME/bin/activate

# Check if requirements.txt exists
if [ -f "$REQUIREMENTS_FILE" ]; then
    # Install dependencies from requirements.txt
    echo "Installing dependencies from $REQUIREMENTS_FILE..."
    pip install -r $REQUIREMENTS_FILE
    echo "Dependencies installed."
else
    echo "The file $REQUIREMENTS_FILE does not exist."
fi

echo "Setup complete. Don't forget to activate the virtual environment."
