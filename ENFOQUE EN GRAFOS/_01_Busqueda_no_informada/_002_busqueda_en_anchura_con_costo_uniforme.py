import heapq  # Importamos heapq para usar una cola de prioridad

def ucs(graph, start, goal):
    """
    Búsqueda en Anchura de Costo Uniforme (UCS) para encontrar el camino más barato.
    :param graph: Diccionario que representa el grafo con costos (ciudad: [(vecina, costo)]).
    :param start: Ciudad de inicio.
    :param goal: Ciudad destino.
    :return: Tupla con el costo total y el camino más barato desde start hasta goal.
    """
    # Cola de prioridad para almacenar (costo acumulado, ciudad actual, camino hasta la ciudad)
    priority_queue = [(0, start, [start])]
    visited = set()  # Conjunto para almacenar ciudades visitadas

    while priority_queue:
        # Extraemos la ciudad con el menor costo acumulado
        cost, city, path = heapq.heappop(priority_queue)

        if city == goal:  # Si hemos llegado al destino, devolvemos el costo y el camino
            return cost, path

        if city not in visited:  # Si la ciudad no ha sido visitada
            visited.add(city)  # La marcamos como visitada

            # Recorremos las ciudades vecinas
            for neighbor, travel_cost in graph.get(city, []):
                if neighbor not in visited:  # Solo procesamos ciudades no visitadas
                    # Agregamos a la cola de prioridad con el costo acumulado actualizado
                    heapq.heappush(priority_queue, (cost + travel_cost, neighbor, path + [neighbor]))

    return None  # Si no encontramos el destino, devolvemos None

# Definimos el grafo con las conexiones entre ciudades mexicanas y sus costos
graph = {
    "Ciudad de México": [("Guadalajara", 10), ("Monterrey", 15)],
    "Guadalajara": [("Tijuana", 12), ("Cancún", 15)],
    "Monterrey": [("Mérida", 10)],
    "Tijuana": [("Chihuahua", 2)],
    "Cancún": [("Chihuahua", 5)],
    "Mérida": [("Chihuahua", 10)],
    "Chihuahua": []
}

# Ejecutamos UCS para encontrar el camino más barato de "Ciudad de México" a "Chihuahua"
resultado = ucs(graph, "Ciudad de México", "Chihuahua")

# Mostramos el resultado
if resultado:
    costo, camino = resultado
    print(f"Camino más barato: {camino} con un costo total de: {costo}")
else:
    print("No se encontró un camino al destino.")