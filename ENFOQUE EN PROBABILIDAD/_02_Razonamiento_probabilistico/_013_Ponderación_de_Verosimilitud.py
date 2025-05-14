"""
Descripción teórica:
La ponderación de verosimilitud es un método de muestreo utilizado en redes bayesianas para calcular probabilidades condicionales. 
Este enfoque genera muestras ponderadas basadas en la evidencia observada y las relaciones de probabilidad entre las variables de la red. 
El peso de cada muestra refleja cuán consistente es con la evidencia proporcionada. 
El algoritmo sigue el orden topológico de las variables en la red, asegurando que las dependencias entre variables se respeten al generar las muestras.

Parámetros:
- red_bayesiana: Representa la estructura de la red bayesiana, donde cada variable tiene padres y una tabla de probabilidad condicional (CPT).
- evidencia: Contiene las variables observadas y sus valores (True/False).
- num_muestras: Número de muestras que se generarán.

Salida:
- Una lista de tuplas, donde cada tupla contiene una muestra generada y su peso asociado.
"""

import random  # Importamos el módulo random para generar números aleatorios

def ponderacion_de_verosimilitud(red_bayesiana, evidencia, num_muestras):
    """
    Realiza ponderación de verosimilitud para calcular probabilidades condicionales en una red bayesiana.
    :param red_bayesiana: Diccionario que representa la red bayesiana.
    :param evidencia: Diccionario con las variables observadas y sus valores.
    :param num_muestras: Número de muestras a generar.
    :return: Lista de muestras con sus pesos.
    """
    muestras_ponderadas = []  # Lista para almacenar las muestras generadas junto con sus pesos

    for _ in range(num_muestras):  # Iteramos para generar el número de muestras especificado
        muestra = {}  # Diccionario para almacenar los valores de las variables en la muestra actual
        peso = 1.0  # Inicializamos el peso de la muestra en 1 (neutro)

        # Generar la muestra siguiendo el orden topológico de las variables
        for variable in red_bayesiana:  # Iteramos sobre cada variable en la red bayesiana
            padres = red_bayesiana[variable]["Padres"]  # Obtenemos los padres de la variable actual
            cpt = red_bayesiana[variable]["CPT"]  # Obtenemos la tabla de probabilidad condicional (CPT) de la variable

            # Obtener los valores de los padres en la muestra actual
            valores_padres = tuple(muestra[p] for p in padres)  # Creamos una tupla con los valores de los padres

            if variable in evidencia:  # Si la variable está en la evidencia proporcionada
                prob = cpt[valores_padres]  # Obtenemos la probabilidad de la variable dado los valores de sus padres
                # Ajustamos el peso de la muestra según la consistencia con la evidencia
                peso *= prob if evidencia[variable] else (1 - prob)
                muestra[variable] = evidencia[variable]  # Fijamos el valor de la variable según la evidencia
            else:  # Si la variable no está en la evidencia
                prob = cpt[valores_padres]  # Obtenemos la probabilidad de la variable dado los valores de sus padres
                # Generamos un valor aleatorio para la variable basado en su probabilidad
                muestra[variable] = random.random() < prob

        # Agregar la muestra y su peso a la lista de resultados
        muestras_ponderadas.append((muestra, peso))

    return muestras_ponderadas  # Devolvemos la lista de muestras con sus pesos

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