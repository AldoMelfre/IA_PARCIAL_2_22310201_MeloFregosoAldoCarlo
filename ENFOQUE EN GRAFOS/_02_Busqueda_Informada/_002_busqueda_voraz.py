import heapq  # Para manejar la cola de prioridad

class Nodo:
    """
    Clase que representa un nodo en el grafo.
    """
    def __init__(self, estado, heuristica=0, padre=None):
        self.estado = estado  # Estado del nodo (nombre o identificador)
        self.heuristica = heuristica  # Valor heurístico del nodo
        self.padre = padre  # Nodo padre (para reconstruir el camino)
    
    def __lt__(self, otro):
        # Comparación basada en el valor heurístico (para la cola de prioridad)
        return self.heuristica < otro.heuristica


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


def busqueda_voraz(grafo, heuristica, inicio, objetivo):
    """
    Implementación de la búsqueda voraz.
    :param grafo: Diccionario que representa el grafo (nodo: [vecinos]).
    :param heuristica: Diccionario con valores heurísticos para cada nodo.
    :param inicio: Nodo inicial.
    :param objetivo: Nodo objetivo.
    :return: Lista con el camino desde inicio hasta objetivo, o None si no se encuentra.
    """
    # Crear el nodo raíz
    nodo_raiz = Nodo(estado=inicio, heuristica=heuristica[inicio])

    # Inicializamos la frontera como una cola de prioridad
    frontera = []
    heapq.heappush(frontera, nodo_raiz)

    # Conjunto de nodos explorados
    explorados = set()

    while frontera:
        # Extraemos el nodo con el menor valor heurístico
        nodo_actual = heapq.heappop(frontera)

        # Si el nodo actual es el objetivo, reconstruimos el camino
        if nodo_actual.estado == objetivo:
            return reconstruir_camino(nodo_actual)

        # Marcamos el nodo actual como explorado
        explorados.add(nodo_actual.estado)

        # Expandimos el nodo actual generando sus hijos
        for vecino in grafo.get(nodo_actual.estado, []):
            if vecino not in explorados:
                # Crear un nodo hijo
                nodo_hijo = Nodo(estado=vecino, heuristica=heuristica[vecino], padre=nodo_actual)

                # Si el vecino no está en la frontera, lo agregamos
                if not any(nodo.estado == vecino for nodo in frontera):
                    heapq.heappush(frontera, nodo_hijo)

    # Si no se encuentra un camino, devolvemos None
    return None


# Definimos un grafo con pueblos mágicos de México
grafo_pueblos_magicos = {
    "Tequila": ["Mazamitla", "San Sebastián del Oeste"],
    "Mazamitla": ["Tapalpa"],
    "San Sebastián del Oeste": ["Mascota"],
    "Tapalpa": ["Ajijic"],
    "Mascota": ["Talpa de Allende"],
    "Ajijic": [],
    "Talpa de Allende": ["Lagos de Moreno"],
    "Lagos de Moreno": []
}

# Definimos una heurística (distancia estimada en línea recta al objetivo)
heuristica = {
    "Tequila": 7,
    "Mazamitla": 6,
    "San Sebastián del Oeste": 5,
    "Tapalpa": 4,
    "Mascota": 3,
    "Ajijic": 2,
    "Talpa de Allende": 1,
    "Lagos de Moreno": 0  # El objetivo tiene heurística 0
}

# Parámetros de búsqueda
nodo_inicial = "Tequila"
nodo_objetivo = "Lagos de Moreno"

# Ejecutamos la búsqueda voraz
camino = busqueda_voraz(grafo_pueblos_magicos, heuristica, nodo_inicial, nodo_objetivo)

# Mostramos el resultado
if camino:
    print(f"Camino encontrado (de {nodo_inicial} a {nodo_objetivo}): {camino}")
else:
    print(f"No se encontró un camino entre '{nodo_inicial}' y '{nodo_objetivo}'.")