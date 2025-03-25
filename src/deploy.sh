#!/bin/bash

echo "🚀 Starting Django Deployment on Render..."

# Exit on any error
set -e

echo "🔹 Installing Python Dependencies..."
pip install -r requirements.txt

echo "🔹 Running Database Migrations..."
python manage.py migrate --noinput

echo "🔹 Collecting Static Files..."
python manage.py collectstatic --noinput --clear

echo "🔹 Starting Gunicorn Server..."
exec gunicorn cfehome.wsgi:application --bind 0.0.0.0:8000 --workers 3

echo "✅ Deployment Completed Successfully!"