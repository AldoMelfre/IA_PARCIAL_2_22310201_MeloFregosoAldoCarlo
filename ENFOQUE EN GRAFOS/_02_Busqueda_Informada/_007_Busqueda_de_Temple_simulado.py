# ============================================
# BÚSQUEDA DE TEMPLE SIMULADO
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La búsqueda de temple simulado es un algoritmo de optimización inspirado en el proceso físico
# de enfriamiento de metales. Durante este proceso, un material se calienta a una temperatura alta
# y luego se enfría lentamente para alcanzar un estado de mínima energía.
# 
# CARACTERÍSTICAS:
# - Permite aceptar soluciones peores con una probabilidad que disminuye a medida que la temperatura baja.
# - Es útil para escapar de máximos locales y encontrar soluciones cercanas al óptimo global.
# - La probabilidad de aceptar una solución peor está determinada por la función:
#   P = exp(-ΔE / T)
#   Donde:
#   - ΔE es la diferencia entre la calidad de la solución actual y la nueva.
#   - T es la temperatura actual.
# 
# APLICACIÓN:
# Este algoritmo es útil en problemas como:
# - Optimización de rutas (por ejemplo, el problema del viajero).
# - Diseño de redes.
# - Problemas de planificación y asignación.

import math
import random

# ============================================
# CLASE NODO
# ============================================
class NodoTemple:
    """
    Clase que representa un nodo en el grafo.
    """
    def __init__(self, estado, heuristica=0):
        self.estado = estado  # Estado del nodo (nombre o identificador)
        self.heuristica = heuristica  # Valor heurístico del nodo
        self.vecinos = []  # Lista de nodos vecinos

    def agregar_vecino(self, vecino):
        """
        Agrega un vecino al nodo.
        :param vecino: Nodo vecino.
        """
        self.vecinos.append(vecino)

# ============================================
# FUNCIÓN PARA EJECUTAR LA BÚSQUEDA DE TEMPLE SIMULADO
# ============================================
def busqueda_temple_simulado(nodo_inicial, temperatura_inicial, enfriamiento, iteraciones_max):
    """
    Implementación de la búsqueda de temple simulado.
    :param nodo_inicial: Nodo inicial desde donde comienza la búsqueda.
    :param temperatura_inicial: Temperatura inicial del sistema.
    :param enfriamiento: Factor de enfriamiento (entre 0 y 1).
    :param iteraciones_max: Número máximo de iteraciones.
    :return: Mejor nodo encontrado y el camino recorrido.
    """
    nodo_actual = nodo_inicial
    mejor_nodo = nodo_actual
    temperatura = temperatura_inicial
    camino = [nodo_actual.estado]  # Lista para almacenar el camino recorrido

    for _ in range(iteraciones_max):
        # Si la temperatura es muy baja, terminamos la búsqueda
        if temperatura <= 0:
            break

        # Seleccionamos un vecino aleatorio
        if nodo_actual.vecinos:
            vecino = random.choice(nodo_actual.vecinos)
        else:
            break

        # Calculamos la diferencia de heurística (ΔE)
        delta_e = vecino.heuristica - nodo_actual.heuristica

        # Si el vecino es mejor, nos movemos a él
        if delta_e < 0 or random.random() < math.exp(-delta_e / temperatura):
            nodo_actual = vecino
            camino.append(nodo_actual.estado)

            # Actualizamos el mejor nodo encontrado
            if nodo_actual.heuristica < mejor_nodo.heuristica:
                mejor_nodo = nodo_actual

        # Reducimos la temperatura
        temperatura *= enfriamiento

    return mejor_nodo, camino

# ============================================
# EJEMPLO DE GRAFO CON CIUDADES EUROPEAS
# ============================================
# Creamos los nodos del grafo
nodo_madrid = NodoTemple("Madrid", heuristica=10)
nodo_paris = NodoTemple("París", heuristica=8)
nodo_berlin = NodoTemple("Berlín", heuristica=6)
nodo_roma = NodoTemple("Roma", heuristica=4)
nodo_viena = NodoTemple("Viena", heuristica=3)
nodo_atenas = NodoTemple("Atenas", heuristica=0)  # Nodo objetivo con heurística 0

# Definimos las conexiones entre los nodos
nodo_madrid.agregar_vecino(nodo_paris)
nodo_madrid.agregar_vecino(nodo_berlin)
nodo_paris.agregar_vecino(nodo_roma)
nodo_berlin.agregar_vecino(nodo_viena)
nodo_roma.agregar_vecino(nodo_atenas)
nodo_viena.agregar_vecino(nodo_atenas)

# ============================================
# EJECUCIÓN DE LA BÚSQUEDA DE TEMPLE SIMULADO
# ============================================
# Parámetros de la búsqueda
temperatura_inicial = 100  # Temperatura inicial
enfriamiento = 0.9  # Factor de enfriamiento
iteraciones_max = 100  # Número máximo de iteraciones

# Ejecutamos la búsqueda desde el nodo inicial (Madrid)
mejor_nodo, camino_recorrido = busqueda_temple_simulado(nodo_madrid, temperatura_inicial, enfriamiento, iteraciones_max)

# Mostramos el resultado
print(f"Mejor nodo encontrado: {mejor_nodo.estado} con heurística {mejor_nodo.heuristica}")
print(f"Camino recorrido: {camino_recorrido}")