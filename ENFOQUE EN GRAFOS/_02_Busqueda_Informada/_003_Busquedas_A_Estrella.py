# ============================================
# BÚSQUEDA A* (A ESTRELLA)
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La búsqueda A* es un algoritmo de búsqueda informada que encuentra el camino más corto entre un nodo inicial y un nodo objetivo.
# Combina dos factores para decidir qué nodo explorar:
# 1. g(n): El costo acumulado desde el nodo inicial hasta el nodo actual.
# 2. h(n): Una estimación heurística del costo desde el nodo actual hasta el objetivo.
# La función utilizada es:
# f(n) = g(n) + h(n)
# Donde:
# - f(n): Es el costo total estimado para llegar al objetivo pasando por el nodo n.
# - g(n): Es el costo real acumulado desde el nodo inicial hasta el nodo actual.
# - h(n): Es la heurística que estima el costo restante desde el nodo actual hasta el objetivo.

# CARACTERÍSTICAS:
# - A* garantiza encontrar el camino más corto si la heurística es admisible (no sobreestima el costo real) y consistente (cumple la desigualdad triangular).
# - Utiliza una cola de prioridad para explorar los nodos con el menor valor f(n) primero.

# APLICACIÓN:
# Este algoritmo es útil en problemas como:
# - Búsqueda de rutas en mapas.
# - Resolución de problemas de planificación.
# - Juegos y sistemas de inteligencia artificial.

import heapq  # Para manejar la cola de prioridad

# ============================================
# CLASE NODO
# ============================================
class Nodo:
    """
    Clase que representa un nodo en el grafo.
    """
    def __init__(self, estado, g=0, h=0, padre=None):
        self.estado = estado  # Estado del nodo (nombre o identificador)
        self.g = g  # Costo acumulado desde el nodo inicial (g(n))
        self.h = h  # Valor heurístico del nodo (h(n))
        self.f = g + h  # Costo total estimado (f(n) = g(n) + h(n))
        self.padre = padre  # Nodo padre (para reconstruir el camino)
    
    def __lt__(self, otro):
        # Comparación basada en el valor total f(n) (para la cola de prioridad)
        return self.f < otro.f


# ============================================
# FUNCIÓN PARA RECONSTRUIR EL CAMINO
# ============================================
def reconstruir_camino(nodo):
    """
    Reconstruye el camino desde el nodo inicial hasta el nodo objetivo.
    :param nodo: Nodo objetivo.
    :return: Lista con el camino desde el nodo inicial hasta el nodo objetivo.
    """
    camino = []
    while nodo:
        camino.append(nodo.estado)
        nodo = nodo.padre
    return camino[::-1]  # Invertimos el camino para mostrarlo desde el inicio


# ============================================
# IMPLEMENTACIÓN DE LA BÚSQUEDA A*
# ============================================
def busqueda_a_estrella(grafo, heuristica, inicio, objetivo):
    """
    Implementación de la búsqueda A*.
    :param grafo: Diccionario que representa el grafo (nodo: {vecino: costo}).
    :param heuristica: Diccionario con valores heurísticos para cada nodo.
    :param inicio: Nodo inicial.
    :param objetivo: Nodo objetivo.
    :return: Lista con el camino desde inicio hasta objetivo, o None si no se encuentra.
    """
    # Crear el nodo inicial
    nodo_inicial = Nodo(estado=inicio, g=0, h=heuristica[inicio])

    # Inicializamos la frontera como una cola de prioridad
    frontera = []
    heapq.heappush(frontera, nodo_inicial)

    # Conjunto de nodos explorados
    explorados = set()

    while frontera:
        # Extraemos el nodo con el menor valor f(n)
        nodo_actual = heapq.heappop(frontera)

        # Si el nodo actual es el objetivo, reconstruimos el camino
        if nodo_actual.estado == objetivo:
            return reconstruir_camino(nodo_actual)

        # Marcamos el nodo actual como explorado
        explorados.add(nodo_actual.estado)

        # Expandimos el nodo actual generando sus hijos
        for vecino, costo in grafo.get(nodo_actual.estado, {}).items():
            if vecino not in explorados:
                # Calcular g(n), h(n) y f(n) para el vecino
                g = nodo_actual.g + costo
                h = heuristica[vecino]
                nodo_hijo = Nodo(estado=vecino, g=g, h=h, padre=nodo_actual)

                # Si el vecino no está en la frontera, lo agregamos
                if not any(nodo.estado == vecino for nodo in frontera):
                    heapq.heappush(frontera, nodo_hijo)

    # Si no se encuentra un camino, devolvemos None
    return None


# ============================================
# GRAFO DE CIUDADES EUROPEAS
# ============================================
# Representa un grafo donde las claves son ciudades y los valores son diccionarios
# que indican las ciudades vecinas y el costo (distancia en kilómetros) para llegar a ellas.
grafo_ciudades = {
    "Madrid": {"París": 1275, "Lisboa": 635},
    "París": {"Berlín": 1050, "Roma": 1420},
    "Lisboa": {"Madrid": 635, "París": 1450},
    "Berlín": {"Varsovia": 570, "Praga": 350},
    "Roma": {"Atenas": 1300},
    "Varsovia": {"Moscú": 1150},
    "Praga": {"Viena": 330},
    "Atenas": {},
    "Moscú": {},
    "Viena": {}
}

# ============================================
# HEURÍSTICA
# ============================================
# Representa una estimación de la distancia en línea recta desde cada ciudad al objetivo.
heuristica = {
    "Madrid": 1500,
    "París": 1200,
    "Lisboa": 1600,
    "Berlín": 800,
    "Roma": 1000,
    "Varsovia": 600,
    "Praga": 700,
    "Atenas": 0,  # El objetivo tiene heurística 0
    "Moscú": 0,
    "Viena": 400
}

# ============================================
# EJECUCIÓN DE LA BÚSQUEDA A*
# ============================================
# Parámetros de búsqueda
nodo_inicial = "Madrid"
nodo_objetivo = "Atenas"

# Ejecutamos la búsqueda A*
camino_a_estrella = busqueda_a_estrella(grafo_ciudades, heuristica, nodo_inicial, nodo_objetivo)

# Mostramos el resultado
if camino_a_estrella:
    print(f"Camino encontrado con A* (de {nodo_inicial} a {nodo_objetivo}): {camino_a_estrella}")
else:
    print(f"No se encontró un camino entre '{nodo_inicial}' y '{nodo_objetivo}'.")
