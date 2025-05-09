import numpy as np

# ============================================
# ALGORITMO HACIA DELANTE-ATRÁS
# ============================================
def hacia_delante_atras(matriz_transicion, matriz_emision, estado_inicial, observaciones):
    """
    Implementa el algoritmo Hacia Delante-Atrás para un Modelo Oculto de Markov.
    :param matriz_transicion: Matriz de transición (numpy array).
    :param matriz_emision: Matriz de emisión (numpy array).
    :param estado_inicial: Distribución inicial de estados.
    :param observaciones: Lista de observaciones (índices enteros).
    :return: Probabilidades posteriores para cada estado en cada tiempo.
    """
    num_estados = matriz_transicion.shape[0]
    num_observaciones = len(observaciones)

    # ============================================
    # HACIA ADELANTE (FORWARD)
    # ============================================
    alpha = np.zeros((num_observaciones, num_estados))
    alpha[0] = estado_inicial * matriz_emision[:, observaciones[0]]

    for t in range(1, num_observaciones):
        for j in range(num_estados):
            alpha[t, j] = np.sum(alpha[t-1] * matriz_transicion[:, j]) * matriz_emision[j, observaciones[t]]

    # ============================================
    # HACIA ATRÁS (BACKWARD)
    # ============================================
    beta = np.zeros((num_observaciones, num_estados))
    beta[-1] = 1  # Inicializar con 1 en el último paso

    for t in range(num_observaciones - 2, -1, -1):
        for i in range(num_estados):
            beta[t, i] = np.sum(beta[t+1] * matriz_transicion[i, :] * matriz_emision[:, observaciones[t+1]])

    # ============================================
    # COMBINAR HACIA ADELANTE Y HACIA ATRÁS
    # ============================================
    posterior = alpha * beta
    posterior /= np.sum(posterior, axis=1, keepdims=True)  # Normalizar

    return posterior

# ============================================
# EJEMPLO: MODELO OCULTO DE MARKOV
# ============================================
# Matriz de transición (2 estados)
matriz_transicion = np.array([
    [0.7, 0.3],
    [0.4, 0.6]
])

# Matriz de emisión (2 estados, 3 observaciones posibles)
matriz_emision = np.array([
    [0.9, 0.1, 0.0],  # Estado 0
    [0.2, 0.3, 0.5]   # Estado 1
])

# Distribución inicial de estados
estado_inicial = np.array([0.6, 0.4])

# Secuencia de observaciones (índices de las observaciones)
observaciones = [0, 1, 2]

# ============================================
# EJECUTAR EL ALGORITMO HACIA DELANTE-ATRÁS
# ============================================
posterior = hacia_delante_atras(matriz_transicion, matriz_emision, estado_inicial, observaciones)

# Mostrar los resultados
print("Probabilidades posteriores:")
for t, dist in enumerate(posterior):
    print(f"Tiempo {t}: {dist}")