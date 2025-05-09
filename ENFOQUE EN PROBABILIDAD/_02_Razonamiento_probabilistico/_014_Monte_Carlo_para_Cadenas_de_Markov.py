import random

# ============================================
# MONTE CARLO PARA CADENAS DE MARKOV (MCMC) - MUETREO DE GIBBS
# ============================================

# El Muestreo de Gibbs es un método de simulación basado en cadenas de Markov.
# Se utiliza para generar muestras de una distribución conjunta cuando no es posible calcularla directamente.
# Este método actualiza iterativamente una variable a la vez, condicionada a los valores actuales de las demás variables.

# ============================================
# FUNCIÓN PRINCIPAL: MUETREO DE GIBBS
# ============================================
def muestreo_gibbs(red_bayesiana, evidencia, num_iteraciones):
    """
    Realiza muestreo de Gibbs para generar muestras de una red bayesiana.
    :param red_bayesiana: Diccionario que representa la red bayesiana.
    :param evidencia: Diccionario con las variables observadas y sus valores.
    :param num_iteraciones: Número de iteraciones a realizar.
    :return: Lista de muestras generadas.
    """
    # Inicializar las variables con valores aleatorios
    # Las variables que no están en la evidencia se inicializan aleatoriamente (True o False)
    muestra_actual = {var: (random.random() < 0.5) for var in red_bayesiana if var not in evidencia}
    muestra_actual.update(evidencia)  # Fijar los valores de las variables en la evidencia

    muestras = []  # Lista para almacenar las muestras generadas

    # Iterar para generar muestras
    for _ in range(num_iteraciones):
        for variable in red_bayesiana:
            if variable not in evidencia:  # Solo actualizamos las variables que no están en la evidencia
                # Calcular la distribución condicional de la variable dada la muestra actual
                prob_true = calcular_prob_condicional(variable, True, muestra_actual, red_bayesiana)
                prob_false = calcular_prob_condicional(variable, False, muestra_actual, red_bayesiana)

                # Normalizar las probabilidades
                total = prob_true + prob_false
                prob_true /= total

                # Actualizar el valor de la variable en la muestra actual
                muestra_actual[variable] = random.random() < prob_true

        # Agregar la muestra actual a la lista de muestras
        muestras.append(muestra_actual.copy())

    return muestras

# ============================================
# FUNCIÓN PARA CALCULAR PROBABILIDAD CONDICIONAL
# ============================================
def calcular_prob_condicional(variable, valor, muestra, red_bayesiana):
    """
    Calcula la probabilidad condicional de una variable dado el resto de la muestra.
    :param variable: La variable de interés.
    :param valor: El valor de la variable (True/False).
    :param muestra: La muestra actual.
    :param red_bayesiana: La red bayesiana.
    :return: Probabilidad condicional de la variable.
    """
    # Obtener los padres de la variable y su tabla de probabilidad condicional (CPT)
    padres = red_bayesiana[variable]["Padres"]
    cpt = red_bayesiana[variable]["CPT"]

    # Obtener los valores de los padres en la muestra actual
    valores_padres = tuple(muestra[p] for p in padres)

    # Probabilidad de la variable dado los valores de los padres
    prob = cpt[valores_padres] if valor else 1 - cpt[valores_padres]

    # Multiplicar por las probabilidades condicionales de los hijos
    for hijo, datos_hijo in red_bayesiana.items():
        if variable in datos_hijo["Padres"]:  # Si la variable es un padre de este hijo
            valores_padres_hijo = tuple(muestra[p] if p != variable else valor for p in datos_hijo["Padres"])
            prob *= datos_hijo["CPT"][valores_padres_hijo] if muestra[hijo] else 1 - datos_hijo["CPT"][valores_padres_hijo]

    return prob

# ============================================
# FUNCIÓN PARA CALCULAR DISTRIBUCIÓN CONDICIONAL
# ============================================
def calcular_distribucion_mcmc(muestras, variable):
    """
    Calcula la distribución condicional de una variable a partir de las muestras generadas por MCMC.
    :param muestras: Lista de muestras generadas.
    :param variable: La variable de interés.
    :return: Distribución condicional de la variable.
    """
    # Contar las ocurrencias de True y False para la variable
    conteo = {True: 0, False: 0}

    for muestra in muestras:
        conteo[muestra[variable]] += 1

    # Normalizar los conteos para obtener probabilidades
    total = sum(conteo.values())
    distribucion = {valor: conteo[valor] / total for valor in conteo}

    return distribucion

# ============================================
# EJEMPLO: RED BAYESIANA SIMPLE
# ============================================
# Definimos una red bayesiana simple
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

# ============================================
# EJEMPLO: MUETREO DE GIBBS
# ============================================
print("\n=== Muestreo de Gibbs ===")
evidencia = {"C": True}  # Fijamos la evidencia
num_iteraciones = 1000  # Número de iteraciones

# Generar muestras usando muestreo de Gibbs
muestras = muestreo_gibbs(red_bayesiana, evidencia, num_iteraciones)
print(f"Se generaron {len(muestras)} muestras.")

# Calcular la distribución condicional de A dado C=True
distribucion = calcular_distribucion_mcmc(muestras, "A")
print(f"Distribución condicional de A dado C=True: {distribucion}")