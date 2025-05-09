import numpy as np

# ============================================
# SIMULACIÓN DE UNA CADENA DE MARKOV
# ============================================
def simular_cadena_markov(matriz_transicion, estado_inicial, num_pasos):
    """
    Simula una cadena de Markov.
    :param matriz_transicion: Matriz de transición (numpy array).
    :param estado_inicial: Estado inicial (índice entero).
    :param num_pasos: Número de pasos a simular.
    :return: Lista de estados visitados.
    """
    estados = [estado_inicial]  # Lista para almacenar los estados visitados
    estado_actual = estado_inicial

    for _ in range(num_pasos):
        # Seleccionar el siguiente estado basado en las probabilidades de transición
        estado_actual = np.random.choice(
            range(len(matriz_transicion)),
            p=matriz_transicion[estado_actual]
        )
        estados.append(estado_actual)

    return estados

# ============================================
# DEFINICIÓN DE LA MATRIZ DE TRANSICIÓN
# ============================================
# Ejemplo: 3 estados (0, 1, 2)
matriz_transicion = np.array([
    [0.1, 0.6, 0.3],  # Probabilidades de transición desde el estado 0
    [0.4, 0.4, 0.2],  # Probabilidades de transición desde el estado 1
    [0.3, 0.3, 0.4]   # Probabilidades de transición desde el estado 2
])

# ============================================
# PARÁMETROS DE LA SIMULACIÓN
# ============================================
estado_inicial = 0  # Comenzamos en el estado 0
num_pasos = 20  # Número de pasos a simular

# Simular la cadena de Markov
estados_visitados = simular_cadena_markov(matriz_transicion, estado_inicial, num_pasos)

# Mostrar los resultados
print("Estados visitados:", estados_visitados)