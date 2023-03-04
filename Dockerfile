# Docker file to run rasa api
# Version 1.0

FROM python:3.6-slim

# Create a working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install rasa

# Make port 5005 available to the world outside this container
EXPOSE 5005

# Define environment variable
ENV NAME Rasa

# Run app.py when the container launches
CMD ["python", "rasa run --enable-api"]