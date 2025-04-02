def dfs(graph, start, goal, path=None, visited=None):
    """
    Búsqueda en Profundidad (DFS) para encontrar un producto en un catálogo.
    :param graph: Diccionario que representa el grafo (categoría: [subcategorías o productos]).
    :param start: Nodo inicial (categoría o subcategoría).
    :param goal: Nodo objetivo (producto a buscar).
    :param path: Camino actual (se actualiza recursivamente).
    :param visited: Conjunto de nodos visitados.
    :return: Lista con el camino al producto o None si no se encuentra.
    """
    if path is None:
        path = [start]  # Inicializamos el camino con el nodo de inicio
    if visited is None:
        visited = set()  # Inicializamos el conjunto de nodos visitados

    visited.add(start)  # Marcamos el nodo actual como visitado

    if start == goal:  # Si el nodo actual es el objetivo, devolvemos el camino
        return path

    # Recorremos los vecinos del nodo actual
    for neighbor in graph.get(start, []):  # Obtenemos los vecinos del nodo actual
        if neighbor not in visited:  # Solo exploramos nodos no visitados
            # Llamada recursiva para explorar el vecino
            result = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if result:  # Si encontramos el producto, devolvemos el camino
                return result

    return None  # Si no encontramos el producto, devolvemos None


# Definimos el catálogo de la tienda como un grafo
catalogo = {
    "Inicio": ["Camisetas", "Sudaderas", "Accesorios"],  # Nodo raíz con las categorías principales
    "Camisetas": ["Camiseta Blanca", "Camiseta Negra", "Camiseta Roja"],  # Subcategorías de camisetas
    "Sudaderas": ["Sudadera Azul", "Sudadera Gris"],  # Subcategorías de sudaderas
    "Accesorios": ["Gorras", "Calcetines"],  # Subcategorías de accesorios
    "Gorras": ["Gorra Negra", "Gorra Blanca"],  # Subcategorías de gorras
    "Calcetines": ["Calcetines Largos", "Calcetines Cortos"],  # Subcategorías de calcetines
}

# Buscamos un producto específico en el catálogo
producto_a_buscar = "Sudadera Gris"  # Producto que queremos encontrar
camino = dfs(catalogo, "Inicio", producto_a_buscar)  # Llamamos a la función DFS

# Mostramos el resultado
if camino:
    # Si encontramos el producto, mostramos el camino para llegar a él
    print(f"Producto encontrado: {producto_a_buscar}")
    print(f"Camino para encontrarlo: {camino}")
else:
    # Si no encontramos el producto, mostramos un mensaje de error
    print(f"El producto '{producto_a_buscar}' no se encuentra en el catálogo.")

# Comentario adicional:
# Podemos hacer interactivo este sistema agregando inputs de búsqueda
# y mostrando los resultados en una interfaz gráfica, en una página web
# o simplemente en la consola.