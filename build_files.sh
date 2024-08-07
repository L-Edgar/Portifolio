
set -e  # Exit immediately if a command exits with a non-zero status


# Install pip packages
python3.10 -m pip install -r requirements.txt

# Collect static files
python3.10 manage.py collectstatic --noinput
