import random  # Importa el módulo random para generar números aleatorios

# ============================================
# MUETREO DIRECTO EN REDES BAYESIANAS
# ============================================
def muestreo_directo(red_bayesiana, num_muestras):
    """
    Realiza muestreo directo para generar muestras de una red bayesiana.
    :param red_bayesiana: Diccionario que representa la red bayesiana.
    :param num_muestras: Número de muestras a generar.
    :return: Lista de muestras generadas.
    """
    # Lista para almacenar las muestras generadas
    muestras = []

    # Obtener el orden topológico de las variables (orden en el que deben ser evaluadas)
    variables = list(red_bayesiana.keys())

    # Generar las muestras
    for _ in range(num_muestras):  # Itera num_muestras veces para generar las muestras
        muestra = {}  # Diccionario para almacenar los valores de las variables en esta muestra

        # Iterar sobre las variables en orden topológico
        for variable in variables:
            padres = red_bayesiana[variable]["Padres"]  # Obtener los padres de la variable
            cpt = red_bayesiana[variable]["CPT"]  # Obtener la tabla de probabilidad condicional (CPT)

            # Obtener los valores de los padres en la muestra actual
            valores_padres = tuple(muestra[p] for p in padres)

            # Generar un valor para la variable basado en la CPT
            prob = cpt[valores_padres]  # Probabilidad de que la variable sea True dado los valores de los padres
            muestra[variable] = random.random() < prob  # True si el número aleatorio es menor que la probabilidad
        muestras.append(muestra)  # Agregar la muestra generada a la lista

    return muestras  # Devuelve la lista de muestras generadas

# ============================================
# MUETREO POR RECHAZO EN REDES BAYESIANAS
# ============================================
def muestreo_por_rechazo(red_bayesiana, evidencia, num_muestras):
    """
    Realiza muestreo por rechazo para calcular probabilidades condicionales en una red bayesiana.
    :param red_bayesiana: Diccionario que representa la red bayesiana.
    :param evidencia: Diccionario con las variables observadas y sus valores.
    :param num_muestras: Número de muestras a generar.
    :return: Lista de muestras que coinciden con la evidencia.
    """
    # Generar muestras usando muestreo directo
    muestras = muestreo_directo(red_bayesiana, num_muestras)

    # Filtrar las muestras que coinciden con la evidencia
    muestras_compatibles = []
    for muestra in muestras:  # Itera sobre cada muestra generada
        # Verificar si la muestra es compatible con la evidencia
        if all(muestra[var] == valor for var, valor in evidencia.items()):  # Comprueba si todas las variables de la evidencia coinciden
            muestras_compatibles.append(muestra)  # Agregar la muestra compatible

    return muestras_compatibles  # Devuelve las muestras compatibles con la evidencia

# ============================================
# FUNCIÓN PARA CALCULAR DISTRIBUCIÓN CONDICIONAL
# ============================================
def calcular_distribucion_condicional(muestras, variable):
    """
    Calcula la distribución condicional de una variable a partir de las muestras.
    :param muestras: Lista de muestras compatibles con la evidencia.
    :param variable: La variable de interés.
    :return: Distribución condicional de la variable.
    """
    # Contar las ocurrencias de True y False para la variable
    conteo = {True: 0, False: 0}  # Inicializa un contador para True y False
    for muestra in muestras:  # Itera sobre cada muestra
        conteo[muestra[variable]] += 1  # Incrementa el contador según el valor de la variable

    # Normalizar los conteos para obtener probabilidades
    total = sum(conteo.values())  # Suma el total de ocurrencias
    distribucion = {valor: conteo[valor] / total for valor in conteo}  # Calcula la probabilidad de cada valor

    return distribucion  # Devuelve la distribución condicional

# ============================================
# EJEMPLO: RED BAYESIANA SIMPLE
# ============================================
# Definimos una red bayesiana simple
red_bayesiana = {
    "A": {
        "Padres": [],  # La variable A no tiene padres
        "CPT": {(): 0.2}  # Probabilidad de A=True es 0.2
    },
    "B": {
        "Padres": ["A"],  # La variable B depende de A
        "CPT": {(True,): 0.8, (False,): 0.5}  # Probabilidad de B=True dado A
    },
    "C": {
        "Padres": ["B"],  # La variable C depende de B
        "CPT": {(True,): 0.7, (False,): 0.1}  # Probabilidad de C=True dado B
    }
}

# ============================================
# EJEMPLO: MUETREO DIRECTO
# ============================================
print("=== Muestreo Directo ===")
num_muestras = 1000  # Número de muestras a generar
muestras = muestreo_directo(red_bayesiana, num_muestras)  # Genera muestras usando muestreo directo
print(f"Se generaron {len(muestras)} muestras.")  # Imprime el número de muestras generadas
print("Primeras 5 muestras:")
print(muestras[:5])  # Muestra las primeras 5 muestras generadas

# ============================================
# EJEMPLO: MUETREO POR RECHAZO
# ============================================
print("\n=== Muestreo por Rechazo ===")
evidencia = {"C": True}  # Evidencia observada: C=True
muestras_compatibles = muestreo_por_rechazo(red_bayesiana, evidencia, num_muestras)  # Filtra muestras compatibles con la evidencia
print(f"Se generaron {len(muestras_compatibles)} muestras compatibles con la evidencia {evidencia}.")  # Imprime el número de muestras compatibles

# Calcular la distribución condicional de A dado C=True
distribucion = calcular_distribucion_condicional(muestras_compatibles, "A")  # Calcula la distribución condicional de A
print(f"Distribución condicional de A dado C=True: {distribucion}")  # Imprime la distribución condicional