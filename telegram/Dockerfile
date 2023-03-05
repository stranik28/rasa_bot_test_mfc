# Docker file to run rasa api
# Version 1.0

FROM python:3.8-slim

# Create a working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install aiogram
RUN pip install requests

# Run app.py when the container launches
CMD ["python", "main.py"]