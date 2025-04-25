# ============================================
# MDP PARCIALMENTE OBSERVABLE (POMDP)
# ============================================

# DESCRIPCIÓN TEÓRICA:
# Un MDP Parcialmente Observable (POMDP) es un modelo matemático para la toma de decisiones secuenciales
# en entornos donde el agente no puede observar directamente el estado actual. En lugar de eso, el agente
# mantiene una "creencia" (distribución de probabilidad) sobre los posibles estados.
# 
# COMPONENTES:
# - **Estados:** Representan las posibles situaciones del entorno.
# - **Acciones:** Decisiones que el agente puede tomar en cada estado.
# - **Observaciones:** Información parcial que el agente recibe sobre el estado actual.
# - **Transiciones:** Probabilidades de moverse entre estados al realizar una acción.
# - **Recompensas:** Beneficio inmediato obtenido al realizar una acción en un estado.
# - **Modelo de observación:** Probabilidades de recibir una observación dada una acción y un estado.
# - **Creencias:** Distribución de probabilidad sobre los estados posibles.
# 
# EJEMPLO:
# Un robot se encuentra en una cuadrícula 2x2 y debe llegar a un objetivo. Sin embargo, el robot no sabe
# exactamente dónde está, pero puede recibir observaciones que le ayudan a actualizar su creencia sobre
# su posición. El algoritmo calcula la política óptima basada en las creencias.

# ============================================
# FUNCIÓN PARA ACTUALIZAR LAS CREENCIAS
# ============================================
def actualizar_creencias(creencias, accion, observacion, transiciones, observaciones):
    """
    Actualiza las creencias del agente basándose en la acción realizada y la observación recibida.
    :param creencias: Diccionario con la distribución de probabilidad sobre los estados.
    :param accion: Acción realizada por el agente.
    :param observacion: Observación recibida después de realizar la acción.
    :param transiciones: Diccionario con las probabilidades de transición entre estados.
    :param observaciones: Diccionario con las probabilidades de observación.
    :return: Diccionario con las creencias actualizadas.
    """
    nuevas_creencias = {}

    # Iteramos sobre los posibles estados
    for estado in creencias:
        probabilidad = 0

        # Calculamos la probabilidad acumulada para el estado actual
        for estado_anterior in creencias:
            prob_transicion = transiciones.get((estado_anterior, accion, estado), 0)
            prob_observacion = observaciones.get((estado, accion, observacion), 0)
            probabilidad += creencias[estado_anterior] * prob_transicion * prob_observacion

        nuevas_creencias[estado] = probabilidad

    # Normalizamos las creencias para que sumen 1
    suma = sum(nuevas_creencias.values())
    if suma > 0:
        for estado in nuevas_creencias:
            nuevas_creencias[estado] /= suma

    return nuevas_creencias

# ============================================
# FUNCIÓN PARA RESOLVER UN POMDP
# ============================================
def resolver_pomdp(estados, acciones, observaciones, transiciones, recompensas, observaciones_modelo, gamma, epsilon):
    """
    Resuelve un POMDP utilizando un enfoque basado en creencias.
    :param estados: Lista de estados posibles.
    :param acciones: Lista de acciones posibles.
    :param observaciones: Lista de observaciones posibles.
    :param transiciones: Diccionario con las probabilidades de transición entre estados.
    :param recompensas: Diccionario con las recompensas inmediatas para cada estado y acción.
    :param observaciones_modelo: Diccionario con las probabilidades de observación.
    :param gamma: Factor de descuento (0 <= gamma <= 1).
    :param epsilon: Umbral de convergencia.
    :return: Política óptima basada en creencias.
    """
    # Inicializamos las creencias uniformemente
    creencias = {estado: 1 / len(estados) for estado in estados}

    # Inicializamos los valores de las creencias
    valores = {estado: 0 for estado in estados}

    while True:
        delta = 0  # Diferencia máxima entre valores consecutivos
        nuevos_valores = valores.copy()  # Copiamos los valores actuales

        # Iteramos sobre cada estado
        for estado in estados:
            max_valor = float('-inf')  # Inicializamos el valor máximo para el estado actual

            # Iteramos sobre cada acción
            for accion in acciones:
                # Calculamos el valor esperado para la acción actual
                valor_accion = sum(
                    transiciones.get((estado, accion, siguiente_estado), 0) *
                    (recompensas.get((estado, accion, siguiente_estado), 0) + gamma * valores[siguiente_estado])
                    for siguiente_estado in estados
                )
                max_valor = max(max_valor, valor_accion)  # Actualizamos el valor máximo

            nuevos_valores[estado] = max_valor  # Asignamos el valor máximo al estado
            delta = max(delta, abs(valores[estado] - nuevos_valores[estado]))  # Actualizamos delta

        valores = nuevos_valores  # Actualizamos los valores

        # Verificamos si hemos alcanzado la convergencia
        if delta < epsilon:
            break

    # Calculamos la política óptima basada en creencias
    politica = {}
    for estado in estados:
        mejor_accion = None
        mejor_valor = float('-inf')

        for accion in acciones:
            valor_accion = sum(
                transiciones.get((estado, accion, siguiente_estado), 0) *
                (recompensas.get((estado, accion, siguiente_estado), 0) + gamma * valores[siguiente_estado])
                for siguiente_estado in estados
            )
            if valor_accion > mejor_valor:
                mejor_valor = valor_accion
                mejor_accion = accion

        politica[estado] = mejor_accion

    return politica

# ============================================
# EJEMPLO: ROBOT EN UNA CUADRÍCULA 2x2
# ============================================
# Definimos los estados (posiciones en la cuadrícula)
estados = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Definimos las acciones
acciones = ["Arriba", "Abajo", "Izquierda", "Derecha"]

# Definimos las observaciones
observaciones = ["Nada", "Cerca del objetivo"]

# Definimos las probabilidades de transición
transiciones = {
    ((0, 0), "Derecha", (0, 1)): 1.0, ((0, 0), "Abajo", (1, 0)): 1.0,
    ((0, 1), "Izquierda", (0, 0)): 1.0, ((0, 1), "Abajo", (1, 1)): 1.0,
    ((1, 0), "Arriba", (0, 0)): 1.0, ((1, 0), "Derecha", (1, 1)): 1.0,
    ((1, 1), "Izquierda", (1, 0)): 1.0, ((1, 1), "Arriba", (0, 1)): 1.0,
}

# Definimos las recompensas inmediatas
recompensas = {
    ((0, 1), "Derecha", (0, 1)): 10,  # Recompensa por alcanzar el objetivo
    **{(estado, accion, siguiente_estado): -1 for estado in estados for accion in acciones for siguiente_estado in estados}
}

# Definimos el modelo de observación
observaciones_modelo = {
    ((0, 1), "Derecha", "Cerca del objetivo"): 1.0,
    ((1, 1), "Izquierda", "Cerca del objetivo"): 1.0,
    **{(estado, accion, "Nada"): 1.0 for estado in estados for accion in acciones}
}

# Factor de descuento
gamma = 0.9

# Umbral de convergencia
epsilon = 0.01

# Llamamos a la función para resolver el POMDP
politica = resolver_pomdp(estados, acciones, observaciones, transiciones, recompensas, observaciones_modelo, gamma, epsilon)

# Mostramos la política óptima
print("Política óptima basada en creencias:")
for estado, accion in politica.items():
    print(f"Estado {estado}: {accion}")