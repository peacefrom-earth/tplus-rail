# Use an official lightweight Python image
FROM python:3.11-slim

# Install pip explicitly (fixes the exit code 127 error)
RUN apt-get update && apt-get install -y python3-pip

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip3 install --upgrade pip  # Use pip3 instead of pip
RUN pip3 install -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5003

# Run the Flask app
CMD ["python3", "app.py", "--host=0.0.0.0", "--port=5003"]
