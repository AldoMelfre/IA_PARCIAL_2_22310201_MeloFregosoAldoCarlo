import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# ============================================
# GENERAR DATOS DE EJEMPLO
# ============================================
# Crear un conjunto de datos no linealmente separable
X, y = make_circles(n_samples=300, factor=0.5, noise=0.1, random_state=42)

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ============================================
# ENTRENAR EL MODELO SVM CON NÚCLEO
# ============================================
# Crear el modelo SVM con un núcleo radial (RBF)
modelo_svm = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)

# Entrenar el modelo
modelo_svm.fit(X_train, y_train)

# ============================================
# EVALUAR EL MODELO
# ============================================
# Predecir las etiquetas para los datos de prueba
y_pred = modelo_svm.predict(X_test)

# Calcular la precisión
precision = accuracy_score(y_test, y_pred)
print("Precisión del modelo SVM:", precision)

# ============================================
# VISUALIZAR LOS RESULTADOS
# ============================================
# Crear una malla para graficar las regiones de decisión
xx, yy = np.meshgrid(
    np.linspace(X[:, 0].min() - 0.5, X[:, 0].max() + 0.5, 500),
    np.linspace(X[:, 1].min() - 0.5, X[:, 1].max() + 0.5, 500)
)
Z = modelo_svm.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Graficar las regiones de decisión
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, levels=50, cmap='coolwarm', alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k', s=50)
plt.title("Máquinas de Vectores de Soporte (SVM) con Núcleo RBF")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()