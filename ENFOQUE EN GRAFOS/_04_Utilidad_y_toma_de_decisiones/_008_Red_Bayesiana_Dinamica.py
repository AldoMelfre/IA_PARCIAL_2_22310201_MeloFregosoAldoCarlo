# ============================================
# RED BAYESIANA DINÁMICA (DBN)
# ============================================

# DESCRIPCIÓN TEÓRICA:
# Una Red Bayesiana Dinámica (DBN) es un modelo probabilístico que representa la evolución de un sistema
# a lo largo del tiempo. Es una extensión de las redes bayesianas que incluye dependencias temporales.
# 
# COMPONENTES:
# - **Estados:** Representan las variables del sistema en un momento dado.
# - **Evidencias:** Observaciones que se obtienen en cada instante de tiempo.
# - **Transiciones:** Probabilidades de pasar de un estado a otro en el siguiente instante.
# - **Modelo de observación:** Probabilidades de observar una evidencia dada un estado.
# 
# EJEMPLO:
# Un robot se mueve en un pasillo y puede estar en una de tres posiciones: izquierda, centro o derecha.
# - El robot tiene un 80% de probabilidad de permanecer en su posición actual y un 10% de moverse a cada posición adyacente.
# - Un sensor indica la posición del robot, pero con un 20% de error.
# - El objetivo es calcular la distribución de probabilidad sobre las posiciones del robot en el tiempo.

# ============================================
# FUNCIÓN PARA ACTUALIZAR LAS CREENCIAS
# ============================================
def actualizar_creencias(creencias, evidencia, transiciones, observaciones):
    """
    Actualiza las creencias del sistema basándose en la evidencia observada.
    :param creencias: Diccionario con la distribución de probabilidad sobre los estados actuales.
    :param evidencia: Evidencia observada en el tiempo actual.
    :param transiciones: Diccionario con las probabilidades de transición entre estados.
    :param observaciones: Diccionario con las probabilidades de observación.
    :return: Diccionario con las creencias actualizadas.
    """
    nuevas_creencias = {}

    # Iteramos sobre los posibles estados
    for estado_actual in creencias:
        probabilidad = 0

        # Calculamos la probabilidad acumulada para el estado actual
        for estado_anterior in creencias:
            prob_transicion = transiciones.get((estado_anterior, estado_actual), 0)
            probabilidad += creencias[estado_anterior] * prob_transicion

        # Multiplicamos por la probabilidad de la evidencia observada
        prob_observacion = observaciones.get((estado_actual, evidencia), 0)
        nuevas_creencias[estado_actual] = probabilidad * prob_observacion

    # Normalizamos las creencias para que sumen 1
    suma = sum(nuevas_creencias.values())
    if suma > 0:
        for estado in nuevas_creencias:
            nuevas_creencias[estado] /= suma

    return nuevas_creencias

# ============================================
# EJEMPLO: ROBOT EN UN PASILLO
# ============================================
# Definimos los estados (posiciones en el pasillo)
estados = ["Izquierda", "Centro", "Derecha"]

# Definimos las probabilidades de transición entre estados
transiciones = {
    ("Izquierda", "Izquierda"): 0.8, ("Izquierda", "Centro"): 0.2,
    ("Centro", "Izquierda"): 0.1, ("Centro", "Centro"): 0.8, ("Centro", "Derecha"): 0.1,
    ("Derecha", "Centro"): 0.2, ("Derecha", "Derecha"): 0.8,
}

# Definimos las probabilidades de observación (sensor)
observaciones = {
    ("Izquierda", "Izquierda"): 0.8, ("Izquierda", "Centro"): 0.1, ("Izquierda", "Derecha"): 0.1,
    ("Centro", "Izquierda"): 0.2, ("Centro", "Centro"): 0.6, ("Centro", "Derecha"): 0.2,
    ("Derecha", "Izquierda"): 0.1, ("Derecha", "Centro"): 0.1, ("Derecha", "Derecha"): 0.8,
}

# Inicializamos las creencias uniformemente
creencias = {estado: 1 / len(estados) for estado in estados}

# Definimos una secuencia de evidencias observadas
evidencias = ["Izquierda", "Centro", "Derecha", "Centro"]

# Iteramos sobre las evidencias para actualizar las creencias
for t, evidencia in enumerate(evidencias):
    print(f"\nTiempo {t + 1}, Evidencia observada: {evidencia}")
    creencias = actualizar_creencias(creencias, evidencia, transiciones, observaciones)
    for estado, probabilidad in creencias.items():
        print(f"Estado {estado}: {probabilidad:.2f}")