# ============================================
# APRENDIZAJE POR REFUERZO PASIVO
# ============================================

# DESCRIPCIÓN TEÓRICA:
# El aprendizaje por refuerzo pasivo evalúa una política fija en un entorno desconocido.
# El agente observa las transiciones y recompensas mientras sigue la política, y aprende los valores
# de los estados basándose en estas experiencias.
# 
# COMPONENTES:
# - **Estados:** Representan las posibles situaciones del entorno.
# - **Acciones:** Decisiones que el agente puede tomar en cada estado.
# - **Recompensas:** Beneficio inmediato obtenido al realizar una acción en un estado.
# - **Política:** Estrategia fija que el agente sigue.
# 
# EJEMPLO:
# Un robot se encuentra en una cuadrícula 3x3 y sigue una política fija para moverse.
# El objetivo es aprender los valores de los estados basándose en las recompensas observadas.

# ============================================
# FUNCIÓN PARA APRENDIZAJE POR REFUERZO PASIVO
# ============================================
def aprendizaje_por_refuerzo_pasivo(politica, estados, transiciones, recompensas, gamma, episodios):
    """
    Implementa el aprendizaje por refuerzo pasivo utilizando evaluación de políticas.
    :param politica: Diccionario que asigna una acción a cada estado.
    :param estados: Lista de estados posibles.
    :param transiciones: Diccionario con las probabilidades de transición entre estados.
    :param recompensas: Diccionario con las recompensas inmediatas para cada estado y acción.
    :param gamma: Factor de descuento (0 <= gamma <= 1).
    :param episodios: Número de episodios para entrenar.
    :return: Diccionario con los valores aprendidos de los estados.
    """
    # Inicializamos los valores de los estados en 0
    valores = {estado: 0 for estado in estados}
    conteo_visitas = {estado: 0 for estado in estados}  # Para promediar las recompensas

    # Iteramos sobre los episodios
    for _ in range(episodios):
        # Seleccionamos un estado inicial aleatorio
        estado_actual = estados[0]

        # Seguimos la política hasta que terminemos el episodio
        while True:
            accion = politica[estado_actual]  # Acción según la política
            siguiente_estado = obtener_siguiente_estado(estado_actual, accion, transiciones)  # Simulamos la transición
            recompensa = recompensas.get((estado_actual, accion, siguiente_estado), 0)  # Obtenemos la recompensa

            # Actualizamos el valor del estado actual usando promedio incremental
            conteo_visitas[estado_actual] += 1
            tasa_aprendizaje = 1 / conteo_visitas[estado_actual]
            valores[estado_actual] += tasa_aprendizaje * (
                recompensa + gamma * valores[siguiente_estado] - valores[estado_actual]
            )

            # Si llegamos a un estado terminal, terminamos el episodio
            if es_estado_terminal(siguiente_estado):
                break

            # Actualizamos el estado actual
            estado_actual = siguiente_estado

    return valores

# ============================================
# FUNCIONES AUXILIARES
# ============================================
def obtener_siguiente_estado(estado_actual, accion, transiciones):
    """
    Simula la transición al siguiente estado basándose en las probabilidades.
    :param estado_actual: Estado actual.
    :param accion: Acción tomada.
    :param transiciones: Diccionario con las probabilidades de transición.
    :return: Siguiente estado.
    """
    import random
    probabilidades = [
        (siguiente_estado, prob)
        for (estado, accion_actual, siguiente_estado), prob in transiciones.items()
        if estado == estado_actual and accion_actual == accion
    ]
    estados, probs = zip(*probabilidades)
    return random.choices(estados, probs)[0]

def es_estado_terminal(estado):
    """
    Verifica si un estado es terminal.
    :param estado: Estado a verificar.
    :return: True si el estado es terminal, False en caso contrario.
    """
    # En este ejemplo, consideramos que no hay estados terminales
    return False

# ============================================
# EJEMPLO: ROBOT EN UNA CUADRÍCULA
# ============================================
# Definimos los estados (posiciones en la cuadrícula)
estados = [(x, y) for x in range(3) for y in range(3)]

# Definimos las acciones
acciones = ["Arriba", "Abajo", "Izquierda", "Derecha"]

# Definimos las probabilidades de transición
transiciones = {
    ((0, 0), "Derecha", (0, 1)): 1.0, ((0, 0), "Abajo", (1, 0)): 1.0,
    ((0, 1), "Derecha", (0, 2)): 1.0, ((0, 1), "Izquierda", (0, 0)): 1.0, ((0, 1), "Abajo", (1, 1)): 1.0,
    ((0, 2), "Izquierda", (0, 1)): 1.0,
    ((1, 0), "Arriba", (0, 0)): 1.0, ((1, 0), "Derecha", (1, 1)): 1.0, ((1, 0), "Abajo", (2, 0)): 1.0,
    ((1, 1), "Arriba", (0, 1)): 1.0, ((1, 1), "Derecha", (1, 2)): 1.0, ((1, 1), "Izquierda", (1, 0)): 1.0, ((1, 1), "Abajo", (2, 1)): 1.0,
    ((1, 2), "Izquierda", (1, 1)): 1.0, ((1, 2), "Arriba", (0, 2)): 1.0, ((1, 2), "Abajo", (2, 2)): 1.0,
    ((2, 0), "Arriba", (1, 0)): 1.0, ((2, 0), "Derecha", (2, 1)): 1.0,
    ((2, 1), "Izquierda", (2, 0)): 1.0, ((2, 1), "Arriba", (1, 1)): 1.0, ((2, 1), "Derecha", (2, 2)): 1.0,
    ((2, 2), "Izquierda", (2, 1)): 1.0, ((2, 2), "Arriba", (1, 2)): 1.0,
}

# Definimos las recompensas inmediatas
recompensas = {
    ((0, 2), "Derecha", (0, 2)): 10,  # Recompensa por alcanzar el objetivo
    **{(estado, accion, siguiente_estado): -1 for estado in estados for accion in acciones for siguiente_estado in estados}
}

# Definimos una política fija
politica = {estado: "Derecha" for estado in estados}

# Factor de descuento
gamma = 0.9

# Número de episodios
episodios = 1000

# Llamamos a la función de aprendizaje por refuerzo pasivo
valores_aprendidos = aprendizaje_por_refuerzo_pasivo(politica, estados, transiciones, recompensas, gamma, episodios)

# Mostramos los valores aprendidos
print("Valores aprendidos de los estados:")
for estado, valor in valores_aprendidos.items():
    print(f"Estado {estado}: {valor:.2f}")