# ============================================
# EXPLORACIÓN VS. EXPLOTACIÓN: ESTRATEGIA EPSILON-GREEDY
# ============================================

import random

# DESCRIPCIÓN TEÓRICA:
# El dilema de exploración vs. explotación se refiere a cómo un agente decide entre:
# - **Explorar:** Probar nuevas acciones para descubrir más información sobre el entorno.
# - **Explotar:** Elegir la mejor acción conocida para maximizar la recompensa inmediata.
# 
# La estrategia **epsilon-greedy** equilibra exploración y explotación:
# - Con probabilidad `epsilon`, el agente explora eligiendo una acción aleatoria.
# - Con probabilidad `1 - epsilon`, el agente explota eligiendo la mejor acción conocida.

# ============================================
# FUNCIÓN PARA EXPLORACIÓN VS. EXPLOTACIÓN
# ============================================
def epsilon_greedy(q_values, estado_actual, acciones, epsilon):
    """
    Implementa la estrategia epsilon-greedy para seleccionar una acción.
    :param q_values: Diccionario con los valores Q para cada estado y acción.
    :param estado_actual: El estado actual del agente.
    :param acciones: Lista de acciones posibles.
    :param epsilon: Probabilidad de exploración (0 <= epsilon <= 1).
    :return: Acción seleccionada.
    """
    import random

    # Decidimos si explorar o explotar
    if random.random() < epsilon:
        # Exploración: Elegimos una acción aleatoria
        accion = random.choice(acciones)
        print(f"Explorando: Acción aleatoria seleccionada -> {accion}")
    else:
        # Explotación: Elegimos la mejor acción conocida
        accion = max(acciones, key=lambda a: q_values.get((estado_actual, a), 0))
        print(f"Explotando: Mejor acción conocida seleccionada -> {accion}")

    return accion

# ============================================
# EJEMPLO: USO DE EPSILON-GREEDY
# ============================================
# Definimos los estados y acciones
estados = ["A", "B", "C"]
acciones = ["Izquierda", "Derecha"]

# Inicializamos los valores Q (simulados)
q_values = {
    ("A", "Izquierda"): 5,
    ("A", "Derecha"): 10,
    ("B", "Izquierda"): 2,
    ("B", "Derecha"): 8,
    ("C", "Izquierda"): 7,
    ("C", "Derecha"): 3,
}

# Parámetros de la estrategia epsilon-greedy
epsilon = 0.2  # Probabilidad de exploración
estado_actual = "A"  # Estado inicial

# Seleccionamos una acción usando epsilon-greedy
accion_seleccionada = epsilon_greedy(q_values, estado_actual, acciones, epsilon)
print(f"Acción seleccionada en el estado {estado_actual}: {accion_seleccionada}")

# ============================================
# SIMULACIÓN DE VARIAS ITERACIONES
# ============================================
print("\nSimulación de varias iteraciones:")
for i in range(10):
    estado_actual = random.choice(estados)  # Seleccionamos un estado aleatorio
    accion_seleccionada = epsilon_greedy(q_values, estado_actual, acciones, epsilon)
    print(f"Iteración {i + 1}: Estado {estado_actual}, Acción {accion_seleccionada}")