# ============================================
# PROBLEMAS DE SATISFACCIÓN DE RESTRICCIONES (CSP)
# ============================================

# DESCRIPCIÓN TEÓRICA:
# Un Problema de Satisfacción de Restricciones (CSP) consiste en encontrar valores para un conjunto de variables
# que satisfagan un conjunto de restricciones. Cada variable tiene un dominio de valores posibles, y las restricciones
# definen las condiciones que deben cumplirse entre las variables.
# 
# CARACTERÍSTICAS:
# - Variables: Conjunto de elementos que deben ser asignados (por ejemplo, colores, números, etc.).
# - Dominios: Conjunto de valores posibles para cada variable.
# - Restricciones: Condiciones que deben cumplirse entre las variables.
# 
# EJEMPLO:
# Resolver el problema de colorear un mapa donde:
# - Cada región debe tener un color.
# - Regiones adyacentes no pueden tener el mismo color.
# 
# MÉTODO:
# Este algoritmo utiliza **Backtracking** para explorar todas las posibles asignaciones de valores a las variables.
# Si una asignación no cumple las restricciones, retrocede (backtrack) y prueba otra asignación.

# ============================================
# FUNCIÓN PARA VERIFICAR LAS RESTRICCIONES
# ============================================
def es_valido(asignacion, variable, valor, restricciones):
    """
    Verifica si asignar un valor a una variable cumple con las restricciones.
    :param asignacion: Diccionario con las variables ya asignadas.
    :param variable: Variable que se está asignando.
    :param valor: Valor que se está asignando a la variable.
    :param restricciones: Diccionario con las restricciones entre variables.
    :return: True si la asignación es válida, False en caso contrario.
    """
    for vecina in restricciones.get(variable, []):  # Iteramos sobre las variables relacionadas con la actual
        if vecina in asignacion and asignacion[vecina] == valor:  # Si una vecina ya tiene el mismo valor, no es válido
            return False
    return True  # Si no hay conflictos, la asignación es válida

# ============================================
# FUNCIÓN PRINCIPAL DE BACKTRACKING
# ============================================
def backtracking(asignacion, variables, dominios, restricciones):
    """
    Implementa el algoritmo de Backtracking para resolver el CSP.
    :param asignacion: Diccionario con las variables ya asignadas.
    :param variables: Lista de variables a asignar.
    :param dominios: Diccionario con los dominios de cada variable.
    :param restricciones: Diccionario con las restricciones entre variables.
    :return: Una asignación completa que satisface las restricciones, o None si no hay solución.
    """
    if len(asignacion) == len(variables):  # Si todas las variables están asignadas, devolvemos la solución
        return asignacion

    # Seleccionamos la siguiente variable a asignar
    for variable in variables:
        if variable not in asignacion:  # Buscamos una variable no asignada
            break

    # Probamos cada valor en el dominio de la variable
    for valor in dominios[variable]:
        if es_valido(asignacion, variable, valor, restricciones):  # Verificamos si el valor cumple las restricciones
            asignacion[variable] = valor  # Asignamos el valor a la variable
            resultado = backtracking(asignacion, variables, dominios, restricciones)  # Llamada recursiva
            if resultado is not None:  # Si encontramos una solución, la devolvemos
                return resultado
            del asignacion[variable]  # Si no es solución, eliminamos la asignación (backtrack)

    return None  # Si no hay solución, devolvemos None

# ============================================
# EJEMPLO: PROBLEMA DE COLOREADO DE MAPAS
# ============================================
# Variables: Regiones del mapa
variables = ["A", "B", "C", "D", "E"]

# Dominios: Colores disponibles para cada región
dominios = {
    "A": ["Rojo", "Verde", "Azul"],
    "B": ["Rojo", "Verde", "Azul"],
    "C": ["Rojo", "Verde", "Azul"],
    "D": ["Rojo", "Verde", "Azul"],
    "E": ["Rojo", "Verde", "Azul"],
}

# Restricciones: Regiones adyacentes no pueden tener el mismo color
restricciones = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E"],
    "E": ["C", "D"],
}

# ============================================
# EJECUCIÓN DEL ALGORITMO
# ============================================
# Llamamos al algoritmo de Backtracking para resolver el problema
solucion = backtracking({}, variables, dominios, restricciones)

# Mostramos el resultado
if solucion:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró solución.")