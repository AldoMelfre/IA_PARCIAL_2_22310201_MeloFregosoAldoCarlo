# ============================================
# TEORÍA DE JUEGOS: EQUILIBRIO DE NASH
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La Teoría de Juegos estudia las interacciones estratégicas entre agentes racionales. 
# Un **Equilibrio de Nash** es una situación en la que ningún jugador puede mejorar su resultado
# cambiando unilateralmente su estrategia, dado que los demás jugadores mantienen sus estrategias.
# 
# COMPONENTES:
# - **Jugadores:** Los agentes que toman decisiones estratégicas.
# - **Estrategias:** Las opciones disponibles para cada jugador.
# - **Pagos:** Las recompensas que recibe cada jugador dependiendo de las estrategias elegidas.
# 
# EJEMPLO:
# Dos empresas (A y B) deben decidir si lanzar una campaña publicitaria o no. 
# - Si ambas lanzan la campaña, ambas obtienen una ganancia baja debido a la competencia.
# - Si ninguna lanza la campaña, ambas obtienen una ganancia moderada.
# - Si una lanza la campaña y la otra no, la que lanza obtiene una ganancia alta y la otra una ganancia baja.
# El algoritmo encuentra el equilibrio de Nash para este juego.

# ============================================
# FUNCIÓN PARA ENCONTRAR EL EQUILIBRIO DE NASH
# ============================================
def encontrar_equilibrio_de_nash(matriz_pagos_jugador1, matriz_pagos_jugador2):
    """
    Encuentra los equilibrios de Nash en un juego de dos jugadores con estrategias puras.
    :param matriz_pagos_jugador1: Matriz de pagos del Jugador 1.
    :param matriz_pagos_jugador2: Matriz de pagos del Jugador 2.
    :return: Lista de equilibrios de Nash como pares de estrategias.
    """
    nash_equilibrios = []

    # Iteramos sobre todas las estrategias posibles
    for i in range(len(matriz_pagos_jugador1)):  # Estrategias del Jugador 1
        for j in range(len(matriz_pagos_jugador1[0])):  # Estrategias del Jugador 2
            # Verificamos si (i, j) es un equilibrio de Nash
            es_mejor_para_jugador1 = all(
                matriz_pagos_jugador1[i][j] >= matriz_pagos_jugador1[k][j]
                for k in range(len(matriz_pagos_jugador1))
            )
            es_mejor_para_jugador2 = all(
                matriz_pagos_jugador2[i][j] >= matriz_pagos_jugador2[i][l]
                for l in range(len(matriz_pagos_jugador2[0]))
            )

            if es_mejor_para_jugador1 and es_mejor_para_jugador2:
                nash_equilibrios.append((i, j))

    return nash_equilibrios

# ============================================
# EJEMPLO: JUEGO DE LAS CAMPAÑAS PUBLICITARIAS
# ============================================
# Matriz de pagos para el Jugador 1 (Empresa A)
matriz_pagos_jugador1 = [
    [2, 0],  # Si Empresa A no lanza la campaña
    [3, 1],  # Si Empresa A lanza la campaña
]

# Matriz de pagos para el Jugador 2 (Empresa B)
matriz_pagos_jugador2 = [
    [2, 3],  # Si Empresa B no lanza la campaña
    [0, 1],  # Si Empresa B lanza la campaña
]

# Llamamos a la función para encontrar los equilibrios de Nash
equilibrios = encontrar_equilibrio_de_nash(matriz_pagos_jugador1, matriz_pagos_jugador2)

# Mostramos los resultados
print("Equilibrios de Nash encontrados:")
for equilibrio in equilibrios:
    print(f"Estrategia Empresa A: {equilibrio[0]}, Estrategia Empresa B: {equilibrio[1]}")