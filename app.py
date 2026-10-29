import os
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Número de vecinos: se puede cambiar sin tocar el código (docker run -e K=7 ...)
K = int(os.environ.get("K", "3"))

# 1797 imágenes de 8x8 píxeles con dígitos escritos a mano (0-9)
digitos = load_digits()
X_train, X_test, y_train, y_test = train_test_split(
    digitos.data, digitos.target, test_size=0.3, random_state=42
)

modelo = KNeighborsClassifier(n_neighbors=K)
modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)
precision = accuracy_score(y_test, predicciones)
print(f"Modelo: KNN con k={K}")
print(f"Imágenes de entrenamiento: {len(X_train)} | de prueba: {len(X_test)}")
print(f"Precisión en datos de prueba: {precision:.3f}")

for i in range(3):
    print(f"Imagen {i}: real = {y_test[i]} | el modelo dijo = {predicciones[i]}")
