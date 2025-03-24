#!/bin/bash

echo "🚀 Starting Django Deployment on Render..."

# Exit on any error
set -e  

echo "🔹 Activating Virtual Environment..."
source venv/bin/activate  # Adjust if using a different virtual environment path

echo "🔹 Installing Dependencies..."
pip install -r requirements.txt

echo "🔹 Running Migrations..."
python manage.py migrate --noinput

echo "🔹 Collecting Static Files..."
python manage.py collectstatic --noinput

echo "🔹 Restarting Gunicorn..."
pkill -f gunicorn || true  # Kill existing Gunicorn processes (if any)
gunicorn --workers=3 --bind=0.0.0.0:8000 cfehome.wsgi:application &

echo "✅ Deployment Completed Successfully!"
