FROM python:3.9-slim-buster

# Install dependencies
RUN pip install --upgrade pip
RUN pip install telethon

# Copy code
WORKDIR /app
COPY main.py .

# Run script
CMD ["python", "main.py"]
