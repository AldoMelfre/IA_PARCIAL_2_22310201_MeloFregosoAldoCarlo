# ============================================
# VALOR DE LA INFORMACIÓN (VOI)
# ============================================

# DESCRIPCIÓN TEÓRICA:
# El Valor de la Información (VOI) mide cuánto vale obtener información adicional antes de tomar una decisión.
# Se calcula como la diferencia entre la utilidad esperada con información perfecta y la utilidad esperada sin información.
# Si el costo de obtener la información es menor que el VOI, entonces es beneficioso obtenerla.
# 
# COMPONENTES:
# - **Utilidad esperada sin información:** Utilidad esperada basada en las probabilidades actuales.
# - **Utilidad esperada con información perfecta:** Utilidad esperada si se conociera el estado del mundo con certeza.
# - **Costo de la información:** Costo asociado a obtener la información adicional.
# 
# EJEMPLO:
# Un agente debe decidir entre dos acciones (A y B) sin información adicional. Luego, puede obtener información
# sobre el estado del mundo (por ejemplo, si el mercado subirá o bajará) y recalcular la utilidad esperada.
# El algoritmo calcula el VOI y determina si vale la pena obtener la información.

# ============================================
# FUNCIÓN PARA CALCULAR LA UTILIDAD ESPERADA
# ============================================
def calcular_utilidad_esperada(probabilidades, utilidades):
    """
    Calcula la utilidad esperada de una decisión.
    :param probabilidades: Lista de probabilidades de los estados.
    :param utilidades: Lista de utilidades asociadas a los estados.
    :return: La utilidad esperada.
    """
    # Inicializamos la utilidad esperada en 0
    utilidad_esperada = 0

    # Iteramos sobre las probabilidades y utilidades
    for p, u in zip(probabilidades, utilidades):
        utilidad_esperada += p * u  # Sumamos el producto de la probabilidad y la utilidad

    return utilidad_esperada  # Devolvemos la utilidad esperada

# ============================================
# FUNCIÓN PARA CALCULAR EL VALOR DE LA INFORMACIÓN
# ============================================
def calcular_valor_de_la_informacion(acciones, estados, costo_informacion=0):
    """
    Calcula el Valor de la Información (VOI) y determina si vale la pena obtenerla.
    :param acciones: Diccionario donde las claves son las acciones y los valores son tuplas
                     (probabilidades, utilidades).
    :param estados: Diccionario donde las claves son los estados y los valores son las probabilidades de cada estado.
    :param costo_informacion: Costo de obtener la información adicional.
    :return: El VOI y si es beneficioso obtener la información.
    """
    # Utilidad esperada sin información
    utilidad_sin_informacion = max(
        calcular_utilidad_esperada(probabilidades, utilidades)
        for probabilidades, utilidades in acciones.values()
    )


    # Utilidad esperada con información perfecta
    utilidad_con_informacion = 0
    for estado, probabilidad_estado in estados.items():
        # Calculamos la mejor utilidad para cada estado
        mejor_utilidad_estado = max(
            utilidades[i] for probabilidades, utilidades in acciones.values()
            for i, p in enumerate(probabilidades) if p == probabilidad_estado
        )
        utilidad_con_informacion += probabilidad_estado * mejor_utilidad_estado

    # Calculamos el VOI
    valor_de_la_informacion = utilidad_con_informacion - utilidad_sin_informacion

    # Determinamos si es beneficioso obtener la información
    es_beneficioso = valor_de_la_informacion > costo_informacion

    return valor_de_la_informacion, es_beneficioso

# ============================================
# EJEMPLO: VALOR DE LA INFORMACIÓN
# ============================================
# Definimos las acciones con sus probabilidades y utilidades
acciones = {
    "Acción A": ([0.7, 0.3], [100, -50]),  # 70% de ganar $100, 30% de perder $50
    "Acción B": ([0.5, 0.5], [200, -100]),  # 50% de ganar $200, 50% de perder $100
}

# Definimos los estados del mundo con sus probabilidades
estados = {
    "Estado 1": 0.7,  # Probabilidad del 70%
    "Estado 2": 0.3,  # Probabilidad del 30%
}

# Costo de obtener la información adicional
costo_informacion = 10

# Calculamos el VOI
valor_de_la_informacion, es_beneficioso = calcular_valor_de_la_informacion(acciones, estados, costo_informacion)

# Mostramos el resultado
print(f"Valor de la Información (VOI): {valor_de_la_informacion}")
if es_beneficioso:
    print(f"Es beneficioso obtener la información adicional (costo: {costo_informacion}).")
else:
    print(f"No es beneficioso obtener la información adicional (costo: {costo_informacion}).")