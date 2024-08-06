FROM python:3.10

# Create app directory
RUN mkdir -p /app
COPY . /app
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port your app runs on
EXPOSE 8080

# Command to run your application
CMD ["python", "main.py"]
