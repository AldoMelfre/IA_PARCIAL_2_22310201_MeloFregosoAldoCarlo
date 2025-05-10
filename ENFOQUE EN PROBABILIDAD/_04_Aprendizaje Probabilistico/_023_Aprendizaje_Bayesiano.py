import numpy as np
import matplotlib.pyplot as plt

# ============================================
# APRENDIZAJE BAYESIANO: ESTIMACIÓN BINOMIAL
# ============================================
def aprendizaje_bayesiano_binomial(alpha, beta, datos):
    """
    Realiza aprendizaje bayesiano para un experimento binomial.
    :param alpha: Parámetro alfa de la distribución Beta (prior).
    :param beta: Parámetro beta de la distribución Beta (prior).
    :param datos: Lista de observaciones (1 para éxito, 0 para fracaso).
    :return: Parámetros actualizados de la distribución Beta.
    """
    # Contar éxitos y fracasos en los datos
    exitos = sum(datos)
    fracasos = len(datos) - exitos

    # Actualizar los parámetros de la distribución Beta
    alpha_posterior = alpha + exitos
    beta_posterior = beta + fracasos

    return alpha_posterior, beta_posterior

# ============================================
# EJEMPLO: LANZAMIENTO DE UNA MONEDA
# ============================================
# Parámetros iniciales de la distribución Beta (prior)
alpha = 2  # Creencia inicial sobre éxitos
beta = 2   # Creencia inicial sobre fracasos

# Datos observados (1 = éxito, 0 = fracaso)
datos = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]

# Actualizar la distribución posterior
alpha_posterior, beta_posterior = aprendizaje_bayesiano_binomial(alpha, beta, datos)

# ============================================
# VISUALIZAR LA DISTRIBUCIÓN POSTERIOR
# ============================================
x = np.linspace(0, 1, 100)
posterior = (x ** (alpha_posterior - 1)) * ((1 - x) ** (beta_posterior - 1))
posterior /= np.sum(posterior)  # Normalizar

plt.figure(figsize=(8, 6))
plt.plot(x, posterior, label=f"Posterior Beta({alpha_posterior}, {beta_posterior})")
plt.title("Distribución Posterior (Aprendizaje Bayesiano)")
plt.xlabel("Probabilidad de éxito")
plt.ylabel("Densidad de probabilidad")
plt.legend()
plt.show()