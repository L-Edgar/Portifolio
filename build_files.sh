p#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

# Check if python3.11 is installed, if not install it
if ! command -v python3.11 &> /dev/null
then
    echo "Python 3.11 not found, installing..."
    sudo apt-get update
    sudo apt-get install -y python3.11 python3.11-venv python3.11-dev
fi

# Check if pip for python3.11 is installed, if not install it
if ! python3.11 -m pip &> /dev/null
then
    echo "pip for Python 3.11 not found, installing..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3.11 get-pip.py
fi

# Install pip packages
python3.11 -m pip install -r requirements.txt

# Collect static files
python3.11 manage.py collectstatic --noinput
