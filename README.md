# Lab: Docker + ML en el navegador

Plantilla del Taller de Computación (USFQ). Un modelo KNN que reconoce dígitos escritos a mano,
empaquetado en un contenedor Docker.

## Archivos
- `app.py` – entrena y evalúa el modelo (k configurable con la variable de entorno `K`).
- `requirements.txt` – dependencias de Python.
- `Dockerfile` – la receta de la imagen.
- `.devcontainer/devcontainer.json` – prepara el Codespace con Docker disponible.

## Pasos rápidos (en la terminal del Codespace)
```bash
docker --version
docker run hello-world
python app.py            # falla: aquí no está scikit-learn
docker build -t miml .   # construye la imagen
docker run miml          # ejecuta el contenedor
docker run -e K=7 miml   # cambia k sin reconstruir
```
