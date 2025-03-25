#!/bin/bash

echo "🚀 Starting Django Deployment on Render..."

# Exit on any error
set -e  

echo "🔹 Installing Dependencies..."
pip install -r requirements.txt

echo "🔹 Running Migrations..."
python manage.py migrate --noinput

echo "🔹 Collecting Static Files..."
python manage.py collectstatic

echo "🔹 Restarting Gunicorn..."
pkill -f gunicorn || true  # Kill existing Gunicorn processes (if any)
gunicorn cfehome.wsgi:application --bind 0.0.0.0:8000
&

echo "✅ Deployment Completed Successfully!"
