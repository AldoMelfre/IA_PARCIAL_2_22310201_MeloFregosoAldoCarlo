import numpy as np

# ============================================
# FILTRADO DE PARTÍCULAS
# ============================================
def filtrado_de_particulas(num_particulas, modelo_transicion, modelo_observacion, evidencia, estado_inicial):
    """
    Implementa el Filtrado de Partículas.
    :param num_particulas: Número de partículas.
    :param modelo_transicion: Función que define el modelo de transición.
    :param modelo_observacion: Función que define el modelo de observación.
    :param evidencia: Lista de observaciones.
    :param estado_inicial: Distribución inicial de estados.
    :return: Lista de estimaciones de estado.
    """
    # Inicializar partículas y pesos
    particulas = np.random.choice(estado_inicial, size=num_particulas)
    pesos = np.ones(num_particulas) / num_particulas  # Pesos iniciales uniformes

    estimaciones = []  # Lista para almacenar las estimaciones

    for obs in evidencia:
        # Predicción: Propagar las partículas hacia adelante
        particulas = np.array([modelo_transicion(p) for p in particulas])

        # Actualización: Ajustar los pesos basándose en la evidencia
        pesos = np.array([modelo_observacion(p, obs) for p in particulas])
        pesos /= np.sum(pesos)  # Normalizar los pesos

        # Reamostrado: Generar nuevas partículas basándose en los pesos
        indices = np.random.choice(range(num_particulas), size=num_particulas, p=pesos)
        particulas = particulas[indices]
        pesos = np.ones(num_particulas) / num_particulas  # Reiniciar los pesos

        # Calcular la estimación como el promedio ponderado de las partículas
        estimacion = np.mean(particulas)
        estimaciones.append(estimacion)

    return estimaciones

# ============================================
# EJEMPLO: FILTRADO DE PARTÍCULAS
# ============================================
# Modelo de transición: x_t = x_{t-1} + ruido
def modelo_transicion(estado):
    return estado + np.random.normal(0, 1)

# Modelo de observación: P(e_t | x_t)
def modelo_observacion(estado, observacion):
    return np.exp(-0.5 * ((observacion - estado) ** 2) / 1)  # Gaussiana con varianza 1

# Parámetros del sistema
num_particulas = 1000
estado_inicial = np.linspace(-10, 10, num_particulas)  # Estados iniciales uniformemente distribuidos
evidencia = [1, 2, 3, 4, 5]  # Observaciones

# ============================================
# EJECUTAR EL FILTRADO DE PARTÍCULAS
# ============================================
estimaciones = filtrado_de_particulas(num_particulas, modelo_transicion, modelo_observacion, evidencia, estado_inicial)

# Mostrar los resultados
print("Estimaciones de estado:")
for t, est in enumerate(estimaciones):
    print(f"Tiempo {t}: {est}")