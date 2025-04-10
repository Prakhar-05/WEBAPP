# Use official Python image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (for Railway / Gunicorn)
EXPOSE 8000

# Collect static files (optional, for prod-ready builds)
RUN python manage.py collectstatic --noinput

# Default command to run the app
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
