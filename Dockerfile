# Docker file to run rasa api
# Version 1.0

FROM python:3.8-slim

# Create a working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Make port 5005 available to the world outside this container
EXPOSE 5005

# Define environment variable
ENV NAME Rasa

# Run rasa when the container launches
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug", "--endpoints", "endpoints.yml", "--port", "5005", "--credentials", "credentials.yml", "--log-file", "rasa.log"]