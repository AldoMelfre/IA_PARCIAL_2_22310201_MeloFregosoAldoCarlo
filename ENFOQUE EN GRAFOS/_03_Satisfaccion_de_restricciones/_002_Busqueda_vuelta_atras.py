# ============================================
# BÚSQUEDA DE VUELTA ATRÁS (BACKTRACKING) - PROBLEMA DE LAS N-REINAS
# ============================================

# DESCRIPCIÓN TEÓRICA:
# El problema de las N-reinas consiste en colocar N reinas en un tablero de ajedrez de tamaño N×N
# de manera que ninguna reina ataque a otra. Una reina puede atacar a otra si están en la misma fila,
# columna o diagonal.
# 
# MÉTODO:
# Este algoritmo utiliza **Backtracking** para explorar todas las posibles configuraciones del tablero.
# Si una configuración no cumple las restricciones, retrocede (backtrack) y prueba otra configuración.

# ============================================
# FUNCIÓN PARA VERIFICAR LAS RESTRICCIONES
# ============================================
def es_valido(asignacion, fila, columna):
    """
    Verifica si colocar una reina en una posición es válido.
    :param asignacion: Diccionario con las filas ya asignadas a columnas.
    :param fila: Fila donde se quiere colocar la reina.
    :param columna: Columna donde se quiere colocar la reina.
    :return: True si la posición es válida, False en caso contrario.
    """
    for fila_asignada, columna_asignada in asignacion.items():
        # Verificar si están en la misma columna
        if columna_asignada == columna:
            return False
        # Verificar si están en la misma diagonal
        if abs(fila_asignada - fila) == abs(columna_asignada - columna):
            return False
    return True  # Si no hay conflictos, la posición es válida

# ============================================
# FUNCIÓN PRINCIPAL DE BACKTRACKING
# ============================================
def backtracking_n_reinas(asignacion, n):
    """
    Implementa el algoritmo de Backtracking para resolver el problema de las N-reinas.
    :param asignacion: Diccionario con las filas ya asignadas a columnas.
    :param n: Tamaño del tablero (N×N).
    :return: Una asignación completa que satisface las restricciones, o None si no hay solución.
    """
    if len(asignacion) == n:  # Si todas las filas tienen una reina asignada, devolvemos la solución
        return asignacion

    fila = len(asignacion)  # Determinamos la fila actual a asignar
    for columna in range(n):  # Probamos cada columna en la fila actual
        if es_valido(asignacion, fila, columna):  # Verificamos si la posición es válida
            asignacion[fila] = columna  # Asignamos la reina a esta columna
            resultado = backtracking_n_reinas(asignacion, n)  # Llamada recursiva
            if resultado is not None:  # Si encontramos una solución, la devolvemos
                return resultado
            del asignacion[fila]  # Si no es solución, eliminamos la asignación (backtrack)

    return None  # Si no hay solución, devolvemos None

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
# Llamamos al algoritmo de Backtracking para resolver el problema
solucion = backtracking_n_reinas({}, n)

# Mostramos el resultado
if solucion:
    print(f"Solución encontrada para un tablero de {n}x{n}:")
    for fila, columna in solucion.items():
        print(f"Reina en fila {fila}, columna {columna}")
    mostrar_tablero(solucion, n)  # Mostramos el tablero gráficamente
else:
    print("No se encontró solución.")