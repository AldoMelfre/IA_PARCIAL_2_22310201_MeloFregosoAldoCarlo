# La búsqueda bidireccional es un algoritmo eficiente para encontrar el camino más corto entre dos nodos en un grafo.
# Este método realiza búsquedas simultáneas desde el nodo inicial y el nodo objetivo, avanzando hacia el centro.
# Cuando las dos búsquedas se encuentran, se combina el camino desde ambas direcciones para obtener la solución.
# Es especialmente útil en grafos grandes, ya que reduce significativamente el espacio de búsqueda en comparación con
# una búsqueda unidireccional.z

from collections import deque  # Importamos deque para manejar las colas de búsqueda de manera eficiente

def busqueda_bidireccional(grafo, inicio, objetivo):
    """
    Búsqueda Bidireccional para encontrar el camino más corto entre dos nodos.
    :param grafo: Diccionario que representa el grafo (nodo: [vecinos]).
    :param inicio: Nodo inicial.
    :param objetivo: Nodo objetivo.
    :return: Lista con el camino entre inicio y objetivo, o None si no se encuentra.
    """
    # Caso especial: si el nodo inicial es igual al nodo objetivo
    if inicio == objetivo:
        return [inicio]

    # Inicializamos las colas de búsqueda y los conjuntos visitados
    cola_inicio = deque([[inicio]])  # Cola para la búsqueda desde el nodo inicial
    cola_objetivo = deque([[objetivo]])  # Cola para la búsqueda desde el nodo objetivo
    visitados_inicio = {inicio}  # Conjunto de nodos visitados desde el inicio
    visitados_objetivo = {objetivo}  # Conjunto de nodos visitados desde el objetivo

    # Mientras ambas colas tengan elementos, continuamos la búsqueda
    while cola_inicio and cola_objetivo:
        # Expansión desde el inicio
        camino_inicio = cola_inicio.popleft()  # Extraemos el primer camino de la cola
        actual_inicio = camino_inicio[-1]  # Último nodo del camino actual

        # Recorremos los vecinos del nodo actual desde el inicio
        for vecino in grafo.get(actual_inicio, []):
            if vecino not in visitados_inicio:  # Si el vecino no ha sido visitado
                nuevo_camino = camino_inicio + [vecino]  # Construimos un nuevo camino
                cola_inicio.append(nuevo_camino)  # Lo agregamos a la cola
                visitados_inicio.add(vecino)  # Marcamos el vecino como visitado

                # Verificamos si este vecino ya fue visitado desde el objetivo
                if vecino in visitados_objetivo:
                    # Si se encuentra, combinamos los caminos y devolvemos el resultado
                    camino_objetivo = next(camino for camino in cola_objetivo if camino[-1] == vecino)
                    return nuevo_camino + camino_objetivo[::-1][1:]

        # Expansión desde el objetivo
        camino_objetivo = cola_objetivo.popleft()  # Extraemos el primer camino de la cola
        actual_objetivo = camino_objetivo[-1]  # Último nodo del camino actual

        # Recorremos los vecinos del nodo actual desde el objetivo
        for vecino in grafo.get(actual_objetivo, []):
            if vecino not in visitados_objetivo:  # Si el vecino no ha sido visitado
                nuevo_camino = camino_objetivo + [vecino]  # Construimos un nuevo camino
                cola_objetivo.append(nuevo_camino)  # Lo agregamos a la cola
                visitados_objetivo.add(vecino)  # Marcamos el vecino como visitado

                # Verificamos si este vecino ya fue visitado desde el inicio
                if vecino in visitados_inicio:
                    # Si se encuentra, combinamos los caminos y devolvemos el resultado
                    camino_inicio = next(camino for camino in cola_inicio if camino[-1] == vecino)
                    return camino_inicio + nuevo_camino[::-1][1:]

    # Si no se encuentra un camino, devolvemos None
    return None


# Definimos un grafo con pueblos mágicos de Jalisco
grafo_pueblos_magicos_jalisco = {
    "Tequila": ["Mazamitla", "San Sebastián del Oeste"],  # Conexiones desde Tequila
    "Mazamitla": ["Tapalpa"],  # Conexiones desde Mazamitla
    "San Sebastián del Oeste": ["Mascota"],  # Conexiones desde San Sebastián del Oeste
    "Tapalpa": ["Ajijic"],  # Conexiones desde Tapalpa
    "Mascota": ["Talpa de Allende"],  # Conexiones desde Mascota
    "Ajijic": [],  # Ajijic no tiene conexiones
    "Talpa de Allende": ["Lagos de Moreno"],  # Conexiones desde Talpa de Allende
    "Lagos de Moreno": []  # Lagos de Moreno no tiene conexiones
}

# Parámetros de búsqueda
nodo_inicial = "Tequila"  # Nodo inicial de la búsqueda
nodo_objetivo = "Lagos de Moreno"  # Nodo objetivo de la búsqueda

# Ejecutamos la búsqueda bidireccional
camino = busqueda_bidireccional(grafo_pueblos_magicos_jalisco, nodo_inicial, nodo_objetivo)

# Mostramos el resultado
if camino:
    print(f"Camino encontrado (de {nodo_inicial} a {nodo_objetivo}): {camino}")
else:
    print(f"No se encontró un camino entre '{nodo_inicial}' y '{nodo_objetivo}'.")