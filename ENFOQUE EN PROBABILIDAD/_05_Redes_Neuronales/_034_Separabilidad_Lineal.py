import numpy as np
import matplotlib.pyplot as plt

# ============================================
# GENERAR DATOS LINEALMENTE SEPARABLES
# ============================================
def generar_datos_lineales():
    """
    Genera un conjunto de datos linealmente separables.
    :return: Características (X) y etiquetas (y).
    """
    X = np.array([
        [2, 3],
        [3, 3],
        [4, 5],
        [1, 1],
        [2, 1],
        [3, 2]
    ])
    y = np.array([1, 1, 1, -1, -1, -1])  # Etiquetas de clase
    return X, y

# ============================================
# GENERAR DATOS NO LINEALMENTE SEPARABLES
# ============================================
def generar_datos_no_lineales():
    """
    Genera un conjunto de datos no linealmente separables.
    :return: Características (X) y etiquetas (y).
    """
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    y = np.array([-1, 1, 1, -1])  # Etiquetas de clase (XOR)
    return X, y

# ============================================
# VISUALIZAR DATOS
# ============================================
def visualizar_datos(X, y, titulo):
    """
    Visualiza un conjunto de datos en 2D.
    :param X: Características (numpy array).
    :param y: Etiquetas (numpy array).
    :param titulo: Título del gráfico.
    """
    plt.figure(figsize=(6, 6))
    for clase in np.unique(y):
        plt.scatter(X[y == clase][:, 0], X[y == clase][:, 1], label=f"Clase {clase}")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Línea horizontal
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Línea vertical
    plt.title(titulo)
    plt.xlabel("Característica 1")
    plt.ylabel("Característica 2")
    plt.legend()
    plt.grid()
    plt.show()

# ============================================
# EJEMPLO: SEPARABILIDAD LINEAL Y NO LINEAL
# ============================================
# Datos linealmente separables
X_lineal, y_lineal = generar_datos_lineales()
visualizar_datos(X_lineal, y_lineal, "Datos Linealmente Separables")

# Datos no linealmente separables
X_no_lineal, y_no_lineal = generar_datos_no_lineales()
visualizar_datos(X_no_lineal, y_no_lineal, "Datos No Linealmente Separables")