FROM python:3.11.8-slim-bullseye

# Set working directory
WORKDIR /app

# Update & install Python dependencies
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Jalankan langsung main.py di root (bukan lagi dari /app/app/)
CMD ["python", "main.py"]
