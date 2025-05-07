# ============================================
# ELIMINACIÓN DE VARIABLES EN REDES BAYESIANAS
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La eliminación de variables es un método eficiente para calcular la probabilidad de una variable en una red bayesiana,
# dado un conjunto de evidencias. Este método reduce el espacio de búsqueda al eliminar variables ocultas (no observadas)
# de manera sistemática, utilizando la suma marginal y la multiplicación de factores.

# ============================================
# FUNCIÓN PARA ELIMINACIÓN DE VARIABLES
# ============================================
def eliminacion_de_variables(variable, evidencia, red_bayesiana):
    """
    Realiza inferencia mediante eliminación de variables para calcular la probabilidad de una variable dada la evidencia.
    :param variable: La variable de interés (por ejemplo, "A").
    :param evidencia: Diccionario con las variables observadas y sus valores (por ejemplo, {"B": True}).
    :param red_bayesiana: Diccionario que representa la estructura de la red bayesiana y sus probabilidades condicionales.
    :return: Probabilidad de la variable de interés dada la evidencia.
    """
    # Paso 1: Convertir las probabilidades condicionales en factores
    factores = crear_factores(red_bayesiana, evidencia)

    # Paso 2: Identificar las variables ocultas (no observadas y no de interés)
    variables_ocultas = [v for v in red_bayesiana if v != variable and v not in evidencia]

    # Paso 3: Eliminar las variables ocultas una por una
    for var in variables_ocultas:
        factores = eliminar_variable(var, factores)

    # Paso 4: Multiplicar los factores restantes
    resultado = multiplicar_factores(factores)

    # Paso 5: Normalizar el resultado para obtener una distribución de probabilidad
    return normalizar(resultado)

# ============================================
# FUNCIÓN PARA CREAR FACTORES
# ============================================
def crear_factores(red_bayesiana, evidencia):
    """
    Convierte las probabilidades condicionales de la red bayesiana en factores, aplicando la evidencia.
    :param red_bayesiana: La red bayesiana.
    :param evidencia: Diccionario con las variables observadas y sus valores.
    :return: Lista de factores.
    """
    factores = []
    for variable, datos in red_bayesiana.items():
        cpt = datos["CPT"]
        padres = datos["Padres"]

        # Si la variable tiene evidencia, reducimos el factor
        if variable in evidencia:
            nuevo_cpt = {}
            for valores_padres, probabilidad in cpt.items():
                if all(p in evidencia for p in padres):
                    if valores_padres == tuple(evidencia[p] for p in padres):
                        nuevo_cpt[valores_padres] = probabilidad if evidencia[variable] else 1 - probabilidad
            factores.append({"variables": padres, "tabla": nuevo_cpt})
        else:
            factores.append({"variables": [variable] + padres, "tabla": cpt})
    return factores

# ============================================
# FUNCIÓN PARA ELIMINAR UNA VARIABLE
# ============================================
def eliminar_variable(variable, factores):
    """
    Elimina una variable oculta marginalizando sobre ella.
    :param variable: La variable a eliminar.
    :param factores: Lista de factores actuales.
    :return: Nueva lista de factores después de eliminar la variable.
    """
    # Seleccionar los factores que contienen la variable
    factores_relevantes = [f for f in factores if variable in f["variables"]]
    factores_restantes = [f for f in factores if variable not in f["variables"]]

    # Multiplicar los factores relevantes
    nuevo_factor = multiplicar_factores(factores_relevantes)

    # Marginalizar sobre la variable
    nuevo_factor = marginalizar(nuevo_factor, variable)

    # Agregar el nuevo factor a los factores restantes
    factores_restantes.append(nuevo_factor)
    return factores_restantes

# ============================================
# FUNCIÓN PARA MULTIPLICAR FACTORES
# ============================================
def multiplicar_factores(factores):
    """
    Multiplica una lista de factores.
    :param factores: Lista de factores a multiplicar.
    :return: Un único factor resultante de la multiplicación.
    """
    # Inicializamos con el primer factor
    resultado = factores[0]
    for factor in factores[1:]:
        resultado = multiplicar_dos_factores(resultado, factor)
    return resultado

def multiplicar_dos_factores(f1, f2):
    """
    Multiplica dos factores.
    :param f1: Primer factor.
    :param f2: Segundo factor.
    :return: Factor resultante.
    """
    variables_comunes = list(set(f1["variables"]) & set(f2["variables"]))
    todas_las_variables = list(set(f1["variables"]) | set(f2["variables"]))

    nueva_tabla = {}
    for valores_f1, prob_f1 in f1["tabla"].items():
        for valores_f2, prob_f2 in f2["tabla"].items():
            if all(valores_f1[f1["variables"].index(var)] == valores_f2[f2["variables"].index(var)] for var in variables_comunes):
                nuevo_valor = tuple(
                    valores_f1[f1["variables"].index(var)] if var in f1["variables"] else valores_f2[f2["variables"].index(var)]
                    for var in todas_las_variables
                )
                nueva_tabla[nuevo_valor] = prob_f1 * prob_f2
    return {"variables": todas_las_variables, "tabla": nueva_tabla}

# ============================================
# FUNCIÓN PARA MARGINALIZAR UNA VARIABLE
# ============================================
def marginalizar(factor, variable):
    """
    Marginaliza un factor sobre una variable.
    :param factor: El factor a marginalizar.
    :param variable: La variable a eliminar.
    :return: Nuevo factor marginalizado.
    """
    indice = factor["variables"].index(variable)
    nuevas_variables = [v for v in factor["variables"] if v != variable]

    nueva_tabla = {}
    for valores, probabilidad in factor["tabla"].items():
        nuevo_valor = tuple(v for i, v in enumerate(valores) if i != indice)
        if nuevo_valor in nueva_tabla:
            nueva_tabla[nuevo_valor] += probabilidad
        else:
            nueva_tabla[nuevo_valor] = probabilidad
    return {"variables": nuevas_variables, "tabla": nueva_tabla}

# ============================================
# FUNCIÓN PARA NORMALIZAR UNA DISTRIBUCIÓN
# ============================================
def normalizar(factor):
    """
    Normaliza un factor para que las probabilidades sumen 1.
    :param factor: El factor a normalizar.
    :return: Factor normalizado.
    """
    total = sum(factor["tabla"].values())
    for clave in factor["tabla"]:
        factor["tabla"][clave] /= total
    return factor

# ============================================
# EJEMPLO: RED BAYESIANA SIMPLE
# ============================================
red_bayesiana = {
    "A": {
        "Padres": [],
        "CPT": {(): 0.2}
    },
    "B": {
        "Padres": ["A"],
        "CPT": {(True,): 0.8, (False,): 0.5}
    },
    "C": {
        "Padres": ["B"],
        "CPT": {(True,): 0.7, (False,): 0.1}
    }
}

evidencia = {"C": True}
resultado = eliminacion_de_variables("A", evidencia, red_bayesiana)
print("Distribución de probabilidad de A dado C=True:")
print(resultado)