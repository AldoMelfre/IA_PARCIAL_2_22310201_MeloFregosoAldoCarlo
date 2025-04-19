# ============================================
# BÚSQUEDA DE ASCENSIÓN DE COLINAS
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La búsqueda de ascensión de colinas es un algoritmo de búsqueda informada que utiliza una heurística
# para guiarse hacia el objetivo. Este algoritmo selecciona el vecino con el mejor valor heurístico
# en cada paso, intentando "ascender" hacia el objetivo.
# 
# CARACTERÍSTICAS:
# - Es un algoritmo **greedy** (voraz), ya que siempre selecciona el mejor vecino en cada paso.
# - No garantiza encontrar la solución óptima, ya que puede quedar atrapado en:
#   - Máximos locales: Un punto que parece ser el mejor, pero no es el óptimo global.
#   - Mesetas: Una región donde todos los vecinos tienen el mismo valor heurístico.
#   - Crestas: Una región donde no hay un vecino mejor, pero el óptimo está más allá.
# 
# APLICACIÓN:
# Este algoritmo es útil en problemas donde:
# - La solución puede aproximarse iterativamente.
# - No se requiere encontrar la solución óptima, sino una solución aceptable.

# ============================================
# CLASE NODO
# ============================================
class NodoColina:
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
# FUNCIÓN PARA EJECUTAR LA BÚSQUEDA DE ASCENSIÓN DE COLINAS
# ============================================
def busqueda_ascension_colinas(nodo_inicial):
    """
    Implementación de la búsqueda de ascensión de colinas.
    :param nodo_inicial: Nodo inicial desde donde comienza la búsqueda.
    :return: Nodo objetivo alcanzado y el camino recorrido.
    """
    nodo_actual = nodo_inicial
    camino = [nodo_actual.estado]  # Lista para almacenar el camino recorrido

    while True:
        # Seleccionamos el vecino con el mejor valor heurístico
        mejor_vecino = None
        for vecino in nodo_actual.vecinos:
            if mejor_vecino is None or vecino.heuristica < mejor_vecino.heuristica:
                mejor_vecino = vecino

        # Si no hay un vecino mejor, hemos alcanzado un máximo local
        if mejor_vecino is None or mejor_vecino.heuristica >= nodo_actual.heuristica:
            break

        # Nos movemos al mejor vecino
        nodo_actual = mejor_vecino
        camino.append(nodo_actual.estado)

    return nodo_actual, camino

# ============================================
# EJEMPLO DE GRAFO CON CIUDADES EUROPEAS
# ============================================
# Creamos los nodos del grafo
nodo_madrid = NodoColina("Madrid", heuristica=10)
nodo_paris = NodoColina("París", heuristica=8)
nodo_berlin = NodoColina("Berlín", heuristica=6)
nodo_roma = NodoColina("Roma", heuristica=4)
nodo_viena = NodoColina("Viena", heuristica=3)
nodo_atenas = NodoColina("Atenas", heuristica=0)  # Nodo objetivo con heurística 0

# Definimos las conexiones entre los nodos
nodo_madrid.agregar_vecino(nodo_paris)
nodo_madrid.agregar_vecino(nodo_berlin)
nodo_paris.agregar_vecino(nodo_roma)
nodo_berlin.agregar_vecino(nodo_viena)
nodo_roma.agregar_vecino(nodo_atenas)
nodo_viena.agregar_vecino(nodo_atenas)

# ============================================
# EJECUCIÓN DE LA BÚSQUEDA DE ASCENSIÓN DE COLINAS
# ============================================
# Ejecutamos la búsqueda desde el nodo inicial (Madrid)
nodo_objetivo, camino_recorrido = busqueda_ascension_colinas(nodo_madrid)

# Mostramos el resultado
print(f"Nodo objetivo alcanzado: {nodo_objetivo.estado} con heurística {nodo_objetivo.heuristica}")
print(f"Camino recorrido: {camino_recorrido}")