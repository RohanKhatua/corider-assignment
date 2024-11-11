FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on - 6000
EXPOSE 6000

# Run app.py when the container launches with specified number of workers
CMD ["gunicorn", "-b", "0.0.0.0:6000", "--workers", "4", "main:app"]
