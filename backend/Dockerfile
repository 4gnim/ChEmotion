# Base image Python yang ringan (berbasis Debian Linux)
FROM python:3.9-slim

# Konfigurasi Environment
ENV PYTHONDONTWRITEBYTECODE=1
# Memastikan log Flask langsung tercetak ke terminal server
ENV PYTHONUNBUFFERED=1

# folder kerja di dalam server container
WORKDIR /app

# Instalasi OS-Level Dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-ind \
    tesseract-ocr-eng \
    && rm -rf /var/lib/apt/lists/*

# Salin file
COPY requirements.txt /app/

# Install dependensi Machine Learning dan Flask
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode API dan model ML (.h5, .pkl)
COPY . /app/

# Buka port 5000 agar Flask bisa diakses
EXPOSE 5000

# Perintah untuk menyalakan API saat container dihidupkan
CMD ["python", "app.py"]