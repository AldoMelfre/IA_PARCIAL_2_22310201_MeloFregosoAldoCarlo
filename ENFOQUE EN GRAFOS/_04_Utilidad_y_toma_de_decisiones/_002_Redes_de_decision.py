# ============================================
# REDES DE DECISIÓN: INVERSIÓN FINANCIERA
# ============================================

# DESCRIPCIÓN TEÓRICA:
# Las redes de decisión son una extensión de las redes bayesianas que incluyen nodos de decisión y nodos de utilidad.
# Estas redes permiten modelar problemas de toma de decisiones bajo incertidumbre, combinando probabilidades y utilidades.
# 
# COMPONENTES:
# - **Nodos de Probabilidad:** Representan variables aleatorias con distribuciones de probabilidad.
# - **Nodos de Decisión:** Representan las acciones que el agente puede tomar.
# - **Nodos de Utilidad:** Representan la utilidad asociada a los resultados de las decisiones.
# 
# EJEMPLO:
# Un agente debe decidir entre tres opciones de inversión:
# - Invertir en acciones: Alta ganancia si el mercado sube, pero alta pérdida si baja.
# - Invertir en bonos: Ganancia moderada sin importar el mercado.
# - Mantener efectivo: Sin ganancia ni pérdida, pero seguro.
# El algoritmo calcula la utilidad esperada de cada decisión y selecciona la mejor.

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
# FUNCIÓN PRINCIPAL PARA REDES DE DECISIÓN
# ============================================
def red_de_decision(decisiones):
    """
    Toma una decisión basada en la utilidad esperada de cada acción en una red de decisión.
    :param decisiones: Diccionario donde las claves son los nombres de las decisiones y los valores son tuplas
                       (probabilidades, utilidades).
    :return: La mejor decisión y su utilidad esperada.
    """
    mejor_decision = None  # Inicializamos la mejor decisión como None
    mejor_utilidad = float('-inf')  # Inicializamos la mejor utilidad como menos infinito

    # Iteramos sobre las decisiones
    for decision, (probabilidades, utilidades) in decisiones.items():
        # Calculamos la utilidad esperada de la decisión actual
        utilidad = calcular_utilidad_esperada(probabilidades, utilidades)
        print(f"Utilidad esperada de {decision}: {utilidad}")  # Mostramos la utilidad esperada

        # Actualizamos la mejor decisión si la utilidad es mayor
        if utilidad > mejor_utilidad:
            mejor_decision = decision
            mejor_utilidad = utilidad

    return mejor_decision, mejor_utilidad  # Devolvemos la mejor decisión y su utilidad esperada

# ============================================
# EJEMPLO: RED DE DECISIÓN PARA INVERSIÓN
# ============================================
# Definimos las decisiones con sus probabilidades y utilidades
decisiones = {
    "Invertir en acciones": ([0.6, 0.4], [100, -50]),  # 60% de que el mercado suba, 40% de que baje
    "Invertir en bonos": ([1.0], [30]),  # Siempre gana 30 sin importar el mercado
    "Mantener efectivo": ([1.0], [0]),  # Sin ganancia ni pérdida
}

# Llamamos a la función para tomar una decisión
mejor_decision, mejor_utilidad = red_de_decision(decisiones)

# Mostramos el resultado
print(f"\nLa mejor decisión es: {mejor_decision} con una utilidad esperada de {mejor_utilidad}")