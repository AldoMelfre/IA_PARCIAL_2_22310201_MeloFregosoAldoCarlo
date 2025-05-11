# Importar librerías necesarias
import numpy as np  # Para operaciones matemáticas y manejo de arrays
import tensorflow as tf  # Framework para construir y entrenar redes neuronales
from tensorflow.keras.models import Sequential  # Para definir modelos secuenciales
from tensorflow.keras.layers import Dense  # Para agregar capas densas (fully connected)
from sklearn.datasets import make_regression  # Para generar un conjunto de datos de regresión
from sklearn.model_selection import train_test_split  # Para dividir los datos en entrenamiento y prueba
from sklearn.preprocessing import StandardScaler  # Para escalar los datos
import matplotlib.pyplot as plt  # Para graficar y visualizar resultados

# ============================================
# GENERAR DATOS DE EJEMPLO
# ============================================
# Crear un conjunto de datos de regresión
X, y = make_regression(n_samples=1000, n_features=1, noise=15, random_state=42)
# X: Características (entrada)
# y: Etiquetas (salida)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Escalar los datos para normalizarlos (mejora la convergencia del modelo)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # Ajustar y transformar los datos de entrenamiento
X_test = scaler.transform(X_test)  # Transformar los datos de prueba

# ============================================
# CREAR EL MODELO DE RED NEURONAL
# ============================================
# Definir el modelo secuencial
modelo = Sequential([
    Dense(16, activation='relu', input_shape=(X_train.shape[1],)),  # Capa oculta con 16 neuronas y activación ReLU
    Dense(8, activation='relu'),  # Segunda capa oculta con 8 neuronas y activación ReLU
    Dense(1)  # Capa de salida con 1 neurona (para regresión)
])

# Compilar el modelo
modelo.compile(optimizer='adam', loss='mse', metrics=['mae'])
# Optimizer: Adam (ajusta los pesos de la red)
# Loss: Error cuadrático medio (MSE) para problemas de regresión
# Métrica: Error absoluto medio (MAE) para evaluar el rendimiento

# ============================================
# ENTRENAR EL MODELO
# ============================================
# Entrenar la red neuronal
historial = modelo.fit(
    X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1
)
# epochs: Número de veces que el modelo verá los datos completos
# batch_size: Número de muestras procesadas antes de actualizar los pesos
# validation_split: Porcentaje de datos usados para validación

# ============================================
# EVALUAR EL MODELO
# ============================================
# Evaluar el modelo en los datos de prueba
resultados = modelo.evaluate(X_test, y_test, verbose=0)
print(f"Error cuadrático medio (MSE) en prueba: {resultados[0]}")
print(f"Error absoluto medio (MAE) en prueba: {resultados[1]}")

# ============================================
# HACER PREDICCIONES
# ============================================
# Generar predicciones para los datos de prueba
y_pred = modelo.predict(X_test)

# ============================================
# VISUALIZAR LOS RESULTADOS
# ============================================
# Graficar los datos reales vs las predicciones
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Datos reales')  # Datos reales
plt.scatter(X_test, y_pred, color='red', label='Predicciones')  # Predicciones del modelo
plt.title("Regresión con Red Neuronal")
plt.xlabel("Entrada (X)")
plt.ylabel("Salida (y)")
plt.legend()
plt.show()

# Graficar la pérdida durante el entrenamiento
plt.figure(figsize=(8, 6))
plt.plot(historial.history['loss'], label='Pérdida de entrenamiento')
plt.plot(historial.history['val_loss'], label='Pérdida de validación')
plt.title("Pérdida durante el entrenamiento")
plt.xlabel("Épocas")
plt.ylabel("Pérdida (MSE)")
plt.legend()
plt.show()