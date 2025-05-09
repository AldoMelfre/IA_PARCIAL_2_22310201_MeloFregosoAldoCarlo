import random

# ============================================
# PONDERACIÓN DE VEROSIMILITUD EN REDES BAYESIANAS
# ============================================
def ponderacion_de_verosimilitud(red_bayesiana, evidencia, num_muestras):
    """
    Realiza ponderación de verosimilitud para calcular probabilidades condicionales en una red bayesiana.
    :param red_bayesiana: Diccionario que representa la red bayesiana.
    :param evidencia: Diccionario con las variables observadas y sus valores.
    :param num_muestras: Número de muestras a generar.
    :return: Lista de muestras con sus pesos.
    """
    muestras_ponderadas = []

    for _ in range(num_muestras):
        muestra = {}
        peso = 1.0  # Inicializamos el peso de la muestra en 1

        # Generar la muestra siguiendo el orden topológico de las variables
        for variable in red_bayesiana:
            padres = red_bayesiana[variable]["Padres"]
            cpt = red_bayesiana[variable]["CPT"]

            # Obtener los valores de los padres en la muestra actual
            valores_padres = tuple(muestra[p] for p in padres)

            if variable in evidencia:
                # Si la variable está en la evidencia, ajustamos el peso
                prob = cpt[valores_padres]
                peso *= prob if evidencia[variable] else (1 - prob)
                muestra[variable] = evidencia[variable]  # Fijamos el valor de la variable según la evidencia
            else:
                # Si la variable no está en la evidencia, generamos un valor aleatorio
                prob = cpt[valores_padres]
                muestra[variable] = random.random() < prob

        # Agregar la muestra y su peso a la lista
        muestras_ponderadas.append((muestra, peso))

    return muestras_ponderadas

# ============================================
# FUNCIÓN PARA CALCULAR DISTRIBUCIÓN CONDICIONAL
# ============================================
def calcular_distribucion_ponderada(muestras_ponderadas, variable):
    """
    Calcula la distribución condicional de una variable a partir de muestras ponderadas.
    :param muestras_ponderadas: Lista de muestras con sus pesos.
    :param variable: La variable de interés.
    :return: Distribución condicional de la variable.
    """
    conteo_ponderado = {True: 0, False: 0}

    for muestra, peso in muestras_ponderadas:
        conteo_ponderado[muestra[variable]] += peso

    # Normalizar los conteos ponderados para obtener probabilidades
    total = sum(conteo_ponderado.values())
    distribucion = {valor: conteo_ponderado[valor] / total for valor in conteo_ponderado}

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
# EJEMPLO: PONDERACIÓN DE VEROSIMILITUD
# ============================================
print("\n=== Ponderación de Verosimilitud ===")
evidencia = {"C": True}
num_muestras = 1000

# Generar muestras ponderadas
muestras_ponderadas = ponderacion_de_verosimilitud(red_bayesiana, evidencia, num_muestras)
print(f"Se generaron {len(muestras_ponderadas)} muestras ponderadas.")

# Calcular la distribución condicional de A dado C=True
distribucion = calcular_distribucion_ponderada(muestras_ponderadas, "A")
print(f"Distribución condicional de A dado C=True: {distribucion}")