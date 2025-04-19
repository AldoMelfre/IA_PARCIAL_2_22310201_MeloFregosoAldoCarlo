# ============================================
# BÚSQUEDA AO* (AND-OR)
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La búsqueda AO* es un algoritmo de búsqueda informada que se utiliza en grafos AND-OR.
# En un grafo AND-OR:
# - Algunos nodos tienen múltiples hijos que deben resolverse conjuntamente (AND).
# - Otros nodos tienen hijos alternativos donde solo uno necesita resolverse (OR).
# 
# El objetivo de AO* es encontrar la solución más eficiente considerando estas relaciones AND-OR.
# 
# CARACTERÍSTICAS:
# - Utiliza una heurística para guiar la búsqueda hacia la solución más prometedora.
# - Propaga los valores hacia atrás desde los nodos hoja hasta el nodo raíz para actualizar los costos.
# - Es útil en problemas de planificación, toma de decisiones y sistemas expertos.

# APLICACIÓN:
# Este algoritmo es útil en problemas como:
# - Árboles de decisión.
# - Resolución de problemas con dependencias AND-OR.
# - Sistemas de razonamiento lógico.

# ============================================
# CLASE NODO
# ============================================
class NodoAO:
    """
    Clase que representa un nodo en un grafo AND-OR.
    """
    def __init__(self, estado, heuristica=0):
        self.estado = estado  # Estado del nodo (nombre o identificador)
        self.heuristica = heuristica  # Valor heurístico del nodo
        self.hijos = []  # Lista de hijos del nodo (pueden ser AND o OR)
        self.tipo = "OR"  # Tipo de nodo: "AND" o "OR"
        self.solucion = False  # Indica si el nodo forma parte de la solución

    def agregar_hijos(self, hijos, tipo="OR"):
        """
        Agrega hijos al nodo y define si son de tipo AND o OR.
        :param hijos: Lista de nodos hijos.
        :param tipo: Tipo de relación ("AND" o "OR").
        """
        self.hijos = hijos
        self.tipo = tipo

# ============================================
# FUNCIÓN PARA PROPAGAR VALORES HACIA ATRÁS
# ============================================
def propagar_valores(nodo):
    """
    Propaga los valores heurísticos hacia atrás desde los nodos hoja hasta el nodo raíz.
    :param nodo: Nodo actual.
    :return: Valor heurístico actualizado del nodo.
    """
    if not nodo.hijos:  # Si el nodo no tiene hijos, es una hoja
        return nodo.heuristica

    if nodo.tipo == "OR":
        # Para nodos OR, seleccionamos el hijo con el menor valor heurístico
        nodo.heuristica = min(propagar_valores(hijo) for hijo in nodo.hijos)
    elif nodo.tipo == "AND":
        # Para nodos AND, sumamos los valores heurísticos de todos los hijos
        nodo.heuristica = sum(propagar_valores(hijo) for hijo in nodo.hijos)

    return nodo.heuristica

# ============================================
# FUNCIÓN PARA EJECUTAR LA BÚSQUEDA AO*
# ============================================
def busqueda_ao(nodo):
    """
    Implementación de la búsqueda AO*.
    :param nodo: Nodo raíz del grafo AND-OR.
    :return: Lista con los nodos que forman parte de la solución.
    """
    # Propagamos los valores heurísticos hacia atrás
    propagar_valores(nodo)

    # Lista para almacenar la solución
    solucion = []

    # Función auxiliar para recorrer el grafo y construir la solución
    def construir_solucion(nodo):
        if not nodo.hijos:  # Si el nodo no tiene hijos, es una hoja
            solucion.append(nodo.estado)
            nodo.solucion = True
            return

        if nodo.tipo == "OR":
            # Para nodos OR, seleccionamos el hijo con el menor valor heurístico
            mejor_hijo = min(nodo.hijos, key=lambda hijo: hijo.heuristica)
            construir_solucion(mejor_hijo)
        elif nodo.tipo == "AND":
            # Para nodos AND, todos los hijos deben formar parte de la solución
            for hijo in nodo.hijos:
                construir_solucion(hijo)

        nodo.solucion = True

    # Construimos la solución a partir del nodo raíz
    construir_solucion(nodo)
    return solucion

# ============================================
# EJEMPLO DE GRAFO AND-OR CON CIUDADES EUROPEAS
# ============================================
# Creamos los nodos del grafo
nodo_madrid = NodoAO("Madrid", heuristica=10)
nodo_paris = NodoAO("París", heuristica=5)
nodo_berlin = NodoAO("Berlín", heuristica=2)
nodo_roma = NodoAO("Roma", heuristica=1)
nodo_viena = NodoAO("Viena", heuristica=7)
nodo_atenas = NodoAO("Atenas", heuristica=3)

# Definimos las relaciones AND-OR entre las ciudades
nodo_madrid.agregar_hijos([nodo_paris, nodo_berlin], tipo="OR")  # Madrid tiene hijos París y Berlín (OR)
nodo_paris.agregar_hijos([nodo_roma, nodo_viena], tipo="AND")  # París tiene hijos Roma y Viena (AND)
nodo_berlin.agregar_hijos([nodo_atenas], tipo="OR")  # Berlín tiene un hijo Atenas (OR)

# ============================================
# EJECUCIÓN DE LA BÚSQUEDA AO*
# ============================================
# Ejecutamos la búsqueda AO* a partir del nodo raíz (Madrid)
solucion_ao = busqueda_ao(nodo_madrid)

# Mostramos el resultado
print(f"Nodos que forman parte de la solución: {solucion_ao}")