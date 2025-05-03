# ============================================
# DISTRIBUCIÓN DE PROBABILIDAD: REPRESENTACIÓN Y CÁLCULO
# ============================================

# DESCRIPCIÓN TEÓRICA:
# Una **distribución de probabilidad** describe cómo se distribuyen las probabilidades entre los posibles valores
# de una variable aleatoria. Puede ser discreta (valores específicos) o continua (intervalos de valores).
#
# Propiedades clave:
# 1. Cada probabilidad es mayor o igual a 0: P(x) ≥ 0.
# 2. La suma de todas las probabilidades es igual a 1: Σ P(x) = 1.
#
# EJEMPLO:
# Supongamos que lanzamos un dado justo. La distribución de probabilidad de los resultados es:
# - P(1) = 1/6
# - P(2) = 1/6
# - P(3) = 1/6
# - P(4) = 1/6
# - P(5) = 1/6
# - P(6) = 1/6
# Este algoritmo calcula y representa una distribución de probabilidad discreta.

# ============================================
# FUNCIÓN PARA CREAR UNA DISTRIBUCIÓN DE PROBABILIDAD
# ============================================
def crear_distribucion_probabilidad(eventos):
    """
    Crea una distribución de probabilidad a partir de una lista de eventos y sus frecuencias.
    :param eventos: Diccionario donde las claves son los eventos y los valores son sus frecuencias.
    :return: Diccionario con la distribución de probabilidad.
    """
    # Calculamos el total de frecuencias
    # Por qué: Necesitamos el total para normalizar las frecuencias en probabilidades.
    # Para qué: Esto asegura que las probabilidades sumen 1.
    total = sum(eventos.values())

    # Calculamos la distribución de probabilidad
    # Por qué: Convertimos las frecuencias en probabilidades dividiendo entre el total.
    # Para qué: Esto nos da la probabilidad de cada evento.
    distribucion = {evento: frecuencia / total for evento, frecuencia in eventos.items()}

    return distribucion

# ============================================
# FUNCIÓN PARA VERIFICAR UNA DISTRIBUCIÓN DE PROBABILIDAD
# ============================================
def verificar_distribucion(distribucion):
    """
    Verifica si una distribución de probabilidad es válida.
    :param distribucion: Diccionario con la distribución de probabilidad.
    :return: True si es válida, False en caso contrario.
    """
    # Verificamos que todas las probabilidades sean mayores o iguales a 0
    # Por qué: Una probabilidad no puede ser negativa.
    # Para qué: Esto asegura que la distribución sea válida.
    if any(prob < 0 for prob in distribucion.values()):
        return False

    # Verificamos que la suma de las probabilidades sea igual a 1
    # Por qué: La suma de las probabilidades debe ser 1 para que sea una distribución válida.
    # Para qué: Esto asegura que la distribución esté correctamente normalizada.
    if not abs(sum(distribucion.values()) - 1) < 1e-6:  # Tolerancia para errores numéricos
        return False

    return True

# ============================================
# EJEMPLO: DISTRIBUCIÓN DE UN DADO JUSTO
# ============================================
# Frecuencias de los eventos (resultados del dado)
eventos = {
    1: 1,  # Frecuencia del resultado 1
    2: 1,  # Frecuencia del resultado 2
    3: 1,  # Frecuencia del resultado 3
    4: 1,  # Frecuencia del resultado 4
    5: 1,  # Frecuencia del resultado 5
    6: 1   # Frecuencia del resultado 6
}

# Creamos la distribución de probabilidad
distribucion = crear_distribucion_probabilidad(eventos)

# Verificamos si la distribución es válida
es_valida = verificar_distribucion(distribucion)

# Mostramos los resultados
print("Distribución de probabilidad (Dado Justo):")
for evento, probabilidad in distribucion.items():
    print(f"P({evento}) = {probabilidad:.2f}")
print("\n¿Es una distribución válida?")
print("Sí" if es_valida else "No")

# ============================================
# EJEMPLO: DISTRIBUCIÓN INVÁLIDA
# ============================================
# Frecuencias de los eventos (distribución inválida)
eventos_invalidos = {
    1: 0.5,  # Frecuencia del resultado 1
    2: 0.3,  # Frecuencia del resultado 2
    3: 0.2,  # Frecuencia del resultado 3
    4: 0.1   # Frecuencia del resultado 4 (suma no es 1)
}

# Creamos la distribución de probabilidad
distribucion_invalida = eventos_invalidos  # Ya está en formato de probabilidad

# Verificamos si la distribución es válida
es_valida_invalida = verificar_distribucion(distribucion_invalida)

# Mostramos los resultados
print("\n============================================")
print("Distribución de probabilidad (Inválida):")
for evento, probabilidad in distribucion_invalida.items():
    print(f"P({evento}) = {probabilidad:.2f}")
print("\n¿Es una distribución válida?")
print("Sí" if es_valida_invalida else "No")

# ============================================
# INTERPRETACIÓN DEL RESULTADO
# ============================================
# En este ejemplo, la distribución de probabilidad es válida y representa un dado justo.
# Cada resultado tiene la misma probabilidad (1/6), y la suma de las probabilidades es igual a 1.