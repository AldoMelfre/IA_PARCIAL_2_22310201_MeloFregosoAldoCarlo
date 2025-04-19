# ============================================
# ALGORITMOS GENÉTICOS
# ============================================

# DESCRIPCIÓN TEÓRICA:
# Los algoritmos genéticos son técnicas de optimización inspiradas en los procesos de selección natural
# y evolución biológica. Utilizan conceptos como población, selección, cruza (recombinación) y mutación
# para encontrar soluciones aproximadas a problemas complejos.
# 
# CARACTERÍSTICAS:
# - Trabajan con una población de soluciones en lugar de una única solución.
# - Utilizan operadores genéticos (selección, cruza y mutación) para explorar el espacio de búsqueda.
# - Son útiles para problemas donde el espacio de búsqueda es grande y no se puede explorar exhaustivamente.
# 
# APLICACIÓN:
# Este algoritmo es útil en problemas como:
# - Optimización de rutas (por ejemplo, el problema del viajero).
# - Diseño de redes.
# - Problemas de planificación y asignación.
# - Ajuste de parámetros en modelos de aprendizaje automático.

import random

# ============================================
# FUNCIÓN DE FITNESS
# ============================================
def calcular_fitness(individuo, distancias):
    """
    Calcula el fitness de un individuo basado en la distancia total de su ruta.
    :param individuo: Lista que representa una ruta (permutación de ciudades).
    :param distancias: Diccionario con las distancias entre ciudades.
    :return: Fitness del individuo (inverso de la distancia total).
    """
    distancia_total = 0
    for i in range(len(individuo) - 1):
        distancia_total += distancias[individuo[i]][individuo[i + 1]]
    distancia_total += distancias[individuo[-1]][individuo[0]]  # Regreso a la ciudad inicial
    return 1 / distancia_total  # Fitness es el inverso de la distancia total

# ============================================
# OPERADOR DE SELECCIÓN
# ============================================
def seleccion_ruleta(poblacion, fitness):
    """
    Selecciona un individuo de la población usando selección por ruleta.
    :param poblacion: Lista de individuos.
    :param fitness: Lista de valores de fitness correspondientes a la población.
    :return: Individuo seleccionado.
    """
    suma_fitness = sum(fitness)
    seleccion = random.uniform(0, suma_fitness)
    acumulado = 0
    for i, individuo in enumerate(poblacion):
        acumulado += fitness[i]
        if acumulado >= seleccion:
            return individuo

# ============================================
# OPERADOR DE CRUZA
# ============================================
def cruza_ordenada(padre1, padre2):
    """
    Realiza una cruza ordenada entre dos padres para generar un hijo.
    :param padre1: Primer padre (lista de ciudades).
    :param padre2: Segundo padre (lista de ciudades).
    :return: Hijo generado por cruza.
    """
    inicio = random.randint(0, len(padre1) - 2)
    fin = random.randint(inicio + 1, len(padre1) - 1)
    hijo = [None] * len(padre1)
    hijo[inicio:fin] = padre1[inicio:fin]
    pos = fin
    for ciudad in padre2:
        if ciudad not in hijo:
            if pos >= len(hijo):
                pos = 0
            hijo[pos] = ciudad
            pos += 1
    return hijo

# ============================================
# OPERADOR DE MUTACIÓN
# ============================================
def mutacion(individuo, tasa_mutacion):
    """
    Realiza una mutación en un individuo con una probabilidad dada.
    :param individuo: Individuo a mutar.
    :param tasa_mutacion: Probabilidad de mutación.
    :return: Individuo mutado.
    """
    for i in range(len(individuo)):
        if random.random() < tasa_mutacion:
            j = random.randint(0, len(individuo) - 1)
            individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo

# ============================================
# ALGORITMO GENÉTICO
# ============================================
def algoritmo_genetico(ciudades, distancias, tamano_poblacion, generaciones, tasa_mutacion):
    """
    Implementación de un algoritmo genético para resolver el problema del viajero.
    :param ciudades: Lista de ciudades.
    :param distancias: Diccionario con las distancias entre ciudades.
    :param tamano_poblacion: Tamaño de la población inicial.
    :param generaciones: Número de generaciones.
    :param tasa_mutacion: Probabilidad de mutación.
    :return: Mejor individuo encontrado y su fitness.
    """
    # Generamos la población inicial
    poblacion = [random.sample(ciudades, len(ciudades)) for _ in range(tamano_poblacion)]

    for _ in range(generaciones):
        # Calculamos el fitness de cada individuo
        fitness = [calcular_fitness(individuo, distancias) for individuo in poblacion]

        # Creamos la nueva población
        nueva_poblacion = []
        for _ in range(tamano_poblacion // 2):
            # Selección
            padre1 = seleccion_ruleta(poblacion, fitness)
            padre2 = seleccion_ruleta(poblacion, fitness)

            # Cruza
            hijo1 = cruza_ordenada(padre1, padre2)
            hijo2 = cruza_ordenada(padre2, padre1)

            # Mutación
            hijo1 = mutacion(hijo1, tasa_mutacion)
            hijo2 = mutacion(hijo2, tasa_mutacion)

            nueva_poblacion.extend([hijo1, hijo2])

        poblacion = nueva_poblacion

    # Calculamos el fitness final y seleccionamos el mejor individuo
    fitness = [calcular_fitness(individuo, distancias) for individuo in poblacion]
    mejor_indice = fitness.index(max(fitness))
    return poblacion[mejor_indice], 1 / fitness[mejor_indice]

# ============================================
# EJEMPLO DE PROBLEMA DEL VIAJERO
# ============================================
# Definimos las ciudades y las distancias entre ellas
ciudades = ["Madrid", "París", "Berlín", "Roma", "Viena", "Atenas"]
distancias = {
    "Madrid": {"Madrid": 0, "París": 1275, "Berlín": 1860, "Roma": 1950, "Viena": 2315, "Atenas": 2850},
    "París": {"Madrid": 1275, "París": 0, "Berlín": 1050, "Roma": 1420, "Viena": 1235, "Atenas": 2100},
    "Berlín": {"Madrid": 1860, "París": 1050, "Berlín": 0, "Roma": 1180, "Viena": 680, "Atenas": 1800},
    "Roma": {"Madrid": 1950, "París": 1420, "Berlín": 1180, "Roma": 0, "Viena": 800, "Atenas": 1050},
    "Viena": {"Madrid": 2315, "París": 1235, "Berlín": 680, "Roma": 800, "Viena": 0, "Atenas": 1280},
    "Atenas": {"Madrid": 2850, "París": 2100, "Berlín": 1800, "Roma": 1050, "Viena": 1280, "Atenas": 0},
}

# Parámetros del algoritmo genético
tamano_poblacion = 10
generaciones = 100
tasa_mutacion = 0.1

# Ejecutamos el algoritmo genético
mejor_ruta, mejor_distancia = algoritmo_genetico(ciudades, distancias, tamano_poblacion, generaciones, tasa_mutacion)

# Mostramos el resultado
print(f"Mejor ruta encontrada: {mejor_ruta}")
print(f"Distancia total: {mejor_distancia}")