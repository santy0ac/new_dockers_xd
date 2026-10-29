# 1) Imagen base: Linux con Python 3.12 ya instalado
FROM python:3.12-slim

# 2) Carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3) Primero las dependencias (así Docker puede reutilizar esta capa)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Después nuestro código
COPY app.py .

# 5) Comando que se ejecuta al iniciar el contenedor
CMD ["python", "app.py"]
