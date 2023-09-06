
FROM ubuntu

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# This is not needed for the calculator code, so it's commented out
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
# Not required for this specific application, but can be useful for web apps
# EXPOSE 80

# Define environment variable
ENV NAME Calculator

# Run python script when the container launches
CMD ["python", "calculator.py"]
