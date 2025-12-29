# Use Python 3.11 base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all project files
COPY . .

# Set environment variables (optional, you can use Render Env Vars)
ENV PYTHONUNBUFFERED=1

# Start bot
CMD ["python", "bot.py"]
