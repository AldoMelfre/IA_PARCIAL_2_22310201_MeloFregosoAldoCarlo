import numpy as np  # Importa la biblioteca NumPy para realizar operaciones matemáticas y trabajar con arreglos.

# ============================================
# FUNCIONES DE ACTIVACIÓN
# ============================================

def sigmoide(z):
    """
    Función de activación Sigmoide.
    Convierte la entrada en un valor entre 0 y 1.
    :param z: Entrada (puede ser un escalar o un numpy array).
    :return: Salida transformada por la función sigmoide.
    """
    return 1 / (1 + np.exp(-z))  # Calcula la función sigmoide: 1 / (1 + e^(-z)).

def tanh(z):
    """
    Función de activación Tangente Hiperbólica.
    Convierte la entrada en un valor entre -1 y 1.
    :param z: Entrada (puede ser un escalar o un numpy array).
    :return: Salida transformada por la función tangente hiperbólica.
    """
    return np.tanh(z)  # Calcula la tangente hiperbólica: (e^z - e^(-z)) / (e^z + e^(-z)).

def relu(z):
    """
    Función de activación ReLU (Rectified Linear Unit).
    Devuelve 0 para valores negativos y el valor original para valores positivos.
    :param z: Entrada (puede ser un escalar o un numpy array).
    :return: Salida transformada por la función ReLU.
    """
    return np.maximum(0, z)  # Devuelve el máximo entre 0 y z.

def leaky_relu(z, alpha=0.01):
    """
    Función de activación Leaky ReLU.
    Similar a ReLU, pero permite un pequeño gradiente para valores negativos.
    :param z: Entrada (puede ser un escalar o un numpy array).
    :param alpha: Pendiente para valores negativos (por defecto 0.01).
    :return: Salida transformada por la función Leaky ReLU.
    """
    return np.where(z > 0, z, alpha * z)  # Si z > 0, devuelve z; de lo contrario, devuelve alpha * z.

def softmax(z):
    """
    Función de activación Softmax.
    Convierte un vector en una distribución de probabilidad (suma de salidas = 1).
    :param z: Entrada (numpy array).
    :return: Salida transformada por la función Softmax.
    """
    exp_z = np.exp(z - np.max(z))  # Calcula e^z para cada elemento, restando el máximo para evitar overflow numérico.
    return exp_z / np.sum(exp_z, axis=0)  # Normaliza dividiendo cada valor por la suma total.

# ============================================
# EJEMPLO: USO DE FUNCIONES DE ACTIVACIÓN
# ============================================

z = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])  # Define un arreglo de entrada con valores de prueba.

# Imprime los resultados de cada función de activación para la entrada z.
print("Sigmoide:", sigmoide(z))  # Aplica la función sigmoide a z y muestra el resultado.
print("Tanh:", tanh(z))  # Aplica la función tangente hiperbólica a z y muestra el resultado.
print("ReLU:", relu(z))  # Aplica la función ReLU a z y muestra el resultado.
print("Leaky ReLU:", leaky_relu(z))  # Aplica la función Leaky ReLU a z y muestra el resultado.
print("Softmax:", softmax(z))  # Aplica la función Softmax a z y muestra el resultado.