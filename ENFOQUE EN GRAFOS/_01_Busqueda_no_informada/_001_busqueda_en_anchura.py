from collections import deque  # Importamos deque para usarlo como una cola eficiente

def bfs(graph, start, goal):
    """
    Función para realizar una búsqueda en anchura (BFS) Breadth-First Search.
    Cómo funciona: Explora todos los nodos a un nivel de profundidad antes de pasar al      siguiente nivel. Es ideal para encontrar el camino más corto en grafos no ponderados.
    Aplicaciones comunes:
        Encontrar el camino más corto en un grafo no ponderado.
        Resolver problemas de conectividad en grafos.
        Resolver rompecabezas como laberintos.
    :param graph: Diccionario que representa el grafo.
    :param start: Nodo de inicio.
    :param goal: Nodo objetivo.
    :return: Lista con el camino más corto desde start hasta goal.
    """
    
    queue = deque([(start, [start])])  # Cola con (nodo actual, camino hasta él)
    visited = set()  # Conjunto para almacenar nodos visitados

    while queue:
        node, path = queue.popleft()  # Extraemos el primer nodo en la cola
        
        if node == goal:  # Si hemos encontrado el destino, devolvemos el camino
            return path  

        if node not in visited:  # Si el nodo no ha sido visitado
            visited.add(node)  # Lo marcamos como visitado
            
            for neighbor in graph.get(node, []):  # Recorremos los vecinos del nodo
                if neighbor not in visited:  # Solo agregamos nodos no visitados
                    queue.append((neighbor, path + [neighbor]))  # Agregamos a la cola

    return None  # Si no encontramos el objetivo, devolvemos None

# Definimos el grafo con las conexiones entre lugares
graph = {
    "Casa": ["Parque", "Escuela"],
    "Parque": ["Tienda"],
    "Escuela": ["Biblioteca"],
    "Biblioteca": ["Tienda"],
    "Tienda": []
}

# Ejecutamos BFS para encontrar el camino más corto de "Casa" a "Tienda"
camino = bfs(graph, "Casa", "Tienda")

# Mostramos el resultado
print("Camino más corto:", camino)
