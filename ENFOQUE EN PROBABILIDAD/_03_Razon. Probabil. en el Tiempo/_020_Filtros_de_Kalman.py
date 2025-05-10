import numpy as np

# ============================================
# FILTRO DE KALMAN
# ============================================
def filtro_de_kalman(A, B, H, Q, R, x_inicial, P_inicial, mediciones, u=None):
    """
    Implementa el Filtro de Kalman.
    :param A: Matriz de transición de estados.
    :param B: Matriz de control.
    :param H: Matriz de observación.
    :param Q: Covarianza del ruido del proceso.
    :param R: Covarianza del ruido de medición.
    :param x_inicial: Estado inicial.
    :param P_inicial: Covarianza inicial del error de estado.
    :param mediciones: Lista de mediciones observadas.
    :param u: Lista de entradas de control (opcional).
    :return: Lista de estimaciones de estado.
    """
    n = len(mediciones)  # Número de pasos de tiempo
    x = x_inicial  # Estado inicial
    P = P_inicial  # Covarianza inicial
    estimaciones = []  # Lista para almacenar las estimaciones de estado

    for t in range(n):
        # Predicción
        x_pred = A @ x + (B @ u[t] if u is not None else 0)
        P_pred = A @ P @ A.T + Q

        # Actualización
        K = P_pred @ H.T @ np.linalg.inv(H @ P_pred @ H.T + R)  # Ganancia de Kalman
        x = x_pred + K @ (mediciones[t] - H @ x_pred)  # Estado actualizado
        P = (np.eye(len(P)) - K @ H) @ P_pred  # Covarianza actualizada

        # Almacenar la estimación
        estimaciones.append(x)

    return estimaciones

# ============================================
# EJEMPLO: FILTRO DE KALMAN
# ============================================
# Parámetros del sistema
A = np.array([[1, 1], [0, 1]])  # Matriz de transición de estados
B = np.array([[0.5], [1]])  # Matriz de control
H = np.array([[1, 0]])  # Matriz de observación
Q = np.array([[1, 0], [0, 1]])  # Covarianza del ruido del proceso
R = np.array([[1]])  # Covarianza del ruido de medición

# Estado inicial y covarianza inicial
x_inicial = np.array([0, 1])  # Posición inicial y velocidad inicial
P_inicial = np.array([[1, 0], [0, 1]])  # Covarianza inicial

# Mediciones observadas (posición)
mediciones = [1, 2, 3, 4, 5]

# Entradas de control (aceleración)
u = [1, 1, 1, 1, 1]

# ============================================
# EJECUTAR EL FILTRO DE KALMAN
# ============================================
estimaciones = filtro_de_kalman(A, B, H, Q, R, x_inicial, P_inicial, mediciones, u)

# Mostrar los resultados
print("Estimaciones de estado:")
for t, est in enumerate(estimaciones):
    print(f"Tiempo {t}: {est}")