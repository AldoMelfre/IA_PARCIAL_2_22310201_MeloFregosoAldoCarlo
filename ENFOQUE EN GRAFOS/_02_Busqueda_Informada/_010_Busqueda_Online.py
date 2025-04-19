# ============================================
# BÚSQUEDA ONLINE
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La búsqueda online es un algoritmo de búsqueda diseñado para entornos donde el agente no tiene
# conocimiento previo del espacio de búsqueda. El agente debe explorar el entorno mientras toma
# decisiones en tiempo real.
# 
# CARACTERÍSTICAS:
# - El agente no conoce el grafo completo al inicio; descubre los nodos y las conexiones mientras se mueve.
# - Es útil en entornos dinámicos o desconocidos.
# - Puede utilizar estrategias como el aprendizaje basado en la experiencia para mejorar su desempeño.
# 
# APLICACIÓN:
# Este algoritmo es útil en problemas como:
# - Exploración de robots en entornos desconocidos.
# - Juegos y simulaciones en tiempo real.
# - Navegación en mapas desconocidos.

# ============================================
# CLASE NODO
# ============================================
class NodoOnline:
    """
    Clase que representa un nodo en el grafo.
    """
    def __init__(self, estado):
        self.estado = estado  # Estado del nodo (nombre o identificador)
        self.vecinos = {}  # Diccionario de vecinos y sus costos

    def agregar_vecino(self, vecino, costo):
        """
        Agrega un vecino al nodo con un costo asociado.
        :param vecino: Nodo vecino.
        :param costo: Costo de moverse al vecino.
        """
        self.vecinos[vecino] = costo

# ============================================
# FUNCIÓN PARA EJECUTAR LA BÚSQUEDA ONLINE
# ============================================
def busqueda_online(nodo_inicial, objetivo):
    """
    Implementación de la búsqueda online.
    :param nodo_inicial: Nodo inicial desde donde comienza la búsqueda.
    :param objetivo: Nodo objetivo que se desea alcanzar.
    :return: Camino recorrido y costo total.
    """
    nodo_actual = nodo_inicial
    camino = [nodo_actual.estado]  # Lista para almacenar el camino recorrido
    costo_total = 0  # Costo acumulado

    while nodo_actual.estado != objetivo.estado:
        # Si no hay vecinos, no se puede continuar
        if not nodo_actual.vecinos:
            print("No hay más vecinos para explorar. Búsqueda fallida.")
            return camino, costo_total

        # Seleccionamos el vecino con el menor costo
        vecino, costo = min(nodo_actual.vecinos.items(), key=lambda item: item[1])

        # Nos movemos al vecino
        nodo_actual = vecino
        camino.append(nodo_actual.estado)
        costo_total += costo

    return camino, costo_total

# ============================================
# EJEMPLO DE GRAFO CON CIUDADES EUROPEAS
# ============================================
# Creamos los nodos del grafo
nodo_madrid = NodoOnline("Madrid")
nodo_paris = NodoOnline("París")
nodo_berlin = NodoOnline("Berlín")
nodo_roma = NodoOnline("Roma")
nodo_viena = NodoOnline("Viena")
nodo_atenas = NodoOnline("Atenas")  # Nodo objetivo

# Definimos las conexiones entre los nodos
nodo_madrid.agregar_vecino(nodo_paris, 1275)
nodo_madrid.agregar_vecino(nodo_berlin, 1860)
nodo_paris.agregar_vecino(nodo_roma, 1420)
nodo_berlin.agregar_vecino(nodo_viena, 680)
nodo_roma.agregar_vecino(nodo_atenas, 1050)
nodo_viena.agregar_vecino(nodo_atenas, 1280)

# ============================================
# EJECUCIÓN DE LA BÚSQUEDA ONLINE
# ============================================
# Ejecutamos la búsqueda desde el nodo inicial (Madrid) hasta el objetivo (Atenas)
camino_recorrido, costo_total = busqueda_online(nodo_madrid, nodo_atenas)

# Mostramos el resultado
print(f"Camino recorrido: {camino_recorrido}")
print(f"Costo total: {costo_total}")