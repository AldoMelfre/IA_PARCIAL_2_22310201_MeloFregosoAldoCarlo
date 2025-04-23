# ============================================
# ITERACIÓN DE POLÍTICAS
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La iteración de políticas es un algoritmo utilizado para resolver problemas de toma de decisiones secuenciales,
# como los Procesos de Decisión de Markov (MDP). Este enfoque alterna entre:
# 1. **Evaluación de la política:** Calcula los valores de los estados para una política fija.
# 2. **Mejora de la política:** Actualiza la política seleccionando las mejores acciones basadas en los valores calculados.
# 
# EJEMPLO:
# Un robot se encuentra en una cuadrícula 3x3 y debe llegar a un objetivo en la esquina superior derecha.
# - Cada movimiento tiene una recompensa de -1 (costo de energía).
# - Si el robot llega al objetivo, obtiene una recompensa de +10.
# - El robot puede moverse hacia arriba, abajo, izquierda o derecha.
# - El algoritmo calcula la política óptima para que el robot alcance el objetivo con la mayor recompensa acumulada.

# ============================================
# FUNCIÓN PARA EVALUAR UNA POLÍTICA
# ============================================
def evaluar_politica(estados, politica, transiciones, recompensas, gamma, epsilon):
    """
    Evalúa una política fija calculando los valores de los estados.
    :param estados: Lista de estados posibles.
    :param politica: Diccionario que asigna una acción a cada estado.
    :param transiciones: Diccionario con las probabilidades de transición entre estados.
    :param recompensas: Diccionario con las recompensas inmediatas para cada estado y acción.
    :param gamma: Factor de descuento (0 <= gamma <= 1).
    :param epsilon: Umbral de convergencia.
    :return: Diccionario con los valores de los estados para la política dada.
    """
    valores = {estado: 0 for estado in estados}  # Inicializamos los valores de los estados en 0

    while True:
        delta = 0  # Diferencia máxima entre valores consecutivos
        nuevos_valores = valores.copy()  # Copiamos los valores actuales

        # Iteramos sobre cada estado
        for estado in estados:
            accion = politica[estado]  # Obtenemos la acción de la política actual
            # Calculamos el valor esperado para la acción actual
            nuevos_valores[estado] = sum(
                transiciones.get((estado, accion, siguiente_estado), 0) *
                (recompensas.get((estado, accion, siguiente_estado), 0) + gamma * valores[siguiente_estado])
                for siguiente_estado in estados
            )
            delta = max(delta, abs(valores[estado] - nuevos_valores[estado]))  # Actualizamos delta

        valores = nuevos_valores  # Actualizamos los valores

        # Verificamos si hemos alcanzado la convergencia
        if delta < epsilon:
            break

    return valores

# ============================================
# FUNCIÓN PARA MEJORAR UNA POLÍTICA
# ============================================
def mejorar_politica(estados, acciones, valores, transiciones, recompensas, gamma):
    """
    Mejora una política seleccionando las mejores acciones basadas en los valores calculados.
    :param estados: Lista de estados posibles.
    :param acciones: Lista de acciones posibles.
    :param valores: Diccionario con los valores de los estados.
    :param transiciones: Diccionario con las probabilidades de transición entre estados.
    :param recompensas: Diccionario con las recompensas inmediatas para cada estado y acción.
    :param gamma: Factor de descuento (0 <= gamma <= 1).
    :return: Diccionario con la política mejorada.
    """
    nueva_politica = {}

    # Iteramos sobre cada estado
    for estado in estados:
        mejor_accion = None
        mejor_valor = float('-inf')

        # Iteramos sobre cada acción
        for accion in acciones:
            # Calculamos el valor esperado para la acción actual
            valor_accion = sum(
                transiciones.get((estado, accion, siguiente_estado), 0) *
                (recompensas.get((estado, accion, siguiente_estado), 0) + gamma * valores[siguiente_estado])
                for siguiente_estado in estados
            )
            if valor_accion > mejor_valor:
                mejor_valor = valor_accion
                mejor_accion = accion

        nueva_politica[estado] = mejor_accion  # Asignamos la mejor acción al estado

    return nueva_politica

# ============================================
# FUNCIÓN PRINCIPAL DE ITERACIÓN DE POLÍTICAS
# ============================================
def iteracion_de_politicas(estados, acciones, transiciones, recompensas, gamma, epsilon):
    """
    Implementa el algoritmo de iteración de políticas.
    :param estados: Lista de estados posibles.
    :param acciones: Lista de acciones posibles.
    :param transiciones: Diccionario con las probabilidades de transición entre estados.
    :param recompensas: Diccionario con las recompensas inmediatas para cada estado y acción.
    :param gamma: Factor de descuento (0 <= gamma <= 1).
    :param epsilon: Umbral de convergencia.
    :return: Diccionario con los valores óptimos de los estados y la política óptima.
    """
    # Inicializamos una política aleatoria
    politica = {estado: acciones[0] for estado in estados}

    while True:
        # Evaluamos la política actual
        valores = evaluar_politica(estados, politica, transiciones, recompensas, gamma, epsilon)

        # Mejoramos la política
        nueva_politica = mejorar_politica(estados, acciones, valores, transiciones, recompensas, gamma)

        # Verificamos si la política ha cambiado
        if nueva_politica == politica:
            break

        politica = nueva_politica  # Actualizamos la política

    return valores, politica

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
    ((0, 2), "Izquierda", (0, 1)): 1.0,  # Objetivo
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

# Factor de descuento
gamma = 0.9

# Umbral de convergencia
epsilon = 0.01

# Llamamos a la función de iteración de políticas
valores, politica = iteracion_de_politicas(estados, acciones, transiciones, recompensas, gamma, epsilon)

# Mostramos los resultados
print("Valores óptimos de los estados:")
for estado, valor in valores.items():
    print(f"Estado {estado}: {valor:.2f}")

print("\nPolítica óptima:")
for estado, accion in politica.items():
    print(f"Estado {estado}: {accion}")