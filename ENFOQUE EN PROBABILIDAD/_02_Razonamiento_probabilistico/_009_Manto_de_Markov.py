# ============================================
# MANTO DE MARKOV: INDEPENDENCIA EN REDES BAYESIANAS
# ============================================

# DESCRIPCIÓN TEÓRICA:
# El **Manto de Markov** de una variable en una red bayesiana es el conjunto mínimo de variables que,
# si se conocen, hacen que la variable sea independiente del resto de las variables en la red.
#
# Para una variable X, su Manto de Markov incluye:
# 1. Sus padres (variables de las que depende directamente).
# 2. Sus hijos (variables que dependen directamente de X).
# 3. Los otros padres de sus hijos (variables que afectan a los hijos de X).
#
# Propiedad clave:
# Dado el Manto de Markov de X, la variable X es condicionalmente independiente del resto de las variables.
#
# EJEMPLO:
# Supongamos una red bayesiana con las siguientes relaciones:
# - A → B → C
# - B → D
# El Manto de Markov de B incluye: {A, C, D}.

# ============================================
# FUNCIÓN PARA CALCULAR EL MANTO DE MARKOV
# ============================================
def calcular_manto_de_markov(variable, red_bayesiana):
    """
    Calcula el Manto de Markov de una variable en una red bayesiana.
    :param variable: La variable para la que se calculará el Manto de Markov.
    :param red_bayesiana: Diccionario que representa la red bayesiana.
                          Cada clave es una variable, y su valor es un diccionario con:
                          - "Padres": Lista de variables padres.
                          - "Hijos": Lista de variables hijos.
    :return: Conjunto con las variables que forman el Manto de Markov.
    """
    manto = set()  # Inicializamos el Manto de Markov como un conjunto vacío

    # Agregamos los padres de la variable
    # Por qué: Los padres afectan directamente a la variable.
    # Para qué: Esto asegura que consideremos las dependencias directas.
    manto.update(red_bayesiana[variable]["Padres"])

    # Agregamos los hijos de la variable
    # Por qué: Los hijos dependen directamente de la variable.
    # Para qué: Esto asegura que consideremos las variables afectadas por la variable.
    manto.update(red_bayesiana[variable]["Hijos"])

    # Agregamos los otros padres de los hijos
    # Por qué: Los otros padres de los hijos también afectan indirectamente a la variable.
    # Para qué: Esto asegura que consideremos todas las dependencias indirectas relevantes.
    for hijo in red_bayesiana[variable]["Hijos"]:
        manto.update(red_bayesiana[hijo]["Padres"])

    # Eliminamos la variable en sí misma del Manto de Markov
    manto.discard(variable)

    return manto

# ============================================
# EJEMPLO: RED BAYESIANA SIMPLE
# ============================================
# Definimos la red bayesiana
red_bayesiana = {
    "A": {"Padres": [], "Hijos": ["B"]},
    "B": {"Padres": ["A"], "Hijos": ["C", "D"]},
    "C": {"Padres": ["B"], "Hijos": []},
    "D": {"Padres": ["B"], "Hijos": []}
}

# Calculamos el Manto de Markov para la variable B
manto_b = calcular_manto_de_markov("B", red_bayesiana)

# Mostramos el resultado
print("Manto de Markov de B:")
print(manto_b)
# Por qué: Mostramos el Manto de Markov para interpretar las dependencias de la variable.
# Para qué: Esto ayuda a entender cómo la variable está conectada con el resto de la red.

# ============================================
# INTERPRETACIÓN DEL RESULTADO
# ============================================
# En este ejemplo, el Manto de Markov de B incluye:
# - A (padre de B).
# - C y D (hijos de B).
# Esto significa que, dado {A, C, D}, la variable B es independiente del resto de las variables en la red.