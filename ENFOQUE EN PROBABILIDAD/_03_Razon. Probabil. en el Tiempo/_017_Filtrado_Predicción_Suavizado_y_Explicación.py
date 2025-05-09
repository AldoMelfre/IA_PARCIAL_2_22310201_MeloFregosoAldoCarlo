import numpy as np

# ============================================
# FILTRADO
# ============================================
def filtrado(matriz_transicion, evidencia, estado_inicial, num_pasos):
    """
    Realiza el filtrado para calcular P(X_t | e_{1:t}).
    :param matriz_transicion: Matriz de transición (numpy array).
    :param evidencia: Lista de observaciones (probabilidades de emisión).
    :param estado_inicial: Distribución inicial de estados.
    :param num_pasos: Número de pasos a calcular.
    :return: Lista de distribuciones de probabilidad para cada paso.
    """
    distribuciones = [estado_inicial]  # Inicializar con la distribución inicial

    for t in range(num_pasos):
        # Predicción: Propagar la distribución hacia adelante
        prediccion = np.dot(distribuciones[-1], matriz_transicion)

        # Actualización: Incorporar la evidencia
        actualizacion = prediccion * evidencia[t]
        actualizacion /= np.sum(actualizacion)  # Normalizar

        distribuciones.append(actualizacion)

    return distribuciones

# ============================================
# PREDICCIÓN
# ============================================
def prediccion(matriz_transicion, distribucion_actual, pasos_futuros):
    """
    Realiza la predicción para calcular P(X_{t+k} | e_{1:t}).
    :param matriz_transicion: Matriz de transición (numpy array).
    :param distribucion_actual: Distribución actual de estados.
    :param pasos_futuros: Número de pasos hacia adelante.
    :return: Distribución de probabilidad en el futuro.
    """
    distribucion = distribucion_actual

    for _ in range(pasos_futuros):
        distribucion = np.dot(distribucion, matriz_transicion)

    return distribucion

# ============================================
# SUAVIZADO
# ============================================
def suavizado(matriz_transicion, distribuciones_filtradas, evidencia):
    """
    Realiza el suavizado para calcular P(X_k | e_{1:T}).
    :param matriz_transicion: Matriz de transición (numpy array).
    :param distribuciones_filtradas: Distribuciones filtradas hacia adelante.
    :param evidencia: Lista de observaciones (probabilidades de emisión).
    :return: Lista de distribuciones suavizadas.
    """
    T = len(distribuciones_filtradas) - 1
    suavizadas = [distribuciones_filtradas[-1]]  # Inicializar con la última distribución filtrada

    for t in range(T - 1, -1, -1):
        # Propagar hacia atrás
        posterior = suavizadas[0] * matriz_transicion.T
        posterior /= np.sum(posterior, axis=1)  # Normalizar
        suavizadas.insert(0, posterior)

    return suavizadas

# ============================================
# EJEMPLO: MATRIZ DE TRANSICIÓN Y EVIDENCIA
# ============================================
matriz_transicion = np.array([
    [0.7, 0.3],
    [0.4, 0.6]
])

evidencia = [
    np.array([0.9, 0.1]),  # Probabilidad de observación en el paso 1
    np.array([0.2, 0.8]),  # Probabilidad de observación en el paso 2
    np.array([0.4, 0.6])   # Probabilidad de observación en el paso 3
]

estado_inicial = np.array([0.6, 0.4])  # Distribución inicial de estados

# ============================================
# FILTRADO
# ============================================
distribuciones_filtradas = filtrado(matriz_transicion, evidencia, estado_inicial, len(evidencia))
print("Distribuciones filtradas:")
for t, dist in enumerate(distribuciones_filtradas):
    print(f"Paso {t}: {dist}")

# ============================================
# PREDICCIÓN
# ============================================
distribucion_futura = prediccion(matriz_transicion, distribuciones_filtradas[-1], 2)
print("\nDistribución futura (2 pasos adelante):", distribucion_futura)

# ============================================
# SUAVIZADO
# ============================================
distribuciones_suavizadas = suavizado(matriz_transicion, distribuciones_filtradas, evidencia)
print("\nDistribuciones suavizadas:")
for t, dist in enumerate(distribuciones_suavizadas):
    print(f"Paso {t}: {dist}")