# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Install PyQt5 and X11 support (necessary for GUI applications)
RUN apt-get update && apt-get install -y python3-pyqt5 && apt-get install -y libxcb-xinerama0

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "calculator.py"]
