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
    # Por qué: Necesitamos una política inicial para comenzar el algoritmo.
    # Para qué: La política inicial será evaluada y mejorada iterativamente.
    politica = {estado: acciones[0] for estado in estados}

    while True:
        # ============================================
        # EVALUACIÓN DE LA POLÍTICA
        # ============================================
        # Inicializamos los valores de los estados en 0
        # Por qué: Los valores iniciales son desconocidos, por lo que los inicializamos en 0.
        # Para qué: Estos valores serán calculados iterativamente para reflejar la recompensa acumulada esperada.
        valores = {estado: 0 for estado in estados}

        while True:
            delta = 0  # Diferencia máxima entre valores consecutivos
            # Por qué: `delta` mide cuánto cambian los valores entre iteraciones.
            # Para qué: Nos ayuda a determinar si los valores han convergido.

            nuevos_valores = valores.copy()  # Copiamos los valores actuales
            # Por qué: Necesitamos una copia para calcular los nuevos valores sin modificar los actuales.
            # Para qué: Esto asegura que las actualizaciones no afecten los cálculos en curso.

            for estado in estados:
                accion = politica[estado]  # Acción según la política actual
                # Por qué: Evaluamos los valores de los estados basándonos en la acción definida por la política actual.
                # Para qué: Esto nos permite calcular el valor esperado de cada estado bajo la política actual.

                # Calculamos el valor esperado para la acción actual
                nuevos_valores[estado] = sum(
                    transiciones.get((estado, accion, siguiente_estado), 0) *
                    (recompensas.get((estado, accion, siguiente_estado), 0) + gamma * valores[siguiente_estado])
                    for siguiente_estado in estados
                )
                # Por qué: Usamos la ecuación de Bellman para calcular el valor esperado de un estado.
                # Para qué: Esto nos da el valor acumulado esperado de seguir la política actual desde este estado.

                delta = max(delta, abs(valores[estado] - nuevos_valores[estado]))  # Actualizamos delta
                # Por qué: Calculamos el cambio máximo entre los valores antiguos y nuevos.
                # Para qué: Esto nos ayuda a verificar si los valores han convergido.

            valores = nuevos_valores  # Actualizamos los valores
            # Por qué: Los nuevos valores ahora se convierten en los valores actuales para la próxima iteración.
            # Para qué: Continuamos iterando hasta que los valores converjan.

            # Verificamos si hemos alcanzado la convergencia
            if delta < epsilon:
                # Por qué: Si el cambio máximo (`delta`) es menor que el umbral (`epsilon`), los valores han convergido.
                # Para qué: Detenemos la evaluación de la política porque los valores son suficientemente precisos.
                break

        # ============================================
        # MEJORA DE LA POLÍTICA
        # ============================================
        politica_estable = True  # Asumimos que la política es estable
        # Por qué: Inicialmente asumimos que la política no cambiará.
        # Para qué: Si encontramos una mejor acción para algún estado, actualizaremos esta variable.

        for estado in estados:
            mejor_accion = None
            mejor_valor = float('-inf')
            # Por qué: Inicializamos la mejor acción y el mejor valor para encontrar la mejor acción en este estado.
            # Para qué: Esto nos permite comparar las acciones y seleccionar la mejor.

            for accion in acciones:
                # Calculamos el valor esperado para cada acción
                valor_accion = sum(
                    transiciones.get((estado, accion, siguiente_estado), 0) *
                    (recompensas.get((estado, accion, siguiente_estado), 0) + gamma * valores[siguiente_estado])
                    for siguiente_estado in estados
                )
                # Por qué: Evaluamos todas las acciones posibles en el estado actual.
                # Para qué: Esto nos permite encontrar la acción que maximiza el valor esperado.

                if valor_accion > mejor_valor:
                    mejor_valor = valor_accion
                    mejor_accion = accion
                    # Por qué: Actualizamos la mejor acción si encontramos un valor mayor.
                    # Para qué: Esto asegura que seleccionemos la acción óptima para este estado.

            # Si la mejor acción no coincide con la acción actual de la política, actualizamos la política
            if mejor_accion != politica[estado]:
                politica[estado] = mejor_accion
                politica_estable = False
                # Por qué: Si encontramos una mejor acción, actualizamos la política.
                # Para qué: Esto asegura que la política mejore en cada iteración.

        # Si la política no cambió, hemos convergido
        if politica_estable:
            # Por qué: Si la política no cambia en una iteración, significa que hemos encontrado la política óptima.
            # Para qué: Detenemos el algoritmo porque ya no hay mejoras posibles.
            break

    return valores, politica
    # Por qué: Devolvemos los valores óptimos y la política óptima.
    # Para qué: Estos resultados pueden ser utilizados para tomar decisiones óptimas en el entorno.

# ============================================
# EJEMPLO: ROBOT EN UNA CUADRÍCULA
# ============================================
# Definimos los estados (posiciones en la cuadrícula)
estados = [(x, y) for x in range(3) for y in range(3)]
# Por qué: Representamos las posiciones posibles del robot en una cuadrícula 3x3.
# Para qué: Estos son los estados que el algoritmo evaluará.

# Definimos las acciones
acciones = ["Arriba", "Abajo", "Izquierda", "Derecha"]
# Por qué: Estas son las acciones que el robot puede tomar en cada estado.
# Para qué: El algoritmo evaluará estas acciones para encontrar la mejor en cada estado.

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
# Por qué: Estas son las probabilidades de transición entre estados al realizar una acción.
# Para qué: El algoritmo utiliza estas probabilidades para calcular los valores esperados.

# Definimos las recompensas inmediatas
recompensas = {
    ((0, 2), "Derecha", (0, 2)): 10,  # Recompensa por alcanzar el objetivo
    **{(estado, accion, siguiente_estado): -1 for estado in estados for accion in acciones for siguiente_estado in estados}
}
# Por qué: Estas son las recompensas inmediatas asociadas a cada transición.
# Para qué: El algoritmo utiliza estas recompensas para calcular los valores de los estados.

# Factor de descuento
gamma = 0.9
# Por qué: El factor de descuento reduce la importancia de las recompensas futuras.
# Para qué: Esto asegura que el algoritmo priorice las recompensas inmediatas.

# Umbral de convergencia
epsilon = 0.01
# Por qué: Este es el margen de error permitido para determinar la convergencia.
# Para qué: Controla la precisión de los valores calculados.

# Llamamos a la función de búsqueda de la política
valores, politica = busqueda_de_la_politica(estados, acciones, transiciones, recompensas, gamma, epsilon)
# Por qué: Ejecutamos el algoritmo para encontrar los valores y la política óptima.
# Para qué: Esto nos permite tomar decisiones óptimas en el entorno.

# Mostramos los resultados
print("Valores óptimos de los estados:")
for estado, valor in valores.items():
    print(f"Estado {estado}: {valor:.2f}")
# Por qué: Mostramos los valores óptimos de cada estado.
# Para qué: Esto nos permite entender la recompensa acumulada esperada desde cada estado.

print("\nPolítica óptima:")
for estado, accion in politica.items():
    print(f"Estado {estado}: {accion}")
# Por qué: Mostramos la política óptima para cada estado.
# Para qué: Esto nos indica la mejor acción a tomar en cada estado.