kFROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Copy run.sh and make it executable
COPY run.sh .
RUN chmod +x run.sh

# Expose the port that Railway expects
EXPOSE 8080

# Set a default environment variable for PORT (Railway will override this if needed)
ENV PORT=8080

# Use run.sh as the entry point
CMD ["/bin/bash", "run.sh", "--log-level", "debug"]

