# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy all files to the working directory
COPY . .

# Install necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the test script first, then run the main program
CMD ["sh", "-c", "python -m unittest discover -s . && python main.py && tail -f /dev/null"]
