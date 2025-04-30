# ============================================
# PROBABILIDAD A PRIORI: CÁLCULO DE PROBABILIDADES INICIALES
# ============================================

# DESCRIPCIÓN TEÓRICA:
# La probabilidad a priori representa nuestras creencias iniciales sobre un evento antes de observar evidencia.
# Es una probabilidad inicial basada en información previa o conocimiento histórico.
#
# En el contexto de la Regla de Bayes:
# - P(H): Es la probabilidad a priori de la hipótesis H.
# - P(¬H): Es la probabilidad a priori de que la hipótesis no sea verdadera.
#
# EJEMPLO:
# Supongamos que queremos calcular la probabilidad de que un correo sea spam basado en datos históricos:
# - El 20% de los correos recibidos son spam (P(Spam) = 0.2).
# - El 80% de los correos recibidos no son spam (P(No Spam) = 0.8).
# Este algoritmo calcula las probabilidades a priori y las utiliza para tomar decisiones iniciales.

# ============================================
# FUNCIÓN PARA CALCULAR PROBABILIDADES A PRIORI
# ============================================
def calcular_probabilidades_a_priori(eventos):
    """
    Calcula las probabilidades a priori de una lista de eventos.
    :param eventos: Diccionario donde las claves son los nombres de los eventos y los valores son sus frecuencias.
    :return: Diccionario con las probabilidades a priori de cada evento.
    """
    # Calculamos el total de frecuencias
    # Por qué: Necesitamos el total para normalizar las frecuencias en probabilidades.
    # Para qué: Esto asegura que las probabilidades sumen 1.
    total = sum(eventos.values())

    # Calculamos las probabilidades a priori
    # Por qué: Convertimos las frecuencias en probabilidades dividiendo entre el total.
    # Para qué: Esto nos da las probabilidades iniciales de cada evento.
    probabilidades_a_priori = {evento: frecuencia / total for evento, frecuencia in eventos.items()}

    return probabilidades_a_priori

# ============================================
# EJEMPLO: CLASIFICACIÓN DE CORREOS
# ============================================
# Frecuencias históricas de los eventos
eventos = {
    "Spam": 200,       # 200 correos son spam
    "No Spam": 800     # 800 correos no son spam
}

# Llamamos a la función para calcular las probabilidades a priori
probabilidades_a_priori = calcular_probabilidades_a_priori(eventos)

# Mostramos los resultados
print("Probabilidades a priori:")
for evento, probabilidad in probabilidades_a_priori.items():
    print(f"P({evento}) = {probabilidad:.2f}")
# Por qué: Mostramos las probabilidades iniciales para interpretar los resultados.
# Para qué: Esto nos ayuda a entender las probabilidades antes de observar evidencia.

# ============================================
# INTERPRETACIÓN DEL RESULTADO
# ============================================
# En este ejemplo, las probabilidades a priori nos indican que el 20% de los correos son spam y el 80% no lo son.
# Estas probabilidades iniciales pueden ser utilizadas como base para cálculos posteriores, como la Regla de Bayes.