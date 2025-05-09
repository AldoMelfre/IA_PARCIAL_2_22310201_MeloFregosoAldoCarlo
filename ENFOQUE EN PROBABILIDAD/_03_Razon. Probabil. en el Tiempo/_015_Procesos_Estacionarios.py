import numpy as np
import matplotlib.pyplot as plt

# ============================================
# SIMULACIÓN DE UN PROCESO ESTACIONARIO
# ============================================
def generar_proceso_estacionario(media, varianza, longitud, correlacion=0.9):
    """
    Genera un proceso estacionario con media constante, varianza constante y autocorrelación.
    :param media: Media del proceso.
    :param varianza: Varianza del proceso.
    :param longitud: Número de puntos en el proceso.
    :param correlacion: Correlación entre puntos consecutivos (entre 0 y 1).
    :return: Serie temporal del proceso estacionario.
    """
    # Inicializar el proceso
    proceso = np.zeros(longitud)  # Crear un arreglo para almacenar los valores del proceso
    proceso[0] = np.random.normal(media, np.sqrt(varianza))  # Generar el primer valor del proceso

    # Generar los valores del proceso
    for t in range(1, longitud):
        # Generar ruido con varianza ajustada para mantener la correlación
        ruido = np.random.normal(0, np.sqrt(varianza * (1 - correlacion**2)))
        # Calcular el valor actual del proceso basado en el valor anterior y el ruido
        proceso[t] = correlacion * proceso[t-1] + ruido

    return proceso

# ============================================
# PARÁMETROS DEL PROCESO
# ============================================
media = 0  # Media constante del proceso
varianza = 1  # Varianza constante del proceso
longitud = 500  # Número de puntos en la serie temporal
correlacion = 0.8  # Correlación entre puntos consecutivos (entre 0 y 1)

# Generar el proceso estacionario
proceso = generar_proceso_estacionario(media, varianza, longitud, correlacion)

# ============================================
# VISUALIZACIÓN DEL PROCESO
# ============================================
plt.figure(figsize=(10, 6))  # Configurar el tamaño de la figura
plt.plot(proceso, label="Proceso Estacionario")  # Graficar el proceso
plt.axhline(media, color='red', linestyle='--', label="Media")  # Línea horizontal para la media
plt.title("Simulación de un Proceso Estacionario")  # Título del gráfico
plt.xlabel("Tiempo")  # Etiqueta del eje X
plt.ylabel("Valor")  # Etiqueta del eje Y
plt.legend()  # Mostrar la leyenda
plt.show()  # Mostrar el gráfico