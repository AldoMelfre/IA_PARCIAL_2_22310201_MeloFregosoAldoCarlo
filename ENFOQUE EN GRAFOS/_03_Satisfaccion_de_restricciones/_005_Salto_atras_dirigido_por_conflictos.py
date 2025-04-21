# ============================================
# SALTO ATRÁS DIRIGIDO POR CONFLICTOS (CONFLICT-DIRECTED BACKJUMPING)
# ============================================

# DESCRIPCIÓN TEÓRICA:
# El salto atrás dirigido por conflictos es una mejora del algoritmo de Backtracking.
# En lugar de retroceder paso a paso, este algoritmo retrocede directamente al punto donde ocurrió el conflicto.
# Esto reduce el número de pasos necesarios para encontrar una solución o determinar que no existe.
# 
# CARACTERÍSTICAS:
# - Variables: Elementos que deben ser asignados (por ejemplo, filas en el problema de las N-reinas).
# - Dominios: Conjunto de valores posibles para cada variable (por ejemplo, columnas en el problema de las N-reinas).
# - Restricciones: Condiciones que deben cumplirse entre las variables (por ejemplo, no estar en la misma columna o diagonal).
# 
# EJEMPLO:
# Resolver el problema de las N-reinas utilizando salto atrás dirigido por conflictos.

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
# FUNCIÓN PRINCIPAL DE SALTO ATRÁS DIRIGIDO POR CONFLICTOS
# ============================================
def salto_atras_dirigido_por_conflictos(asignacion, n, fila, conflictos):
    """
    Implementa el algoritmo de salto atrás dirigido por conflictos para resolver el problema de las N-reinas.
    :param asignacion: Diccionario con las filas ya asignadas a columnas.
    :param n: Tamaño del tablero (N×N).
    :param fila: Fila actual a asignar.
    :param conflictos: Diccionario que rastrea los conflictos para cada fila.
    :return: Una asignación completa que satisface las restricciones, o None si no hay solución.
    """
    if fila == n:  # Si todas las filas tienen una reina asignada, devolvemos la solución
        return asignacion

    for columna in range(n):  # Probamos cada columna en la fila actual
        if es_valido(asignacion, fila, columna):  # Verificamos si la posición es válida
            asignacion[fila] = columna  # Asignamos la reina a esta columna
            resultado = salto_atras_dirigido_por_conflictos(asignacion, n, fila + 1, conflictos)  # Llamada recursiva
            if resultado is not None:  # Si encontramos una solución, la devolvemos
                return resultado
            del asignacion[fila]  # Si no es solución, eliminamos la asignación (backtrack)
        else:
            conflictos[fila] = fila - 1  # Registramos el conflicto con la fila anterior

    # Si no se puede asignar una reina en esta fila, retrocedemos al punto de conflicto
    if fila in conflictos:
        return None  # Retrocedemos directamente al punto de conflicto

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

# Inicializamos el diccionario de conflictos
conflictos = {}

# ============================================
# EJECUCIÓN DEL ALGORITMO
# ============================================
# Llamamos al algoritmo de salto atrás dirigido por conflictos para resolver el problema
solucion = salto_atras_dirigido_por_conflictos({}, n, 0, conflictos)

# Mostramos el resultado
if solucion:
    print(f"Solución encontrada para un tablero de {n}x{n}:")
    for fila, columna in solucion.items():
        print(f"Reina en fila {fila}, columna {columna}")
    mostrar_tablero(solucion, n)  # Mostramos el tablero gráficamente
else:
    print("No se encontró solución.")