# Importar librerías necesarias
import numpy as np  # Para realizar operaciones matemáticas y manejo de arrays
import tensorflow as tf  # Framework para construir y entrenar modelos de aprendizaje profundo
from tensorflow.keras.models import Sequential  # Para definir modelos secuenciales de redes neuronales
from tensorflow.keras.layers import Dense  # Para agregar capas densas (fully connected) a la red neuronal
from sklearn.datasets import make_moons  # Para generar un conjunto de datos no linealmente separable
from sklearn.model_selection import train_test_split  # Para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.preprocessing import StandardScaler  # Para escalar los datos y normalizarlos
from sklearn.metrics import accuracy_score  # Para calcular la precisión del modelo
import matplotlib.pyplot as plt  # Para graficar y visualizar los resultados

# ============================================
# GENERAR DATOS DE EJEMPLO
# ============================================
# Crear un conjunto de datos no linealmente separable
X, y = make_moons(n_samples=1000, noise=0.1, random_state=42)  # Genera datos en forma de dos lunas con ruido

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # 70% entrenamiento, 30% prueba

# Escalar los datos
scaler = StandardScaler()  # Inicializa el escalador para normalizar los datos
X_train = scaler.fit_transform(X_train)  # Ajusta el escalador a los datos de entrenamiento y los transforma
X_test = scaler.transform(X_test)  # Transforma los datos de prueba usando el mismo escalador

# ============================================
# CREAR EL MODELO DE RED NEURONAL
# ============================================
# Definir el modelo secuencial
modelo = Sequential([  # Crea un modelo secuencial, donde las capas se apilan una tras otra
    Dense(16, activation='relu', input_shape=(X_train.shape[1],)),  # Capa oculta con 16 neuronas y activación ReLU
    Dense(8, activation='relu'),  # Segunda capa oculta con 8 neuronas y activación ReLU
    Dense(1, activation='sigmoid')  # Capa de salida con 1 neurona y activación sigmoide (para clasificación binaria)
])

# Compilar el modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  
# Configura el modelo con el optimizador Adam, función de pérdida binaria y métrica de precisión

# ============================================
# ENTRENAR EL MODELO
# ============================================
# Entrenar la red neuronal
historial = modelo.fit(
    X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1
)  # Entrena el modelo durante 50 épocas con un tamaño de lote de 32 y 20% de validación

# ============================================
# EVALUAR EL MODELO
# ============================================
# Evaluar el modelo en los datos de prueba
y_pred = (modelo.predict(X_test) > 0.5).astype("int32")  # Genera predicciones y las convierte a 0 o 1
precision = accuracy_score(y_test, y_pred)  # Calcula la precisión comparando las predicciones con las etiquetas reales
print("Precisión del modelo de Aprendizaje Profundo:", precision)  # Imprime la precisión del modelo

# ============================================
# VISUALIZAR LOS RESULTADOS
# ============================================
# Graficar la pérdida durante el entrenamiento
plt.figure(figsize=(8, 6))  # Configura el tamaño de la figura
plt.plot(historial.history['loss'], label='Pérdida de entrenamiento')  # Grafica la pérdida en entrenamiento
plt.plot(historial.history['val_loss'], label='Pérdida de validación')  # Grafica la pérdida en validación
plt.title("Pérdida durante el entrenamiento")  # Título del gráfico
plt.xlabel("Épocas")  # Etiqueta del eje x
plt.ylabel("Pérdida")  # Etiqueta del eje y
plt.legend()  # Muestra la leyenda
plt.show()  # Muestra el gráfico

# Graficar las regiones de decisión
xx, yy = np.meshgrid(
    np.linspace(X[:, 0].min() - 0.5, X[:, 0].max() + 0.5, 500),  # Genera una cuadrícula de valores para el eje x
    np.linspace(X[:, 1].min() - 0.5, X[:, 1].max() + 0.5, 500)   # Genera una cuadrícula de valores para el eje y
)
Z = modelo.predict(scaler.transform(np.c_[xx.ravel(), yy.ravel()]))  # Predice las clases para cada punto de la cuadrícula
Z = Z.reshape(xx.shape)  # Reshape para que coincida con la cuadrícula

plt.figure(figsize=(8, 6))  # Configura el tamaño de la figura
plt.contourf(xx, yy, Z, levels=50, cmap='coolwarm', alpha=0.8)  # Grafica las regiones de decisión
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k', s=50)  # Grafica los puntos de datos originales
plt.title("Regiones de decisión - Red Neuronal")  # Título del gráfico
plt.xlabel("Característica 1")  # Etiqueta del eje x
plt.ylabel("Característica 2")  # Etiqueta del eje y
plt.show()  # Muestra el gráfico