# Usamos una imagen oficial de Python
FROM python:3.11-slim

# Instalamos las herramientas de compilación (gcc, g++) que le faltaban al servidor
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Configuramos el directorio de trabajo
WORKDIR /app

# Copiamos las dependencias e instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . .

# Exponemos el puerto
EXPOSE 8080

# Arrancamos el servidor con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "servidor_ia:app"]