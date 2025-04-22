# ============================================
# ACONDICIONAMIENTO DEL CORTE (CONSTRAINT PROPAGATION)
# ============================================

# DESCRIPCIÓN TEÓRICA:
# El acondicionamiento del corte es una técnica utilizada en problemas de satisfacción de restricciones (CSP).
# Este enfoque reduce los dominios de las variables propagando las restricciones entre ellas.
# En el problema del Sudoku, cada celda es una variable, y las restricciones aseguran que:
# - Los números en cada fila sean únicos.
# - Los números en cada columna sean únicos.
# - Los números en cada subcuadro 3x3 sean únicos.
# 
# CARACTERÍSTICAS:
# - Variables: Las celdas del tablero de Sudoku.
# - Dominios: Los números posibles (1-9) para cada celda.
# - Restricciones: Un número no puede repetirse en la misma fila, columna o subcuadro.
# 
# EJEMPLO:
# Resolver un tablero de Sudoku parcialmente completado utilizando acondicionamiento del corte.

# ============================================
# FUNCIÓN PARA OBTENER LAS RESTRICCIONES
# ============================================
def obtener_restricciones():
    """
    Genera las restricciones del Sudoku.
    :return: Diccionario con las restricciones para cada celda.
    """
    restricciones = {}
    for fila in range(9):
        for columna in range(9):
            celda = (fila, columna)
            restricciones[celda] = set()

            # Restricciones de fila
            for c in range(9):
                if c != columna:
                    restricciones[celda].add((fila, c))

            # Restricciones de columna
            for f in range(9):
                if f != fila:
                    restricciones[celda].add((f, columna))

            # Restricciones de subcuadro 3x3
            inicio_fila = (fila // 3) * 3
            inicio_columna = (columna // 3) * 3
            for f in range(inicio_fila, inicio_fila + 3):
                for c in range(inicio_columna, inicio_columna + 3):
                    if (f, c) != celda:
                        restricciones[celda].add((f, c))

    return restricciones

# ============================================
# FUNCIÓN PARA PROPAGAR RESTRICCIONES
# ============================================
def propagar_restricciones(tablero, dominios, restricciones):
    """
    Propaga las restricciones para reducir los dominios de las celdas.
    :param tablero: Tablero de Sudoku con las celdas asignadas.
    :param dominios: Diccionario con los dominios de cada celda.
    :param restricciones: Diccionario con las restricciones entre celdas.
    :return: Diccionario con los dominios reducidos, o None si hay inconsistencias.
    """
    while True:
        cambios = False
        for celda, valores in dominios.items():
            if len(valores) == 1:  # Si la celda tiene un único valor asignado
                valor = next(iter(valores))
                for vecina in restricciones[celda]:
                    if valor in dominios[vecina]:
                        dominios[vecina].remove(valor)  # Eliminamos el valor del dominio de las vecinas
                        cambios = True
                        if not dominios[vecina]:  # Si un dominio queda vacío, hay una inconsistencia
                            return None
        if not cambios:  # Si no hubo cambios, terminamos la propagación
            break
    return dominios

# ============================================
# FUNCIÓN PRINCIPAL PARA RESOLVER EL SUDOKU
# ============================================
def resolver_sudoku(tablero, dominios, restricciones):
    """
    Resuelve el Sudoku utilizando acondicionamiento del corte y backtracking.
    :param tablero: Tablero de Sudoku con las celdas asignadas.
    :param dominios: Diccionario con los dominios de cada celda.
    :param restricciones: Diccionario con las restricciones entre celdas.
    :return: Tablero resuelto, o None si no hay solución.
    """
    if all(len(valores) == 1 for valores in dominios.values()):  # Si todas las celdas tienen un único valor
        return {celda: next(iter(valores)) for celda, valores in dominios.items()}

    # Seleccionamos la celda con el menor dominio (mínimo número de valores posibles)
    celda = min((c for c in dominios if len(dominios[c]) > 1), key=lambda c: len(dominios[c]))

    for valor in dominios[celda]:  # Probamos cada valor en el dominio de la celda
        nuevo_dominios = {c: set(v) for c, v in dominios.items()}  # Copiamos los dominios
        nuevo_dominios[celda] = {valor}  # Asignamos el valor a la celda
        nuevo_dominios = propagar_restricciones(tablero, nuevo_dominios, restricciones)  # Propagamos restricciones
        if nuevo_dominios is not None:  # Si no hay inconsistencias
            resultado = resolver_sudoku(tablero, nuevo_dominios, restricciones)  # Llamada recursiva
            if resultado is not None:  # Si encontramos una solución, la devolvemos
                return resultado

    return None  # Si no hay solución, devolvemos None

# ============================================
# EJEMPLO: PROBLEMA DEL SUDOKU
# ============================================
# Tablero inicial (0 representa una celda vacía)
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

# Inicializamos los dominios
dominios = {(fila, columna): {tablero[fila][columna]} if tablero[fila][columna] != 0 else set(range(1, 10))
            for fila in range(9) for columna in range(9)}

# Obtenemos las restricciones
restricciones = obtener_restricciones()

# Resolvemos el Sudoku
solucion = resolver_sudoku(tablero, dominios, restricciones)

# Mostramos el resultado
if solucion:
    print("Sudoku resuelto:")
    for fila in range(9):
        print([solucion[(fila, columna)] for columna in range(9)])
else:
    print("No se encontró solución.")