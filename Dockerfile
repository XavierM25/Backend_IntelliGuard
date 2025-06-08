# Usa una imagen oficial de Python compatible con dlib
FROM python:3.10-slim

# Establece variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Instala dependencias del sistema necesarias para dlib y opencv
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    libboost-python-dev \
    libboost-thread-dev \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Crea el directorio de la app
WORKDIR /app

# Copia primero los archivos de requisitos para aprovechar la caché de Docker
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Crea directorios necesarios
RUN mkdir -p data/runs

# Expone el puerto que Render usará
EXPOSE 10000

# Comando para correr la app con Gunicorn optimizado para Render
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--workers", "1", "--threads", "2", "--timeout", "120", "app:app"] 