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
        path = [start]
    if visited is None:
        visited = set()

    visited.add(start)  # Marcamos el nodo como visitado

    if start == goal:  # Si encontramos el producto, devolvemos el camino
        return path

    for neighbor in graph.get(start, []):  # Recorremos las subcategorías o productos
        if neighbor not in visited:  # Solo exploramos nodos no visitados
            result = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if result:  # Si encontramos el producto, devolvemos el camino
                return result

    return None  # Si no encontramos el producto, devolvemos None


# Definimos el catálogo de la tienda como un grafo
catalogo = {
    "Inicio": ["Camisetas", "Sudaderas", "Accesorios"],
    "Camisetas": ["Camiseta Blanca", "Camiseta Negra", "Camiseta Roja"],
    "Sudaderas": ["Sudadera Azul", "Sudadera Gris"],
    "Accesorios": ["Gorras", "Calcetines"],
    "Gorras": ["Gorra Negra", "Gorra Blanca"],
    "Calcetines": ["Calcetines Largos", "Calcetines Cortos"],
}

# Buscamos un producto específico en el catálogo
producto_a_buscar = "Sudadera Gris"
camino = dfs(catalogo, "Inicio", producto_a_buscar)

# Mostramos el resultado
if camino:
    print(f"Producto encontrado: {producto_a_buscar}")
    print(f"Camino para encontrarlo: {camino}")
else:
    print(f"El producto '{producto_a_buscar}' no se encuentra en el catálogo.")

    #PODEMOS HACER INTERACTIVO ESTE SISTEMA AGREGANDO INPUTS DE BUSQUEDA   
# Y MOSTRANDO LOS RESULTADOS EN UNA INTERFAZ GRAFICA
# O EN UNA PAGINA WEB
# O SIMPLEMENTE EN LA CONSOLA

#DE LA SIGUIENTE MANERA:
