
set -e  # Exit immediately if a command exits with a non-zero status


# Install pip packages
python3.11 -m pip install -r requirements.txt

# Collect static files
python3.11 manage.py collectstatic --noinput
