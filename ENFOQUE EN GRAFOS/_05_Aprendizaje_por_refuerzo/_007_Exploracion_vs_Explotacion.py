# ============================================
# EXPLORACIÓN VS. EXPLOTACIÓN: EPSILON-GREEDY CON BÚSQUEDA DE POLÍTICA
# ============================================

import random

# DESCRIPCIÓN TEÓRICA:
# Este azlgoritmo utiliza la estrategia epsilon-greedy para equilibrar exploración y explotación.
# Además, busca la política óptima seleccionando la mejor acción para cada estado según los valores Q aprendidos.

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
# FUNCIÓN PARA BUSCAR LA POLÍTICA ÓPTIMA
# ============================================
def buscar_politica_optima(q_values, estados, acciones):
    """
    Busca la política óptima seleccionando la mejor acción para cada estado.
    :param q_values: Diccionario con los valores Q para cada estado y acción.
    :param estados: Lista de estados posibles.
    :param acciones: Lista de acciones posibles.
    :return: Diccionario con la política óptima.
    """
    politica_optima = {}
    for estado in estados:
        # Seleccionamos la acción con el mayor valor Q para el estado actual
        mejor_accion = max(acciones, key=lambda a: q_values.get((estado, a), 0))
        politica_optima[estado] = mejor_accion
    return politica_optima

# ============================================
# EJEMPLO: USO DE EPSILON-GREEDY Y BÚSQUEDA DE POLÍTICA
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

# Buscamos la política óptima
politica_optima = buscar_politica_optima(q_values, estados, acciones)
print("\nPolítica óptima encontrada:")
for estado, accion in politica_optima.items():
    print(f"Estado {estado}: {accion}")

# ============================================
# SIMULACIÓN DE VARIAS ITERACIONES
# ============================================
print("\nSimulación de varias iteraciones:")
for i in range(10):
    estado_actual = random.choice(estados)  # Seleccionamos un estado aleatorio
    accion_seleccionada = epsilon_greedy(q_values, estado_actual, acciones, epsilon)
    print(f"Iteración {i + 1}: Estado {estado_actual}, Acción {accion_seleccionada}")