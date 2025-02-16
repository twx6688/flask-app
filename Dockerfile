# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run Flask
CMD ["python", "app.py"]
