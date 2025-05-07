# ============================================
# REGLA DE LA CADENA: DESCOMPOSICIÓN DE PROBABILIDADES CONJUNTAS
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La **Regla de la Cadena** descompone una probabilidad conjunta en términos de probabilidades condicionales.
# Para un conjunto de variables aleatorias A, B, C, ..., Z:
# P(A, B, C, ..., Z) = P(A) * P(B | A) * P(C | A, B) * ... * P(Z | A, B, ..., Y)
#
# Esto es útil para calcular probabilidades conjuntas en sistemas complejos, como redes bayesianas.
#
# EJEMPLOS:
# 1. Caso simple: Dos variables (A y B).
# 2. Caso intermedio: Tres variables (A, B y C).
# 3. Caso complejo: Cuatro variables (A, B, C y D).

# ============================================
# FUNCIÓN PARA CALCULAR PROBABILIDAD CONJUNTA USANDO LA REGLA DE LA CADENA
# ============================================
def calcular_probabilidad_conjunta(probabilidades_condicionales):
    """
    Calcula la probabilidad conjunta utilizando la Regla de la Cadena.
    :param probabilidades_condicionales: Lista de probabilidades condicionales en el orden de la descomposición.
    :return: Probabilidad conjunta.
    """
    probabilidad_conjunta = 1.0  # Inicializamos la probabilidad conjunta

    # Multiplicamos todas las probabilidades condicionales
    for probabilidad in probabilidades_condicionales:
        probabilidad_conjunta *= probabilidad

    return probabilidad_conjunta

# ============================================
# CASO 1: DOS VARIABLES (A Y B)
# ============================================
# P(A) = 0.6
# P(B | A) = 0.7
probabilidades_caso_1 = [0.6, 0.7]
probabilidad_conjunta_caso_1 = calcular_probabilidad_conjunta(probabilidades_caso_1)

print("Caso 1: Dos variables (A y B)")
print(f"P(A, B) = {probabilidad_conjunta_caso_1:.4f}")

# ============================================
# CASO 2: TRES VARIABLES (A, B Y C)
# ============================================
# P(A) = 0.5
# P(B | A) = 0.8
# P(C | A, B) = 0.9
probabilidades_caso_2 = [0.5, 0.8, 0.9]
probabilidad_conjunta_caso_2 = calcular_probabilidad_conjunta(probabilidades_caso_2)

print("\nCaso 2: Tres variables (A, B y C)")
print(f"P(A, B, C) = {probabilidad_conjunta_caso_2:.4f}")

# ============================================
# CASO 3: CUATRO VARIABLES (A, B, C Y D)
# ============================================
# P(A) = 0.4
# P(B | A) = 0.6
# P(C | A, B) = 0.7
# P(D | A, B, C) = 0.8
probabilidades_caso_3 = [0.4, 0.6, 0.7, 0.8]
probabilidad_conjunta_caso_3 = calcular_probabilidad_conjunta(probabilidades_caso_3)

print("\nCaso 3: Cuatro variables (A, B, C y D)")
print(f"P(A, B, C, D) = {probabilidad_conjunta_caso_3:.4f}")

# ============================================
# INTERPRETACIÓN DEL RESULTADO
# ============================================
# En cada caso, la probabilidad conjunta se calcula multiplicando las probabilidades condicionales
# en el orden especificado por la Regla de la Cadena. Esto permite descomponer problemas complejos
# en cálculos más simples.