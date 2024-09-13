
FROM python:3.11-alpine

# Set environment variables to avoid creating .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory content into the container
COPY . /app/

# Expose the Flask API port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
