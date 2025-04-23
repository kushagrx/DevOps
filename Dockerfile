# Use Ubuntu as the base image
FROM ubuntu:20.04

# Avoid interactive prompts
ARG DEBIAN_FRONTEND=noninteractive

# Update and install Python & pip
RUN apt update && \
    apt install -y python3 python3-pip && \
    apt clean

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Expose the FastAPI default port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]