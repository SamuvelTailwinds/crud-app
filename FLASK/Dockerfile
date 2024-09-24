# Use the official Python image as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY crud-app/FLASK/requirements.txt ./

# Install dependencies from the requirements.txt file
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the application code to the container
COPY crud-app/FLASK/ ./

# Expose the application port (assuming Flask runs on port 5000 by default)
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
