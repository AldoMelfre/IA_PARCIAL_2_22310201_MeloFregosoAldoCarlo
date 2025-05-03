# ============================================
# REGLA DE BAYES: ACTUALIZACIÓN DE PROBABILIDADES
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La **Regla de Bayes** es una herramienta fundamental en probabilidad para actualizar nuestras creencias
# sobre una hipótesis (H) en función de nueva evidencia (E). Se expresa como:
#
# P(H | E) = [P(E | H) * P(H)] / P(E)
#
# Donde:
# - P(H | E): Probabilidad posterior de la hipótesis H dado que ocurrió la evidencia E.
# - P(E | H): Probabilidad de observar la evidencia E si la hipótesis H es verdadera.
# - P(H): Probabilidad previa de la hipótesis H (antes de observar la evidencia).
# - P(E): Probabilidad de la evidencia E (normalizador).
#
# EJEMPLO:
# Supongamos que un médico quiere diagnosticar una enfermedad rara basada en un resultado positivo de una prueba.
# - La enfermedad tiene una prevalencia del 1% (P(H)).
# - La prueba tiene una sensibilidad del 95% (P(E | H)).
# - La prueba tiene una tasa de falsos positivos del 5% (P(E | ¬H)).
# Este algoritmo calcula la probabilidad de que el paciente tenga la enfermedad dado un resultado positivo.

# ============================================
# FUNCIÓN PARA CALCULAR LA PROBABILIDAD POSTERIOR
# ============================================
def regla_de_bayes(p_hipotesis, p_evidencia_dado_hipotesis, p_evidencia_dado_no_hipotesis):
    """
    Calcula la probabilidad posterior utilizando la Regla de Bayes.
    :param p_hipotesis: Probabilidad previa de la hipótesis (P(H)).
    :param p_evidencia_dado_hipotesis: Probabilidad de la evidencia dado que la hipótesis es verdadera (P(E | H)).
    :param p_evidencia_dado_no_hipotesis: Probabilidad de la evidencia dado que la hipótesis es falsa (P(E | ¬H)).
    :return: Probabilidad posterior de la hipótesis dado la evidencia (P(H | E)).
    """
    # Calculamos la probabilidad de la hipótesis complementaria (¬H)
    # Por qué: Necesitamos considerar tanto la hipótesis como su complemento para calcular P(E).
    # Para qué: Esto asegura que tengamos en cuenta todas las posibilidades.
    p_no_hipotesis = 1 - p_hipotesis

    # Calculamos la probabilidad total de la evidencia (P(E))
    # Por qué: P(E) es el denominador en la Regla de Bayes y normaliza las probabilidades.
    # Para qué: Esto asegura que la probabilidad posterior esté correctamente escalada.
    p_evidencia = (p_evidencia_dado_hipotesis * p_hipotesis) + (p_evidencia_dado_no_hipotesis * p_no_hipotesis)

    # Calculamos la probabilidad posterior (P(H | E))
    # Por qué: Usamos la Regla de Bayes para actualizar nuestra creencia sobre la hipótesis.
    # Para qué: Esto nos da la probabilidad de la hipótesis dado que ocurrió la evidencia.
    p_posterior = (p_evidencia_dado_hipotesis * p_hipotesis) / p_evidencia

    return p_posterior

# ============================================
# EJEMPLO: DIAGNÓSTICO MÉDICO
# ============================================
# Probabilidad previa de la enfermedad (P(H))
p_hipotesis = 0.01  # 1% de prevalencia

# Probabilidad de un resultado positivo si el paciente tiene la enfermedad (P(E | H))
p_evidencia_dado_hipotesis = 0.95  # Sensibilidad del 95%

# Probabilidad de un resultado positivo si el paciente no tiene la enfermedad (P(E | ¬H))
p_evidencia_dado_no_hipotesis = 0.05  # Tasa de falsos positivos del 5%

# Llamamos a la función para calcular la probabilidad posterior
p_posterior = regla_de_bayes(p_hipotesis, p_evidencia_dado_hipotesis, p_evidencia_dado_no_hipotesis)

# Mostramos el resultado
print("Probabilidad posterior de tener la enfermedad dado un resultado positivo:")
print(f"P(H | E) = {p_posterior:.4f}")
# Por qué: Mostramos el resultado para interpretar la probabilidad posterior.
# Para qué: Esto ayuda a tomar decisiones informadas basadas en la evidencia.

# ============================================
# INTERPRETACIÓN DEL RESULTADO
# ============================================
# En este ejemplo, aunque la prueba tiene alta sensibilidad, la probabilidad posterior de tener la enfermedad
# sigue siendo baja debido a la baja prevalencia de la enfermedad. Esto ilustra cómo la Regla de Bayes
# combina la probabilidad previa con la nueva evidencia para manejar la incertidumbre.