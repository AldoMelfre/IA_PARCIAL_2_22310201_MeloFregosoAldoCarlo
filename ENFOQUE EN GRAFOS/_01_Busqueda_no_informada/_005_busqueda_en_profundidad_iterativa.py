#La búsqueda en profundidad iterativa (IDDFS - Iterative Deepening Depth-First Search) es un algoritmo de búsqueda que combina las ventajas de la búsqueda en profundidad (DFS) y la búsqueda en anchura (BFS). Es particularmente útil cuando no se conoce la profundidad del nodo objetivo en un grafo o árbol.

def dls(graph, start, goal, limit, path=None, depth=0):
    """
    Búsqueda en Profundidad Limitada (DLS) para un límite específico.
    """
    if path is None:
        path = [start]

    if start == goal:  # Si encontramos el objetivo, devolvemos el camino
        return path

    if depth >= limit:  # Si alcanzamos el límite, detenemos la búsqueda
        return None

    for neighbor in graph.get(start, []):  # Recorremos los vecinos
        result = dls(graph, neighbor, goal, limit, path + [neighbor], depth + 1)
        if result:
            return result

    return None


def iddfs(graph, start, goal):
    """
    Búsqueda en Profundidad Iterativa (IDDFS) sin límite explícito.
    :param graph: Diccionario que representa el grafo (nodo: [vecinos]).
    :param start: Nodo inicial.
    :param goal: Nodo objetivo.
    :return: Lista con el camino al nodo objetivo o None si no se encuentra.
    """
    depth = 0  # Comenzamos con un límite de profundidad de 0
    while True:  # Iteramos indefinidamente
        print(f"Buscando con límite de profundidad: {depth}")
        result = dls(graph, start, goal, depth)
        if result:  # Si encontramos el objetivo, devolvemos el camino
            return result
        depth += 1  # Incrementamos el límite de profundidad en cada iteración


# Definimos un grafo con pueblos mágicos de Jalisco
grafo_pueblos_magicos_jalisco = {
    "Tequila": ["Mazamitla", "San Sebastián del Oeste"],
    "Mazamitla": ["Tapalpa"],
    "San Sebastián del Oeste": ["Mascota"],
    "Tapalpa": ["Ajijic"],
    "Mascota": ["Talpa de Allende"],
    "Ajijic": [],
    "Talpa de Allende": ["Lagos de Moreno"],
    "Lagos de Moreno": []
}

# Parámetros de búsqueda
nodo_inicial = "Tequila"
nodo_objetivo = "Lagos de Moreno"

# Ejecutamos la búsqueda en profundidad iterativa
camino = iddfs(grafo_pueblos_magicos_jalisco, nodo_inicial, nodo_objetivo)

# Mostramos el resultado
if camino:
    print(f"Camino encontrado: {camino}")
else:
    print(f"No se encontró el nodo '{nodo_objetivo}'.")


# Parámetros de búsqueda para el segundo camino
nodo_inicial_2 = "Mazamitla"
nodo_objetivo_2 = "Ajijic"

# División visual en la consola para separar los dos caminos
print("\n" + "=" * 50 + "\n")

# Ejecutamos la búsqueda en profundidad iterativa para el segundo camino
camino_2 = iddfs(grafo_pueblos_magicos_jalisco, nodo_inicial_2, nodo_objetivo_2)

# Mostramos el resultado del segundo camino
if camino_2:
    print(f"Camino 2 encontrado (de {nodo_inicial_2} a {nodo_objetivo_2}): {camino_2}")
else:
    print(f"No se encontró el nodo '{nodo_objetivo_2}' desde '{nodo_inicial_2}'.")