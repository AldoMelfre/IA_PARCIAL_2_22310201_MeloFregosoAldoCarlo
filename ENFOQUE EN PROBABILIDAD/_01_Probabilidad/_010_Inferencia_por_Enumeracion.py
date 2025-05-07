# ============================================
# INFERENCIA POR ENUMERACIÓN EN REDES BAYESIANAS
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La inferencia por enumeración es un método para calcular la probabilidad de una variable en una red bayesiana,
# dado un conjunto de evidencias. Este método utiliza la regla de Bayes y la propiedad de independencia condicional
# para calcular las probabilidades marginales.

# Pasos principales:
# 1. Identificar las variables relevantes en la red.
# 2. Expandir las probabilidades condicionales según la estructura de la red.
# 3. Sumar sobre las variables ocultas (no observadas) para obtener la probabilidad deseada.

# ============================================
# FUNCIÓN PARA INFERENCIA POR ENUMERACIÓN
# ============================================
def inferencia_por_enumeracion(variable, evidencia, red_bayesiana):
    """
    Realiza inferencia por enumeración para calcular la probabilidad de una variable dada la evidencia.
    :param variable: La variable de interés (por ejemplo, "A").
    :param evidencia: Diccionario con las variables observadas y sus valores (por ejemplo, {"B": True}).
    :param red_bayesiana: Diccionario que representa la red bayesiana.
                          Cada clave es una variable, y su valor es un diccionario con:
                          - "Padres": Lista de variables padres.
                          - "CPT": Tabla de probabilidad condicional (diccionario).
    :return: Probabilidad normalizada de la variable dada la evidencia.
    """
    # Paso 1: Inicializar un diccionario para almacenar las probabilidades
    distribucion = {}

    # Paso 2: Calcular la probabilidad para cada valor posible de la variable
    for valor in [True, False]:  # Asumimos que las variables son binarias (True/False)
        # Actualizamos la evidencia con el valor actual de la variable
        evidencia[variable] = valor

        # Llamamos a la función recursiva para calcular la probabilidad
        distribucion[valor] = enumerar_todas(red_bayesiana, list(red_bayesiana.keys()), evidencia)

    # Paso 3: Normalizar la distribución para que las probabilidades sumen 1
    total = sum(distribucion.values())
    for valor in distribucion:
        distribucion[valor] /= total

    # Retornamos la distribución normalizada
    return distribucion

# ============================================
# FUNCIÓN RECURSIVA PARA ENUMERAR TODAS LAS VARIABLES
# ============================================
def enumerar_todas(red_bayesiana, variables, evidencia):
    """
    Calcula la probabilidad total mediante enumeración recursiva.
    :param red_bayesiana: La red bayesiana.
    :param variables: Lista de variables a considerar.
    :param evidencia: Diccionario con las variables observadas y sus valores.
    :return: Probabilidad total.
    """
    # Caso base: Si no hay más variables, retornamos 1
    if not variables:
        return 1.0

    # Tomamos la primera variable de la lista
    primera = variables[0]
    resto = variables[1:]

    # Si la variable está en la evidencia, usamos su valor
    if primera in evidencia:
        prob = probabilidad_condicional(primera, evidencia[primera], evidencia, red_bayesiana)
        return prob * enumerar_todas(red_bayesiana, resto, evidencia)
    else:
        # Si la variable no está en la evidencia, sumamos sobre todos sus valores posibles
        suma = 0
        for valor in [True, False]:  # Asumimos que las variables son binarias
            evidencia[primera] = valor
            prob = probabilidad_condicional(primera, valor, evidencia, red_bayesiana)
            suma += prob * enumerar_todas(red_bayesiana, resto, evidencia)
        del evidencia[primera]  # Limpiamos la evidencia temporal
        return suma

# ============================================
# FUNCIÓN PARA CALCULAR LA PROBABILIDAD CONDICIONAL
# ============================================
def probabilidad_condicional(variable, valor, evidencia, red_bayesiana):
    """
    Calcula la probabilidad condicional de una variable dado su evidencia.
    :param variable: La variable de interés.
    :param valor: El valor de la variable (True/False).
    :param evidencia: Diccionario con las variables observadas y sus valores.
    :param red_bayesiana: La red bayesiana.
    :return: Probabilidad condicional.
    """
    # Obtenemos los padres de la variable
    padres = red_bayesiana[variable]["Padres"]

    # Construimos una clave para buscar en la tabla de probabilidad condicional (CPT)
    clave = tuple(evidencia[p] for p in padres)

    # Retornamos la probabilidad correspondiente de la CPT
    if valor:
        return red_bayesiana[variable]["CPT"][clave]
    else:
        return 1 - red_bayesiana[variable]["CPT"][clave]

# ============================================
# EJEMPLO: RED BAYESIANA SIMPLE
# ============================================
# Definimos una red bayesiana con tablas de probabilidad condicional (CPT)
red_bayesiana = {
    "A": {
        "Padres": [],
        "CPT": {(): 0.2}  # Probabilidad de A=True es 0.2
    },
    "B": {
        "Padres": ["A"],
        "CPT": {(True,): 0.8, (False,): 0.5}  # Probabilidad de B=True dado A
    },
    "C": {
        "Padres": ["B"],
        "CPT": {(True,): 0.7, (False,): 0.1}  # Probabilidad de C=True dado B
    }
}

# Evidencia: Sabemos que C=True
evidencia = {"C": True}

# Calculamos la probabilidad de A dado la evidencia
resultado = inferencia_por_enumeracion("A", evidencia, red_bayesiana)

# Mostramos el resultado
print("Distribución de probabilidad de A dado C=True:")
print(resultado)