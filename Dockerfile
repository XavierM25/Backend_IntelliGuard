# Usa una imagen oficial de Python compatible con dlib
FROM python:3.10-slim

# Variables de entorno para Hugging Face
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    GRADIO_SERVER_NAME=0.0.0.0 \
    GRADIO_SERVER_PORT=7860

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
    wget \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Crea el directorio de la app
WORKDIR /app

# Copia primero los archivos de requisitos para aprovechar la caché de Docker
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir gradio && \
    pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Crea directorios necesarios
RUN mkdir -p data/dataset_facial data/pertenencias

# Exponer puerto de Gradio
EXPOSE 7860

# Comando para Hugging Face Spaces
CMD ["python", "gradio_app.py"] 