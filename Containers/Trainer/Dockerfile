# Use a slim version of Python 3.12 as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all project files to the container's working directory
COPY Containers/Trainer/requirements.txt .
COPY Containers/Trainer/main.py .

# Install Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


RUN mkdir -p data
COPY data/FlavorSense.csv data/

COPY /App .

# Start the FastAPI application using Uvicorn
# Note: 'App.main:app' refers to 'main.py' inside the 'App' folder
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

