import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# ============================================
# GENERAR DATOS DE EJEMPLO
# ============================================
# Crear un conjunto de datos no linealmente separable
X, y = make_moons(n_samples=1000, noise=0.1, random_state=42)

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Escalar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ============================================
# CREAR EL MODELO DE RED NEURONAL
# ============================================
# Definir el modelo secuencial
modelo = Sequential([
    Dense(16, activation='relu', input_shape=(X_train.shape[1],)),  # Capa oculta con 16 neuronas
    Dense(8, activation='relu'),  # Capa oculta con 8 neuronas
    Dense(1, activation='sigmoid')  # Capa de salida (clasificación binaria)
])

# Compilar el modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# ============================================
# ENTRENAR EL MODELO
# ============================================
# Entrenar la red neuronal
historial = modelo.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

# ============================================
# EVALUAR EL MODELO
# ============================================
# Evaluar el modelo en los datos de prueba
y_pred = (modelo.predict(X_test) > 0.5).astype("int32")
precision = accuracy_score(y_test, y_pred)
print("Precisión del modelo de Aprendizaje Profundo:", precision)

# ============================================
# VISUALIZAR LOS RESULTADOS
# ============================================
# Graficar la pérdida durante el entrenamiento
plt.figure(figsize=(8, 6))
plt.plot(historial.history['loss'], label='Pérdida de entrenamiento')
plt.plot(historial.history['val_loss'], label='Pérdida de validación')
plt.title("Pérdida durante el entrenamiento")
plt.xlabel("Épocas")
plt.ylabel("Pérdida")
plt.legend()
plt.show()

# Graficar las regiones de decisión
xx, yy = np.meshgrid(
    np.linspace(X[:, 0].min() - 0.5, X[:, 0].max() + 0.5, 500),
    np.linspace(X[:, 1].min() - 0.5, X[:, 1].max() + 0.5, 500)
)
Z = modelo.predict(scaler.transform(np.c_[xx.ravel(), yy.ravel()]))
Z = Z.reshape(xx.shape)

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, levels=50, cmap='coolwarm', alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k', s=50)
plt.title("Regiones de decisión - Red Neuronal")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()