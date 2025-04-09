# ¿Qué es Greedy Best-First Search?
# Es un algoritmo de búsqueda informada que utiliza una heurística para decidir qué nodo explorar a continuación.
# Siempre selecciona el nodo con el menor valor heurístico, es decir, el que parece estar más cerca del objetivo.

# Funcionamiento:
# - Utiliza una cola de prioridad para almacenar los nodos pendientes de explorar.
# - La cola de prioridad ordena los nodos según su valor heurístico, de modo que el nodo con el menor valor se procesa primero.
# - A medida que se expanden los nodos, se agregan sus vecinos a la cola de prioridad.

# Heurística:
# - La heurística es una función que estima qué tan cerca está un nodo del objetivo.
# - En este ejemplo, la heurística es un diccionario que asigna un valor a cada nodo, representando una distancia estimada al objetivo.

# Ventajas:
# - Es más rápido que los algoritmos no informados (como BFS o DFS) porque utiliza la heurística para guiar la búsqueda.
# - Es fácil de implementar y entender.

# Limitaciones:
# - No garantiza encontrar el camino más corto, ya que solo considera la heurística y no el costo acumulado.
# - Depende de la calidad de la heurística. Si la heurística no es precisa, el algoritmo puede explorar nodos innecesarios.

import heapq  # Para manejar la cola de prioridad

class Nodo:
    """
    Clase que representa un nodo en el grafo.
    """
    def __init__(self, nombre, coste=0, heuristica=0):
        self.nombre = nombre  # Nombre del nodo
        self.coste = coste  # Costo acumulado desde el inicio (g(n))
        self.heuristica = heuristica  # Valor heurístico (h(n))
        self.valor = coste + heuristica  # Valor total (f(n) = g(n) + h(n))
        self.hijos = []  # Lista de hijos del nodo

    def __lt__(self, otro):
        # Comparación basada en el valor total (para la cola de prioridad)
        return self.valor < otro.valor

    def agregar_hijo(self, hijo):
        """
        Agrega un hijo al nodo.
        """
        self.hijos.append(hijo)

    def hijo_menor(self, n=1):
        """
        Devuelve el hijo con el n-ésimo menor valor, sin sacarlo de la lista.
        """
        if len(self.hijos) < n:
            return None
        return sorted(self.hijos, key=lambda x: x.valor)[n - 1]


def busqueda_greedy_clase(grafo, heuristica, inicio, objetivo):
    """
    Búsqueda Greedy Best-First utilizando la clase Nodo.
    :param grafo: Diccionario que representa el grafo (nodo: [vecinos]).
    :param heuristica: Diccionario con valores heurísticos para cada nodo.
    :param inicio: Nodo inicial.
    :param objetivo: Nodo objetivo.
    :return: Lista con el camino desde inicio hasta objetivo, o None si no se encuentra.
    """
    # Crear el nodo inicial
    nodo_inicial = Nodo(inicio, coste=0, heuristica=heuristica[inicio])

    # Cola de prioridad para almacenar los nodos según su valor heurístico
    cola_prioridad = []
    heapq.heappush(cola_prioridad, nodo_inicial)

    # Conjunto de nodos visitados para evitar ciclos
    visitados = set()

    while cola_prioridad:
        # Extraemos el nodo con el menor valor heurístico
        nodo_actual = heapq.heappop(cola_prioridad)

        # Si el nodo actual ya fue visitado, lo ignoramos
        if nodo_actual.nombre in visitados:
            continue

        # Marcamos el nodo actual como visitado
        visitados.add(nodo_actual.nombre)

        # Si llegamos al nodo objetivo, devolvemos el camino
        if nodo_actual.nombre == objetivo:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual.nombre)
                nodo_actual = nodo_actual.padre if hasattr(nodo_actual, "padre") else None
            return camino[::-1]  # Invertimos el camino para mostrarlo desde el inicio

        # Recorremos los vecinos del nodo actual
        for vecino in grafo.get(nodo_actual.nombre, []):
            if vecino not in visitados:
                # Crear un nodo hijo
                nodo_hijo = Nodo(vecino, coste=nodo_actual.coste + 1, heuristica=heuristica[vecino])
                nodo_hijo.padre = nodo_actual  # Guardamos una referencia al nodo padre
                nodo_actual.agregar_hijo(nodo_hijo)  # Agregamos el hijo al nodo actual
                heapq.heappush(cola_prioridad, nodo_hijo)

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

# Ejecutamos la búsqueda Greedy Best-First
camino = busqueda_greedy_clase(grafo_pueblos_magicos, heuristica, nodo_inicial, nodo_objetivo)

# Mostramos el resultado
if camino:
    print(f"Camino encontrado (de {nodo_inicial} a {nodo_objetivo}): {camino}")
else:
    print(f"No se encontró un camino entre '{nodo_inicial}' y '{nodo_objetivo}'.")