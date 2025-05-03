# ============================================
# INDEPENDENCIA CONDICIONAL: REPRESENTACIÓN Y VERIFICACIÓN
# ============================================

# DESCRIPCIÓN TEÓRICA:
# Dos eventos A y B son **independientes condicionalmente** dado un tercer evento C si:
# P(A ∩ B | C) = P(A | C) * P(B | C)
#
# Esto significa que, dado el conocimiento de C, la ocurrencia de A no afecta la probabilidad de B, y viceversa.
# La independencia condicional es útil para simplificar cálculos en modelos probabilísticos.
#
# EJEMPLO:
# Supongamos que queremos verificar si dos síntomas (fiebre y tos) son independientes condicionalmente
# dado que un paciente tiene gripe. Esto se puede verificar utilizando las probabilidades condicionales.

# ============================================
# FUNCIÓN PARA VERIFICAR INDEPENDENCIA CONDICIONAL
# ============================================
def verificar_independencia_condicional(p_a_dado_c, p_b_dado_c, p_a_y_b_dado_c):
    """
    Verifica si dos eventos son independientes condicionalmente dado un tercer evento.
    :param p_a_dado_c: Probabilidad de A dado C (P(A | C)).
    :param p_b_dado_c: Probabilidad de B dado C (P(B | C)).
    :param p_a_y_b_dado_c: Probabilidad de A y B dado C (P(A ∩ B | C)).
    :return: True si son independientes condicionalmente, False en caso contrario.
    """
    # Calculamos el producto de P(A | C) y P(B | C)
    # Por qué: Según la definición de independencia condicional, este producto debe ser igual a P(A ∩ B | C).
    # Para qué: Esto nos permite verificar si los eventos son independientes condicionalmente.
    producto = p_a_dado_c * p_b_dado_c

    # Verificamos si el producto es aproximadamente igual a P(A ∩ B | C)
    # Por qué: Usamos una tolerancia para manejar errores numéricos.
    # Para qué: Esto asegura que la comparación sea precisa.
    return abs(producto - p_a_y_b_dado_c) < 1e-6

# ============================================
# EJEMPLO: SÍNTOMAS Y GRIPE
# ============================================
# Probabilidades condicionales
p_a_dado_c = 0.8  # Probabilidad de fiebre dado que el paciente tiene gripe (P(Fiebre | Gripe))
p_b_dado_c = 0.6  # Probabilidad de tos dado que el paciente tiene gripe (P(Tos | Gripe))
p_a_y_b_dado_c = 0.48  # Probabilidad de fiebre y tos dado que el paciente tiene gripe (P(Fiebre ∩ Tos | Gripe))

# Verificamos si fiebre y tos son independientes condicionalmente dado que el paciente tiene gripe
es_independiente = verificar_independencia_condicional(p_a_dado_c, p_b_dado_c, p_a_y_b_dado_c)

# Mostramos los resultados
print("¿Son fiebre y tos independientes condicionalmente dado que el paciente tiene gripe?")
print("Sí" if es_independiente else "No")
# Por qué: Mostramos el resultado para interpretar la relación entre los eventos.
# Para qué: Esto ayuda a entender si los eventos son independientes condicionalmente.

# ============================================
# EJEMPLO: EVENTOS NO INDEPENDIENTES
# ============================================
# Probabilidades condicionales
p_a_dado_c = 0.7  # Probabilidad de fiebre dado que el paciente tiene gripe (P(Fiebre | Gripe))
p_b_dado_c = 0.5  # Probabilidad de tos dado que el paciente tiene gripe (P(Tos | Gripe))
p_a_y_b_dado_c = 0.45  # Probabilidad de fiebre y tos dado que el paciente tiene gripe (P(Fiebre ∩ Tos | Gripe))

# Verificamos si fiebre y tos son independientes condicionalmente dado que el paciente tiene gripe
es_independiente_no = verificar_independencia_condicional(p_a_dado_c, p_b_dado_c, p_a_y_b_dado_c)

# Mostramos los resultados
print("\n¿Son fiebre y tos independientes condicionalmente dado que el paciente tiene gripe (caso no independiente)?")
print("Sí" if es_independiente_no else "No")
# Por qué: Mostramos el resultado para interpretar la relación entre los eventos.
# Para qué: Esto ayuda a entender si los eventos son independientes condicionalmente.

# ============================================
# INTERPRETACIÓN DEL RESULTADO
# ============================================
# En el primer ejemplo, fiebre y tos son independientes condicionalmente dado que el paciente tiene gripe,
# ya que P(Fiebre ∩ Tos | Gripe) = P(Fiebre | Gripe) * P(Tos | Gripe).
# En el segundo ejemplo, no son independientes condicionalmente porque esta igualdad no se cumple.