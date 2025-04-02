#La búsqueda en profundidad limitada (Depth-Limited Search, DLS) es una variante de la búsqueda en profundidad (DFS) que establece un límite en la profundidad máxima que se puede explorar. Esto es útil para evitar ciclos infinitos en grafos con ciclos o para limitar la exploración en grafos muy grandes.

def dls(graph, start, goal, limit, path=None, depth=0):
    """
    Búsqueda en Profundidad Limitada (DLS) para encontrar un nodo objetivo.
    :param graph: Diccionario que representa el grafo (nodo: [vecinos]).
    :param start: Nodo inicial.
    :param goal: Nodo objetivo.
    :param limit: Profundidad máxima permitida.
    :param path: Camino actual (se actualiza recursivamente).
    :param depth: Profundidad actual de la búsqueda.
    :return: Lista con el camino al nodo objetivo o None si no se encuentra.
    """
    if path is None:
        path = [start]  # Inicializamos el camino con el nodo de inicio

    if start == goal:  # Si encontramos el nodo objetivo, devolvemos el camino
        return path

    if depth >= limit:  # Si alcanzamos el límite de profundidad, detenemos la búsqueda
        return None

    # Recorremos los vecinos del nodo actual
    for neighbor in graph.get(start, []):
        result = dls(graph, neighbor, goal, limit, path + [neighbor], depth + 1)
        if result:  # Si encontramos el objetivo, devolvemos el camino
            return result

    return None  # Si no encontramos el objetivo, devolvemos None


# Definimos un grafo simple
grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": ["H"],
    "F": [],
    "G": [],
    "H": ["I"],
    "I": []
}

# Parámetros de búsqueda
nodo_inicial = "A"
nodo_objetivo = "H"
limite_profundidad = 3  # Límite de profundidad para la búsqueda en profundidad limitada

# Ejecutamos la búsqueda en profundidad limitada
camino = dls(grafo, nodo_inicial, nodo_objetivo, limite_profundidad)

# Mostramos el resultado
if camino:
    print(f"Camino encontrado: {camino}") #['A', 'B', 'E', 'H'] PORQUE EL NODO E ES EL UNICO QUE CONECTA A H
else:
    print(f"No se encontró el nodo '{nodo_objetivo}' dentro del límite de profundidad {limite_profundidad}.")

# En este ejemplo, la búsqueda en profundidad limitada busca el nodo "H" comenzando desde "A" y con un límite de profundidad de 3.

# Si el nodo objetivo no se encuentra dentro de la profundidad especificada, la función devuelve None.
#Ejemplo
# Parámetros de búsqueda para el nodo "I"
nodo_objetivo_2 = "I"
camino_2 = dls(grafo, nodo_inicial, nodo_objetivo_2, limite_profundidad)

# Mostramos el resultado para el nodo "I"
if camino_2:
    print(f"Camino encontrado para el nodo '{nodo_objetivo_2}': {camino_2}")
else:
    print(f"No se encontró el nodo '{nodo_objetivo_2}' dentro del límite de profundidad {limite_profundidad}.") #No se encontró el nodo 'I' dentro del límite de profundidad 3.