# ============================================
# APRENDIZAJE POR REFUERZO ACTIVO: Q-LEARNING
# ============================================

# DESCRIPCIÓN TEÓRICA:
# El aprendizaje por refuerzo activo permite al agente aprender una política óptima explorando activamente
# el entorno. El agente toma decisiones basándose en una política inicial, observa las recompensas y
# actualiza los valores de las acciones para mejorar su política.
# 
# COMPONENTES:
# - **Estados:** Representan las posibles situaciones del entorno.
# - **Acciones:** Decisiones que el agente puede tomar en cada estado.
# - **Recompensas:** Beneficio inmediato obtenido al realizar una acción en un estado.
# - **Q-Values:** Valores que representan la calidad de una acción en un estado.
# 
# EJEMPLO:
# Un robot se encuentra en una cuadrícula 3x3 y debe aprender a llegar a un objetivo con la mayor recompensa.
# - Cada movimiento tiene un costo de -1 (energía gastada).
# - Si el robot llega al objetivo, obtiene una recompensa de +10.
# - El robot explora el entorno y aprende la política óptima utilizando Q-Learning.

# ============================================
# FUNCIÓN PARA APRENDIZAJE POR REFUERZO ACTIVO (Q-LEARNING)
# ============================================
def q_learning(estados, acciones, transiciones, recompensas, gamma, alpha, epsilon, episodios):
    """
    Implementa el algoritmo de Q-Learning para aprendizaje por refuerzo activo.
    :param estados: Lista de estados posibles.
    :param acciones: Lista de acciones posibles.
    :param transiciones: Diccionario con las probabilidades de transición entre estados.
    :param recompensas: Diccionario con las recompensas inmediatas para cada estado y acción.
    :param gamma: Factor de descuento (0 <= gamma <= 1).
    :param alpha: Tasa de aprendizaje (0 <= alpha <= 1).
    :param epsilon: Probabilidad de exploración (0 <= epsilon <= 1).
    :param episodios: Número de episodios para entrenar.
    :return: Diccionario con los valores Q aprendidos y la política óptima.
    """
    import random

    # Inicializamos los valores Q en 0
    q_values = {(estado, accion): 0 for estado in estados for accion in acciones}

    # Iteramos sobre los episodios
    for _ in range(episodios):
        # Seleccionamos un estado inicial aleatorio
        estado_actual = random.choice(estados)

        # Seguimos explorando hasta que terminemos el episodio
        while True:
            # Elegimos una acción usando la política epsilon-greedy
            if random.random() < epsilon:
                accion = random.choice(acciones)  # Exploración
            else:
                accion = max(acciones, key=lambda a: q_values[(estado_actual, a)])  # Explotación

            # Simulamos la transición al siguiente estado
            siguiente_estado = obtener_siguiente_estado(estado_actual, accion, transiciones)
            recompensa = recompensas.get((estado_actual, accion, siguiente_estado), 0)

            # Actualizamos el valor Q usando la ecuación de Q-Learning
            mejor_q_siguiente = max(q_values[(siguiente_estado, a)] for a in acciones)
            q_values[(estado_actual, accion)] += alpha * (
                recompensa + gamma * mejor_q_siguiente - q_values[(estado_actual, accion)]
            )

            # Si llegamos a un estado terminal, terminamos el episodio
            if es_estado_terminal(siguiente_estado):
                break

            # Actualizamos el estado actual
            estado_actual = siguiente_estado

    # Derivamos la política óptima a partir de los valores Q
    politica = {
        estado: max(acciones, key=lambda a: q_values[(estado, a)])
        for estado in estados
    }

    return q_values, politica

# ============================================
# FUNCIONES AUXILIARES
# ============================================
def obtener_siguiente_estado(estado_actual, accion, transiciones):
    """
    Simula la transición al siguiente estado basándose en las probabilidades.
    :param estado_actual: Estado actual.
    :param accion: Acción tomada.
    :param transiciones: Diccionario con las probabilidades de transición.
    :return: Siguiente estado.
    """
    import random
    probabilidades = [
        (siguiente_estado, prob)
        for (estado, accion_actual, siguiente_estado), prob in transiciones.items()
        if estado == estado_actual and accion_actual == accion
    ]

    # Si no hay transiciones definidas, devolvemos el estado actual
    if not probabilidades:
        print(f"Advertencia: No se encontraron transiciones para el estado {estado_actual} con la acción {accion}.")
        return estado_actual

    # Seleccionamos el siguiente estado basado en las probabilidades
    estados, probs = zip(*probabilidades)
    return random.choices(estados, probs)[0]

def es_estado_terminal(estado):
    """
    Verifica si un estado es terminal.
    :param estado: Estado a verificar.
    :return: True si el estado es terminal, False en caso contrario.
    """
    # Consideramos que el estado (0, 2) es terminal en este ejemplo
    return estado == (0, 2)

# ============================================
# EJEMPLO: ROBOT EN UNA CUADRÍCULA
# ============================================
# Definimos los estados (posiciones en la cuadrícula)
estados = [(x, y) for x in range(3) for y in range(3)]

# Definimos las acciones
acciones = ["Arriba", "Abajo", "Izquierda", "Derecha"]

# Definimos las probabilidades de transición
transiciones = {
    ((0, 0), "Derecha", (0, 1)): 1.0, ((0, 0), "Abajo", (1, 0)): 1.0,
    ((0, 1), "Derecha", (0, 2)): 1.0, ((0, 1), "Izquierda", (0, 0)): 1.0, ((0, 1), "Abajo", (1, 1)): 1.0,
    ((0, 2), "Izquierda", (0, 1)): 1.0,
    ((1, 0), "Arriba", (0, 0)): 1.0, ((1, 0), "Derecha", (1, 1)): 1.0, ((1, 0), "Abajo", (2, 0)): 1.0,
    ((1, 1), "Arriba", (0, 1)): 1.0, ((1, 1), "Derecha", (1, 2)): 1.0, ((1, 1), "Izquierda", (1, 0)): 1.0, ((1, 1), "Abajo", (2, 1)): 1.0,
    ((1, 2), "Izquierda", (1, 1)): 1.0, ((1, 2), "Arriba", (0, 2)): 1.0, ((1, 2), "Abajo", (2, 2)): 1.0,
    ((2, 0), "Arriba", (1, 0)): 1.0, ((2, 0), "Derecha", (2, 1)): 1.0,
    ((2, 1), "Izquierda", (2, 0)): 1.0, ((2, 1), "Arriba", (1, 1)): 1.0, ((2, 1), "Derecha", (2, 2)): 1.0,
    ((2, 2), "Izquierda", (2, 1)): 1.0, ((2, 2), "Arriba", (1, 2)): 1.0,
}

# Definimos las recompensas inmediatas
recompensas = {
    ((0, 2), "Derecha", (0, 2)): 10,  # Recompensa por alcanzar el objetivo
    **{(estado, accion, siguiente_estado): -1 for estado in estados for accion in acciones for siguiente_estado in estados}
}

# Parámetros del algoritmo
gamma = 0.9  # Factor de descuento
alpha = 0.1  # Tasa de aprendizaje
epsilon = 0.1  # Probabilidad de exploración
episodios = 1000  # Número de episodios

# Llamamos a la función de Q-Learning
q_values, politica_optima = q_learning(estados, acciones, transiciones, recompensas, gamma, alpha, epsilon, episodios)

# Mostramos la política óptima aprendida
print("Política óptima aprendida:")
for estado, accion in politica_optima.items():
    print(f"Estado {estado}: {accion}")