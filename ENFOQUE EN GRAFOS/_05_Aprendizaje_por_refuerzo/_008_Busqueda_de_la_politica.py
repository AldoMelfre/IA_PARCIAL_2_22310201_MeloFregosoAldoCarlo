# ============================================
# BÚSQUEDA DE LA POLÍTICA: ROBOT EN UNA CUADRÍCULA
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La búsqueda de la política es un algoritmo utilizado para resolver problemas de toma de decisiones secuenciales,
# como los Procesos de Decisión de Markov (MDP). Este enfoque alterna entre:
# 1. **Evaluación de la Política:** Calcula los valores de los estados para una política fija.
# 2. **Mejora de la Política:** Actualiza la política seleccionando la mejor acción en cada estado.
# 
# El algoritmo repite estos pasos hasta que la política converge (es decir, ya no cambia).

# ============================================
# FUNCIÓN PARA LA BÚSQUEDA DE LA POLÍTICA
# ============================================
def busqueda_de_la_politica(estados, acciones, transiciones, recompensas, gamma, epsilon):
    """
    Implementa el algoritmo de búsqueda de la política.
    :param estados: Lista de estados posibles.
    :param acciones: Lista de acciones posibles.
    :param transiciones: Diccionario con las probabilidades de transición entre estados.
    :param recompensas: Diccionario con las recompensas inmediatas para cada estado y acción.
    :param gamma: Factor de descuento (0 <= gamma <= 1).
    :param epsilon: Umbral de convergencia para la evaluación de la política.
    :return: Diccionario con los valores óptimos de cada estado y la política óptima.
    """
    # Inicializamos una política aleatoria (por ejemplo, siempre elegir la primera acción)
    politica = {estado: acciones[0] for estado in estados}

    while True:
        # ============================================
        # EVALUACIÓN DE LA POLÍTICA
        # ============================================
        valores = {estado: 0 for estado in estados}  # Inicializamos los valores de los estados en 0

        while True:
            delta = 0  # Diferencia máxima entre valores consecutivos
            nuevos_valores = valores.copy()  # Copiamos los valores actuales

            for estado in estados:
                accion = politica[estado]  # Acción según la política actual
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

        # ============================================
        # MEJORA DE LA POLÍTICA
        # ============================================
        politica_estable = True  # Asumimos que la política es estable

        for estado in estados:
            mejor_accion = None
            mejor_valor = float('-inf')

            for accion in acciones:
                # Calculamos el valor esperado para cada acción
                valor_accion = sum(
                    transiciones.get((estado, accion, siguiente_estado), 0) *
                    (recompensas.get((estado, accion, siguiente_estado), 0) + gamma * valores[siguiente_estado])
                    for siguiente_estado in estados
                )
                if valor_accion > mejor_valor:
                    mejor_valor = valor_accion
                    mejor_accion = accion

            # Si la mejor acción no coincide con la acción actual de la política, actualizamos la política
            if mejor_accion != politica[estado]:
                politica[estado] = mejor_accion
                politica_estable = False

        # Si la política no cambió, hemos convergido
        if politica_estable:
            break

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

# Llamamos a la función de búsqueda de la política
valores, politica = busqueda_de_la_politica(estados, acciones, transiciones, recompensas, gamma, epsilon)

# Mostramos los resultados
print("Valores óptimos de los estados:")
for estado, valor in valores.items():
    print(f"Estado {estado}: {valor:.2f}")

print("\nPolítica óptima:")
for estado, accion in politica.items():
    print(f"Estado {estado}: {accion}")