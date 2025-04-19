# ============================================
# BÚSQUEDA TABÚ
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La búsqueda tabú es un algoritmo de optimización que extiende la búsqueda local
# al permitir movimientos que empeoran la solución actual, pero evita ciclos
# mediante el uso de una lista tabú.
# 
# CARACTERÍSTICAS:
# - Utiliza una lista tabú para almacenar soluciones recientes y evitar revisitar estados.
# - Permite escapar de máximos locales al aceptar soluciones peores temporalmente.
# - Es útil en problemas de optimización combinatoria donde el espacio de búsqueda es grande.
# 
# APLICACIÓN:
# Este algoritmo es útil en problemas como:
# - Optimización de rutas (por ejemplo, el problema del viajero).
# - Diseño de redes.
# - Problemas de planificación y asignación.

# ============================================
# CLASE NODO
# ============================================
class NodoTabu:
    """
    Clase que representa un nodo en el grafo.
    """
    def __init__(self, estado, heuristica=0):
        self.estado = estado  # Estado del nodo (nombre o identificador)
        self.heuristica = heuristica  # Valor heurístico del nodo
        self.vecinos = []  # Lista de nodos vecinos

    def agregar_vecino(self, vecino):
        """
        Agrega un vecino al nodo.
        :param vecino: Nodo vecino.
        """
        self.vecinos.append(vecino)

# ============================================
# FUNCIÓN PARA EJECUTAR LA BÚSQUEDA TABÚ
# ============================================
def busqueda_tabu(nodo_inicial, iteraciones_max, tamano_tabu):
    """
    Implementación de la búsqueda tabú.
    :param nodo_inicial: Nodo inicial desde donde comienza la búsqueda.
    :param iteraciones_max: Número máximo de iteraciones.
    :param tamano_tabu: Tamaño máximo de la lista tabú.
    :return: Mejor nodo encontrado y el camino recorrido.
    """
    nodo_actual = nodo_inicial
    mejor_nodo = nodo_actual
    lista_tabu = []  # Lista tabú para almacenar nodos visitados
    camino = [nodo_actual.estado]  # Lista para almacenar el camino recorrido

    for _ in range(iteraciones_max):
        # Agregamos el nodo actual a la lista tabú
        lista_tabu.append(nodo_actual)
        if len(lista_tabu) > tamano_tabu:
            lista_tabu.pop(0)  # Eliminamos el nodo más antiguo si la lista tabú excede su tamaño

        # Seleccionamos el mejor vecino que no esté en la lista tabú
        mejor_vecino = None
        for vecino in nodo_actual.vecinos:
            if vecino not in lista_tabu and (mejor_vecino is None or vecino.heuristica < mejor_vecino.heuristica):
                mejor_vecino = vecino

        # Si no hay vecinos válidos, terminamos la búsqueda
        if mejor_vecino is None:
            break

        # Nos movemos al mejor vecino
        nodo_actual = mejor_vecino
        camino.append(nodo_actual.estado)

        # Actualizamos el mejor nodo encontrado
        if nodo_actual.heuristica < mejor_nodo.heuristica:
            mejor_nodo = nodo_actual

    return mejor_nodo, camino

# ============================================
# EJEMPLO DE GRAFO CON CIUDADES EUROPEAS
# ============================================
# Creamos los nodos del grafo
nodo_madrid = NodoTabu("Madrid", heuristica=10)
nodo_paris = NodoTabu("París", heuristica=8)
nodo_berlin = NodoTabu("Berlín", heuristica=6)
nodo_roma = NodoTabu("Roma", heuristica=4)
nodo_viena = NodoTabu("Viena", heuristica=3)
nodo_atenas = NodoTabu("Atenas", heuristica=0)  # Nodo objetivo con heurística 0

# Definimos las conexiones entre los nodos
nodo_madrid.agregar_vecino(nodo_paris)
nodo_madrid.agregar_vecino(nodo_berlin)
nodo_paris.agregar_vecino(nodo_roma)
nodo_berlin.agregar_vecino(nodo_viena)
nodo_roma.agregar_vecino(nodo_atenas)
nodo_viena.agregar_vecino(nodo_atenas)

# ============================================
# EJECUCIÓN DE LA BÚSQUEDA TABÚ
# ============================================
# Parámetros de la búsqueda
iteraciones_max = 10  # Número máximo de iteraciones
tamano_tabu = 3  # Tamaño máximo de la lista tabú

# Ejecutamos la búsqueda desde el nodo inicial (Madrid)
mejor_nodo, camino_recorrido = busqueda_tabu(nodo_madrid, iteraciones_max, tamano_tabu)

# Mostramos el resultado
print(f"Mejor nodo encontrado: {mejor_nodo.estado} con heurística {mejor_nodo.heuristica}")
print(f"Camino recorrido: {camino_recorrido}")