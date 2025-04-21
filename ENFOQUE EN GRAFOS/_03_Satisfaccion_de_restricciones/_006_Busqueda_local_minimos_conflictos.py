# ============================================
# BÚSQUEDA LOCAL CON MÍNIMOS CONFLICTOS (MIN-CONFLICTS)
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La búsqueda local con mínimos conflictos es un algoritmo heurístico para resolver problemas de satisfacción
# de restricciones (CSP). Este enfoque intenta minimizar los conflictos en cada paso, moviéndose hacia una solución
# válida de manera eficiente.
# 
# CARACTERÍSTICAS:
# - Variables: Elementos que deben ser asignados (por ejemplo, filas en el problema de las N-reinas).
# - Dominios: Conjunto de valores posibles para cada variable (por ejemplo, columnas en el problema de las N-reinas).
# - Restricciones: Condiciones que deben cumplirse entre las variables (por ejemplo, no estar en la misma columna o diagonal).
# 
# EJEMPLO:
# Resolver el problema de las N-reinas utilizando búsqueda local con mínimos conflictos.

import random

# ============================================
# FUNCIÓN PARA CONTAR CONFLICTOS
# ============================================
def contar_conflictos(asignacion, fila, columna):
    """
    Cuenta el número de conflictos para colocar una reina en una posición específica.
    :param asignacion: Diccionario con las filas ya asignadas a columnas.
    :param fila: Fila donde se quiere colocar la reina.
    :param columna: Columna donde se quiere colocar la reina.
    :return: Número de conflictos.
    """
    conflictos = 0
    for fila_asignada, columna_asignada in asignacion.items():
        if fila_asignada == fila:
            continue
        # Conflicto en la misma columna
        if columna_asignada == columna:
            conflictos += 1
        # Conflicto en la misma diagonal
        if abs(fila_asignada - fila) == abs(columna_asignada - columna):
            conflictos += 1
    return conflictos

# ============================================
# FUNCIÓN PRINCIPAL DE MIN-CONFLICTS
# ============================================
def min_conflicts(n, max_iter=10000, reinicios=5):
    """
    Implementa el algoritmo de búsqueda local con mínimos conflictos para resolver el problema de las N-reinas.
    :param n: Tamaño del tablero (N×N).
    :param max_iter: Número máximo de iteraciones por intento.
    :param reinicios: Número máximo de reinicios aleatorios.
    :return: Una asignación completa que satisface las restricciones, o None si no hay solución.
    """
    for intento in range(reinicios):
        # Generamos una asignación inicial aleatoria
        asignacion = {fila: random.randint(0, n - 1) for fila in range(n)}

        for _ in range(max_iter):
            # Verificamos si la asignación actual no tiene conflictos
            conflictos = [(fila, contar_conflictos(asignacion, fila, columna))
                          for fila, columna in asignacion.items()]
            conflictos = [fila for fila, conflicto in conflictos if conflicto > 0]

            if not conflictos:  # Si no hay conflictos, devolvemos la solución
                return asignacion

            # Elegimos una fila con conflictos al azar
            fila = random.choice(conflictos)

            # Encontramos la columna con el menor número de conflictos para esa fila
            mejor_columna = min(range(n), key=lambda columna: contar_conflictos(asignacion, fila, columna))

            # Actualizamos la asignación
            asignacion[fila] = mejor_columna

    return None  # Si no encontramos solución después de varios reinicios, devolvemos None

# ============================================
# FUNCIÓN PARA MOSTRAR EL TABLERO
# ============================================
def mostrar_tablero(solucion, n):
    """
    Muestra el tablero con la solución de las N-reinas.
    :param solucion: Diccionario con la solución del problema.
    :param n: Tamaño del tablero (N×N).
    """
    tablero = [["." for _ in range(n)] for _ in range(n)]  # Creamos un tablero vacío
    for fila, columna in solucion.items():
        tablero[fila][columna] = "Q"  # Colocamos una reina ("Q") en la posición correspondiente

    print("\nTablero:")
    for fila in tablero:
        print(" ".join(fila))  # Mostramos cada fila del tablero

# ============================================
# EJEMPLO: PROBLEMA DE LAS N-REINAS
# ============================================
# Tamaño del tablero (N×N)
n = 8  # Cambia este valor para probar con diferentes tamaños de tablero

# ============================================
# EJECUCIÓN DEL ALGORITMO
# ============================================
# Llamamos al algoritmo de búsqueda local con mínimos conflictos para resolver el problema
solucion = min_conflicts(n, max_iter=10000, reinicios=10)

# Mostramos el resultado
if solucion:
    print(f"Solución encontrada para un tablero de {n}x{n}:")
    for fila, columna in solucion.items():
        print(f"Reina en fila {fila}, columna {columna}")
    mostrar_tablero(solucion, n)  # Mostramos el tablero gráficamente
else:
    print("No se encontró solución después de varios intentos.")