# Set base image
FROM python:3.12-alpine

# Set working directory
WORKDIR /app

# Install any needed packages specified in your requirements.txt
RUN pip install flask
RUN pip install boto3

# COPY the rest of the application code
COPY . .

# Expose port 5000
EXPOSE 5000

# Command to run the application
CMD [ "python", "app.py" ]