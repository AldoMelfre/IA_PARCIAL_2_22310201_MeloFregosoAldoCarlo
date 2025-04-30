# ============================================
# PROBABILIDAD CONDICIONADA Y NORMALIZACIÓN
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La **probabilidad condicionada** mide la probabilidad de que ocurra un evento A dado que ya ocurrió otro evento B.
# Se calcula con la fórmula:
# P(A | B) = P(A ∩ B) / P(B)
#
# La **normalización** asegura que las probabilidades sumen 1, lo cual es necesario para que sean válidas.
# Esto se logra dividiendo cada probabilidad entre la suma total de probabilidades.
#
# EJEMPLO:
# Supongamos que queremos calcular la probabilidad de que un correo sea spam dado que contiene la palabra "oferta".
# - P(Spam) = 0.2
# - P(No Spam) = 0.8
# - P("oferta" | Spam) = 0.7
# - P("oferta" | No Spam) = 0.1
# Este algoritmo calcula P(Spam | "oferta") y P(No Spam | "oferta") utilizando probabilidad condicionada y normalización.

# ============================================
# FUNCIÓN PARA CALCULAR PROBABILIDAD CONDICIONADA
# ============================================
def calcular_probabilidad_condicionada(prior, likelihood):
    """
    Calcula la probabilidad conjunta y la normaliza para obtener probabilidades condicionadas.
    :param prior: Diccionario con las probabilidades a priori de los eventos.
    :param likelihood: Diccionario con las probabilidades de la evidencia dado cada evento.
    :return: Diccionario con las probabilidades condicionadas normalizadas.
    """
    # Calculamos las probabilidades conjuntas
    # Por qué: La probabilidad conjunta combina la probabilidad a priori con la probabilidad de la evidencia.
    # Para qué: Esto nos da P(A ∩ B) para cada evento.
    conjunta = {evento: prior[evento] * likelihood[evento] for evento in prior}

    # Calculamos la suma total de las probabilidades conjuntas
    # Por qué: Necesitamos la suma total para normalizar las probabilidades.
    # Para qué: Esto asegura que las probabilidades condicionadas sumen 1.
    total = sum(conjunta.values())

    # Normalizamos las probabilidades conjuntas
    # Por qué: Dividimos cada probabilidad conjunta entre la suma total para obtener probabilidades condicionadas.
    # Para qué: Esto nos da P(A | B) para cada evento.
    condicionada = {evento: conjunta[evento] / total for evento in conjunta}

    return condicionada

# ============================================
# EJEMPLO: CLASIFICACIÓN DE CORREOS CON "OFERTA"
# ============================================
# Probabilidades a priori
prior = {
    "Spam": 0.2,       # 20% de los correos son spam
    "No Spam": 0.8     # 80% de los correos no son spam
}

# Probabilidades de la evidencia dado cada evento (P("oferta" | Evento))
likelihood = {
    "Spam": 0.7,       # 70% de los correos spam contienen "oferta"
    "No Spam": 0.1     # 10% de los correos no spam contienen "oferta"
}

# Llamamos a la función para calcular las probabilidades condicionadas
probabilidades_condicionadas = calcular_probabilidad_condicionada(prior, likelihood)

# Mostramos los resultados
print("Probabilidades condicionadas normalizadas:")
for evento, probabilidad in probabilidades_condicionadas.items():
    print(f"P({evento} | 'oferta') = {probabilidad:.2f}")
# Por qué: Mostramos las probabilidades condicionadas para interpretar los resultados.
# Para qué: Esto nos ayuda a entender cómo cambia la probabilidad de cada evento dado la evidencia.

# ============================================
# INTERPRETACIÓN DEL RESULTADO
# ============================================
# En este ejemplo, las probabilidades condicionadas nos indican cómo cambia la probabilidad de que un correo sea spam
# o no spam dado que contiene la palabra "oferta". La normalización asegura que las probabilidades sumen 1.