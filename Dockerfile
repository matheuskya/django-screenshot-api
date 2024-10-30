# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install --with-deps

# Copy the entire project folder into the container
COPY . /app/

# Expose the port the Django app runs on
EXPOSE 8000

# Run Django’s development server, specifying the correct path to manage.py
CMD ["python", "screenshotapi/manage.py", "runserver", "0.0.0.0:8000"]
