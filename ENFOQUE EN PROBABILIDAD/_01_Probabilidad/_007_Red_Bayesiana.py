# ============================================
# RED BAYESIANA: RAZONAMIENTO PROBABILÍSTICO
# ============================================

# DESCRIPCIÓN TEÓRICA:
# Una **Red Bayesiana** es un modelo probabilístico que representa un conjunto de variables aleatorias
# y sus dependencias condicionales mediante un grafo dirigido acíclico (DAG).
#
# Componentes principales:
# 1. **Nodos:** Representan las variables aleatorias.
# 2. **Arcos:** Representan dependencias condicionales entre las variables.
# 3. **Tablas de Probabilidad Condicional (CPT):** Especifican las probabilidades condicionales de cada nodo
#    dado sus padres en el grafo.
#
# EJEMPLO:
# Supongamos que queremos modelar una red bayesiana para diagnosticar si un paciente tiene gripe (G) basado en
# dos síntomas: fiebre (F) y tos (T). La estructura de la red es:
# - G → F
# - G → T
# Esto significa que fiebre y tos dependen condicionalmente de la presencia de gripe.

# ============================================
# FUNCIÓN PARA CALCULAR PROBABILIDADES EN UNA RED BAYESIANA
# ============================================
def calcular_probabilidad_red_bayesiana(evidencia, red_bayesiana):
    """
    Calcula la probabilidad conjunta de una evidencia en una red bayesiana.
    :param evidencia: Diccionario con los valores observados de las variables.
    :param red_bayesiana: Diccionario que representa la red bayesiana.
                          Cada clave es una variable, y su valor es un diccionario con:
                          - "Padres": Lista de variables padres.
                          - "CPT": Tabla de Probabilidad Condicional.
    :return: Probabilidad conjunta de la evidencia.
    """
    probabilidad_conjunta = 1.0  # Inicializamos la probabilidad conjunta

    # Iteramos sobre cada variable en la red bayesiana
    for variable, datos in red_bayesiana.items():
        padres = datos["Padres"]  # Obtenemos los padres de la variable
        cpt = datos["CPT"]  # Obtenemos la tabla de probabilidad condicional

        # Construimos la clave para buscar en la CPT
        if padres:
            clave = tuple(evidencia[p] for p in padres)
        else:
            clave = ()  # Si no hay padres, usamos una clave vacía

        # Multiplicamos la probabilidad correspondiente de la CPT
        probabilidad_conjunta *= cpt[clave][evidencia[variable]]

    return probabilidad_conjunta

# ============================================
# EJEMPLO: RED BAYESIANA PARA DIAGNÓSTICO MÉDICO
# ============================================
# Definimos la red bayesiana
red_bayesiana = {
    "Gripe": {
        "Padres": [],
        "CPT": {
            (): {True: 0.1, False: 0.9}  # P(Gripe)
        }
    },
    "Fiebre": {
        "Padres": ["Gripe"],
        "CPT": {
            (True,): {True: 0.8, False: 0.2},  # P(Fiebre | Gripe)
            (False,): {True: 0.3, False: 0.7}  # P(Fiebre | ¬Gripe)
        }
    },
    "Tos": {
        "Padres": ["Gripe"],
        "CPT": {
            (True,): {True: 0.7, False: 0.3},  # P(Tos | Gripe)
            (False,): {True: 0.4, False: 0.6}  # P(Tos | ¬Gripe)
        }
    }
}

# Definimos la evidencia
evidencia = {
    "Gripe": True,
    "Fiebre": True,
    "Tos": True
}

# Calculamos la probabilidad conjunta de la evidencia
probabilidad = calcular_probabilidad_red_bayesiana(evidencia, red_bayesiana)

# Mostramos el resultado
print("Probabilidad conjunta de la evidencia:")
print(f"P(Gripe=True, Fiebre=True, Tos=True) = {probabilidad:.4f}")
# Por qué: Mostramos la probabilidad conjunta para interpretar el resultado.
# Para qué: Esto ayuda a entender cómo las dependencias condicionales afectan la probabilidad conjunta.

# ============================================
# INTERPRETACIÓN DEL RESULTADO
# ============================================
# En este ejemplo, la probabilidad conjunta de que el paciente tenga gripe, fiebre y tos se calcula
# utilizando las dependencias condicionales especificadas en la red bayesiana. Esto ilustra cómo
# las redes bayesianas combinan probabilidades condicionales para razonar sobre incertidumbre.