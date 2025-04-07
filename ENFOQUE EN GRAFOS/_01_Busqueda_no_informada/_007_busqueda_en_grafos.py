from collections import deque

def busqueda_en_grafos(grafo, inicio, objetivo):
    """
    Búsqueda en grafos para encontrar un camino entre dos nodos.
    :param grafo: Diccionario que representa el grafo (nodo: [vecinos]).
    :param inicio: Nodo inicial.
    :param objetivo: Nodo objetivo.
    :return: Lista con el camino entre inicio y objetivo, o None si no se encuentra.
    """
    # Caso especial: si el nodo inicial es igual al nodo objetivo
    if inicio == objetivo:
        return [inicio]

    # Inicializamos la cola de búsqueda y el conjunto de nodos visitados
    cola = deque([[inicio]])  # Cola que almacena caminos
    visitados = set()  # Conjunto de nodos visitados

    while cola:
        # Extraemos el primer camino de la cola
        camino = cola.popleft()
        nodo_actual = camino[-1]  # Último nodo del camino actual

        # Si el nodo actual ya fue visitado, lo ignoramos
        if nodo_actual in visitados:
            continue

        # Marcamos el nodo actual como visitado
        visitados.add(nodo_actual)

        # Recorremos los vecinos del nodo actual
        for vecino in grafo.get(nodo_actual, []):
            # Construimos un nuevo camino que incluye al vecino
            nuevo_camino = camino + [vecino]

            # Si encontramos el nodo objetivo, devolvemos el camino
            if vecino == objetivo:
                return nuevo_camino

            # Agregamos el nuevo camino a la cola
            cola.append(nuevo_camino)

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

# Parámetros de búsqueda para el primer camino
nodo_inicial_1 = "Tequila"
nodo_objetivo_1 = "Lagos de Moreno"

# Ejecutamos la búsqueda en grafos para el primer camino
camino_1 = busqueda_en_grafos(grafo_pueblos_magicos, nodo_inicial_1, nodo_objetivo_1)

# Mostramos el resultado del primer camino
if camino_1:
    print(f"Camino encontrado (de {nodo_inicial_1} a {nodo_objetivo_1}): {camino_1}")
else:
    print(f"No se encontró un camino entre '{nodo_inicial_1}' y '{nodo_objetivo_1}'.")

# División visual en la consola
print("\n" + "#" * 50 + "\n")

# Parámetros de búsqueda para el segundo camino
nodo_inicial_2 = "Mazamitla"
nodo_objetivo_2 = "Mascota"

# Ejecutamos la búsqueda en grafos para el segundo camino
camino_2 = busqueda_en_grafos(grafo_pueblos_magicos, nodo_inicial_2, nodo_objetivo_2)

# Mostramos el resultado del segundo camino
if camino_2:
    print(f"Camino encontrado (de {nodo_inicial_2} a {nodo_objetivo_2}): {camino_2}")
else:
    print(f"No se encontró un camino entre '{nodo_inicial_2}' y '{nodo_objetivo_2}'.")