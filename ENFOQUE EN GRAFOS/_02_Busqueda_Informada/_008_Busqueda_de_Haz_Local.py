# ============================================
# BÚSQUEDA DE HAZ LOCAL
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La búsqueda de haz local es un algoritmo de búsqueda informada que explora múltiples caminos
# simultáneamente. En cada iteración, selecciona los mejores caminos (según una heurística) y descarta
# los demás, enfocándose en las soluciones más prometedoras.
# 
# CARACTERÍSTICAS:
# - Explora múltiples estados simultáneamente, lo que reduce la probabilidad de quedar atrapado en un máximo local.
# - Utiliza una heurística para evaluar los estados y seleccionar los mejores.
# - No garantiza encontrar la solución óptima, pero puede ser más eficiente que otros métodos.
# 
# APLICACIÓN:
# Este algoritmo es útil en problemas como:
# - Optimización de rutas.
# - Resolución de problemas de planificación.
# - Búsqueda en espacios grandes y complejos.

import random

# ============================================
# CLASE NODO
# ============================================
class NodoHaz:
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
# FUNCIÓN PARA EJECUTAR LA BÚSQUEDA DE HAZ LOCAL
# ============================================
def busqueda_haz_local(nodos_iniciales, k):
    """
    Implementación de la búsqueda de haz local.
    :param nodos_iniciales: Lista de nodos iniciales desde donde comienza la búsqueda.
    :param k: Número de caminos (haz) a mantener en cada iteración.
    :return: Mejor nodo encontrado y el camino recorrido.
    """
    haz = nodos_iniciales  # Inicializamos el haz con los nodos iniciales
    caminos = [[nodo.estado] for nodo in haz]  # Lista para almacenar los caminos recorridos

    while True:
        # Generamos todos los vecinos de los nodos en el haz
        nuevos_nodos = []
        nuevos_caminos = []
        for i, nodo in enumerate(haz):
            for vecino in nodo.vecinos:
                nuevos_nodos.append(vecino)
                nuevos_caminos.append(caminos[i] + [vecino.estado])

        # Si no hay nuevos nodos, terminamos la búsqueda
        if not nuevos_nodos:
            break

        # Seleccionamos los k mejores nodos según su heurística
        mejores_indices = sorted(range(len(nuevos_nodos)), key=lambda i: nuevos_nodos[i].heuristica)[:k]
        haz = [nuevos_nodos[i] for i in mejores_indices]
        caminos = [nuevos_caminos[i] for i in mejores_indices]

        # Si encontramos un nodo con heurística 0, terminamos la búsqueda
        for nodo in haz:
            if nodo.heuristica == 0:
                return nodo, caminos[haz.index(nodo)]

    # Devolvemos el mejor nodo encontrado y su camino
    mejor_nodo = min(haz, key=lambda nodo: nodo.heuristica)
    return mejor_nodo, caminos[haz.index(mejor_nodo)]

# ============================================
# EJEMPLO DE GRAFO CON CIUDADES EUROPEAS
# ============================================
# Creamos los nodos del grafo
nodo_madrid = NodoHaz("Madrid", heuristica=10)
nodo_paris = NodoHaz("París", heuristica=8)
nodo_berlin = NodoHaz("Berlín", heuristica=6)
nodo_roma = NodoHaz("Roma", heuristica=4)
nodo_viena = NodoHaz("Viena", heuristica=3)
nodo_atenas = NodoHaz("Atenas", heuristica=0)  # Nodo objetivo con heurística 0

# Definimos las conexiones entre los nodos
nodo_madrid.agregar_vecino(nodo_paris)
nodo_madrid.agregar_vecino(nodo_berlin)
nodo_paris.agregar_vecino(nodo_roma)
nodo_berlin.agregar_vecino(nodo_viena)
nodo_roma.agregar_vecino(nodo_atenas)
nodo_viena.agregar_vecino(nodo_atenas)

# ============================================
# EJECUCIÓN DE LA BÚSQUEDA DE HAZ LOCAL
# ============================================
# Parámetros de la búsqueda
nodos_iniciales = [nodo_madrid, nodo_paris]  # Nodos iniciales
k = 2  # Número de caminos (haz) a mantener

# Ejecutamos la búsqueda
mejor_nodo, camino_recorrido = busqueda_haz_local(nodos_iniciales, k)

# Mostramos el resultado
print(f"Mejor nodo encontrado: {mejor_nodo.estado} con heurística {mejor_nodo.heuristica}")
print(f"Camino recorrido: {camino_recorrido}")