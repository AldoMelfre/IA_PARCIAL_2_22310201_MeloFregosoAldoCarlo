# ============================================
# PROCESO DE DECISIÓN DE MARKOV (MDP)
# ============================================

# DESCRIPCIÓN TEÓRICA:
# Un Proceso de Decisión de Markov (MDP) es un modelo matemático para la toma de decisiones secuenciales.
# En un MDP, un agente toma decisiones en un entorno estocástico, donde cada acción puede llevar a diferentes
# estados con ciertas probabilidades y recompensas.
# 
# COMPONENTES:
# - **Estados:** Representan las posibles situaciones del entorno.
# - **Acciones:** Decisiones que el agente puede tomar en cada estado.
# - **Transiciones:** Probabilidades de moverse entre estados al realizar una acción.
# - **Recompensas:** Beneficio inmediato obtenido al realizar una acción en un estado.
# - **Factor de descuento (gamma):** Reduce el valor de las recompensas futuras.
# 
# EJEMPLO:
# Un robot se encuentra en una cuadrícula 3x3 y debe llegar a un objetivo en la esquina superior derecha.
# - Cada movimiento tiene un costo de -1 (energía gastada).
# - Si el robot llega al objetivo, obtiene una recompensa de +10.
# - El robot puede moverse hacia arriba, abajo, izquierda o derecha.
# - El algoritmo calcula la política óptima para que el robot alcance el objetivo con la mayor recompensa acumulada.

# ============================================
# FUNCIÓN PARA RESOLVER UN MDP CON ITERACIÓN DE VALORES
# ============================================
def resolver_mdp(estados, acciones, transiciones, recompensas, gamma, epsilon):
    """
    Resuelve un Proceso de Decisión de Markov (MDP) utilizando iteración de valores.
    :param estados: Lista de estados posibles.
    :param acciones: Lista de acciones posibles.
    :param transiciones: Diccionario con las probabilidades de transición entre estados.
    :param recompensas: Diccionario con las recompensas inmediatas para cada estado y acción.
    :param gamma: Factor de descuento (0 <= gamma <= 1).
    :param epsilon: Umbral de convergencia.
    :return: Diccionario con los valores óptimos de los estados y la política óptima.
    """
    # Inicializamos los valores de los estados en 0
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

    # Calculamos la política óptima
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

# Llamamos a la función para resolver el MDP
valores, politica = resolver_mdp(estados, acciones, transiciones, recompensas, gamma, epsilon)

# Mostramos los resultados
print("Valores óptimos de los estados:")
for estado, valor in valores.items():
    print(f"Estado {estado}: {valor:.2f}")

print("\nPolítica óptima:")
for estado, accion in politica.items():
    print(f"Estado {estado}: {accion}")