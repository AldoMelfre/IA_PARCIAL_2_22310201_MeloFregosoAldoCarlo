import numpy as np

# ============================================
# MODELO OCULTO DE MARKOV PARA RECONOCIMIENTO DEL HABLA
# ============================================
def reconocimiento_habla_hmm(matriz_transicion, matriz_emision, estado_inicial, observaciones):
    """
    Implementa el reconocimiento del habla utilizando un Modelo Oculto de Markov.
    :param matriz_transicion: Matriz de transición (numpy array).
    :param matriz_emision: Matriz de emisión (numpy array).
    :param estado_inicial: Distribución inicial de estados.
    :param observaciones: Lista de observaciones (índices enteros).
    :return: Secuencia más probable de estados.
    """
    num_estados = matriz_transicion.shape[0]
    num_observaciones = len(observaciones)

    # Matriz para almacenar las probabilidades máximas
    dp = np.zeros((num_observaciones, num_estados))
    # Matriz para rastrear los estados previos
    backtrack = np.zeros((num_observaciones, num_estados), dtype=int)

    # Inicialización
    dp[0] = estado_inicial * matriz_emision[:, observaciones[0]]

    # Rellenar la tabla dinámica
    for t in range(1, num_observaciones):
        for j in range(num_estados):
            prob_transiciones = dp[t-1] * matriz_transicion[:, j]
            dp[t, j] = np.max(prob_transiciones) * matriz_emision[j, observaciones[t]]
            backtrack[t, j] = np.argmax(prob_transiciones)

    # Reconstruir la secuencia más probable
    secuencia = np.zeros(num_observaciones, dtype=int)
    secuencia[-1] = np.argmax(dp[-1])
    for t in range(num_observaciones - 2, -1, -1):
        secuencia[t] = backtrack[t + 1, secuencia[t + 1]]

    return secuencia

# ============================================
# EJEMPLO: RECONOCIMIENTO DEL HABLA
# ============================================
# Matriz de transición (3 estados)
matriz_transicion = np.array([
    [0.7, 0.2, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])

# Matriz de emisión (3 estados, 4 observaciones posibles)
matriz_emision = np.array([
    [0.6, 0.2, 0.1, 0.1],  # Estado 0
    [0.1, 0.7, 0.1, 0.1],  # Estado 1
    [0.1, 0.2, 0.6, 0.1]   # Estado 2
])

# Distribución inicial de estados
estado_inicial = np.array([0.5, 0.3, 0.2])

# Secuencia de observaciones (índices de las observaciones)
observaciones = [0, 1, 2, 3, 2]

# ============================================
# EJECUTAR EL RECONOCIMIENTO DEL HABLA
# ============================================
secuencia_estados = reconocimiento_habla_hmm(matriz_transicion, matriz_emision, estado_inicial, observaciones)

# Mostrar los resultados
print("Secuencia más probable de estados:")
print(secuencia_estados)