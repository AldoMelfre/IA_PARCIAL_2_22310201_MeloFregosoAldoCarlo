# ============================================
# COMPROBACIÓN HACIA ADELANTE (FORWARD CHECKING)
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La comprobación hacia adelante es una técnica utilizada en problemas de satisfacción de restricciones (CSP).
# Este enfoque reduce el dominio de las variables no asignadas cada vez que se realiza una asignación.
# Si una asignación deja sin valores posibles a una variable no asignada, se retrocede inmediatamente.
# 
# CARACTERÍSTICAS:
# - Variables: Elementos que deben ser asignados (por ejemplo, colores, números, etc.).
# - Dominios: Conjunto de valores posibles para cada variable.
# - Restricciones: Condiciones que deben cumplirse entre las variables.
# 
# EJEMPLO:
# Resolver el problema de colorear un mapa donde:
# - Cada región debe tener un color.
# - Regiones adyacentes no pueden tener el mismo color.

# ============================================
# FUNCIÓN PARA VERIFICAR LAS RESTRICCIONES
# ============================================
def es_valido(variable, valor, asignacion, restricciones):
    """
    Verifica si asignar un valor a una variable cumple con las restricciones.
    :param variable: Variable que se está asignando.
    :param valor: Valor que se está asignando a la variable.
    :param asignacion: Diccionario con las variables ya asignadas.
    :param restricciones: Diccionario con las restricciones entre variables.
    :return: True si la asignación es válida, False en caso contrario.
    """
    for vecina in restricciones.get(variable, []):  # Iteramos sobre las variables relacionadas con la actual
        if vecina in asignacion and asignacion[vecina] == valor:  # Si una vecina ya tiene el mismo valor, no es válido
            return False
    return True  # Si no hay conflictos, la asignación es válida

# ============================================
# FUNCIÓN PARA REDUCIR EL DOMINIO (FORWARD CHECKING)
# ============================================
def reducir_dominio(variable, valor, dominios, restricciones):
    """
    Reduce el dominio de las variables no asignadas basándose en la asignación actual.
    :param variable: Variable que se está asignando.
    :param valor: Valor asignado a la variable.
    :param dominios: Diccionario con los dominios de cada variable.
    :param restricciones: Diccionario con las restricciones entre variables.
    :return: Diccionario con los dominios reducidos, o None si algún dominio queda vacío.
    """
    dominios_reducidos = {var: list(dom) for var, dom in dominios.items()}  # Copiamos los dominios
    for vecina in restricciones.get(variable, []):  # Iteramos sobre las variables relacionadas con la actual
        if valor in dominios_reducidos[vecina]:  # Si el valor asignado está en el dominio de la vecina
            dominios_reducidos[vecina].remove(valor)  # Lo eliminamos del dominio
            if not dominios_reducidos[vecina]:  # Si el dominio queda vacío, no es válido
                return None
    return dominios_reducidos  # Devolvemos los dominios reducidos

# ============================================
# FUNCIÓN PRINCIPAL DE FORWARD CHECKING
# ============================================
def forward_checking(asignacion, variables, dominios, restricciones):
    """
    Implementa el algoritmo de Forward Checking para resolver el CSP.
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
        if es_valido(variable, valor, asignacion, restricciones):  # Verificamos si el valor cumple las restricciones
            asignacion[variable] = valor  # Asignamos el valor a la variable
            dominios_reducidos = reducir_dominio(variable, valor, dominios, restricciones)  # Reducimos el dominio
            if dominios_reducidos is not None:  # Si los dominios son válidos
                resultado = forward_checking(asignacion, variables, dominios_reducidos, restricciones)  # Llamada recursiva
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
# Llamamos al algoritmo de Forward Checking para resolver el problema
solucion = forward_checking({}, variables, dominios, restricciones)

# Mostramos el resultado
if solucion:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró solución.")