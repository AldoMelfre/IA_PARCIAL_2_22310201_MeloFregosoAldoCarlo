# ============================================
# TEORÍA DE LA UTILIDAD: FUNCIÓN DE UTILIDAD
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La teoría de la utilidad es un marco matemático utilizado para modelar la toma de decisiones bajo incertidumbre.
# Una función de utilidad asigna un valor numérico a cada posible resultado, representando la "satisfacción" o
# "beneficio" que un agente obtiene de ese resultado.
# 
# CARACTERÍSTICAS:
# - **Estados:** Representan las posibles situaciones del mundo.
# - **Acciones:** Decisiones que el agente puede tomar.
# - **Resultados:** Consecuencias de las acciones en los estados.
# - **Utilidad:** Valor numérico asignado a cada resultado.
# - **Utilidad esperada:** Promedio ponderado de las utilidades de los resultados, considerando las probabilidades.
# 
# EJEMPLO:
# Un agente debe decidir entre dos acciones:
# - Acción A: Tiene una probabilidad del 70% de ganar $100 y un 30% de perder $50.
# - Acción B: Tiene una probabilidad del 50% de ganar $200 y un 50% de perder $100.
# El algoritmo calcula la utilidad esperada de cada acción y selecciona la mejor.

# ============================================
# FUNCIÓN PARA CALCULAR LA UTILIDAD ESPERADA
# ============================================
def calcular_utilidad_esperada(probabilidades, utilidades):
    """
    Calcula la utilidad esperada de una acción.
    :param probabilidades: Lista de probabilidades de los resultados.
    :param utilidades: Lista de utilidades asociadas a los resultados.
    :return: La utilidad esperada.
    """
    # Inicializamos la utilidad esperada en 0
    utilidad_esperada = 0

    # Iteramos sobre las probabilidades y utilidades
    for p, u in zip(probabilidades, utilidades):
        utilidad_esperada += p * u  # Sumamos el producto de la probabilidad y la utilidad

    return utilidad_esperada  # Devolvemos la utilidad esperada

# ============================================
# FUNCIÓN PRINCIPAL PARA TOMAR DECISIONES
# ============================================
def tomar_decision(acciones):
    """
    Toma una decisión basada en la utilidad esperada de cada acción.
    :param acciones: Diccionario donde las claves son los nombres de las acciones y los valores son tuplas
                     (probabilidades, utilidades).
    :return: La mejor acción y su utilidad esperada.
    """
    mejor_accion = None  # Inicializamos la mejor acción como None
    mejor_utilidad = float('-inf')  # Inicializamos la mejor utilidad como menos infinito

    # Iteramos sobre las acciones
    for accion, (probabilidades, utilidades) in acciones.items():
        # Calculamos la utilidad esperada de la acción actual
        utilidad = calcular_utilidad_esperada(probabilidades, utilidades)
        print(f"Utilidad esperada de {accion}: {utilidad}")  # Mostramos la utilidad esperada

        # Actualizamos la mejor acción si la utilidad es mayor
        if utilidad > mejor_utilidad:
            mejor_accion = accion
            mejor_utilidad = utilidad

    return mejor_accion, mejor_utilidad  # Devolvemos la mejor acción y su utilidad esperada

# ============================================
# EJEMPLO: TOMA DE DECISIONES
# ============================================
# Definimos las acciones con sus probabilidades y utilidades
acciones = {
    "Acción A": ([0.7, 0.3], [100, -50]),  # 70% de ganar $100, 30% de perder $50
    "Acción B": ([0.5, 0.5], [200, -100]),  # 50% de ganar $200, 50% de perder $100
}

# Llamamos a la función para tomar una decisión
mejor_accion, mejor_utilidad = tomar_decision(acciones)

# Mostramos el resultado
print(f"\nLa mejor acción es: {mejor_accion} con una utilidad esperada de {mejor_utilidad}")