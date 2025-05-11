from hmmlearn import hmm
import numpy as np

# ============================================
# EJEMPLO: MODELO DE MARKOV OCULTO (HMM)
# ============================================

# Definir los parámetros del modelo
num_estados = 3  # Número de estados ocultos
num_observaciones = 4  # Número de posibles observaciones

# Crear el modelo HMM
modelo = hmm.MultinomialHMM(n_components=num_estados, n_iter=100, tol=1e-4, random_state=42)

# Definir las probabilidades iniciales (inicialización aleatoria)
modelo.startprob_ = np.array([0.6, 0.3, 0.1])  # Probabilidades iniciales de los estados

# Definir la matriz de transición entre estados
modelo.transmat_ = np.array([
    [0.7, 0.2, 0.1],  # Transiciones desde el estado 0
    [0.3, 0.5, 0.2],  # Transiciones desde el estado 1
    [0.2, 0.3, 0.5]   # Transiciones desde el estado 2
])

# Definir la matriz de emisión (probabilidades de observaciones en cada estado)
modelo.emissionprob_ = np.array([
    [0.5, 0.2, 0.2, 0.1],  # Emisiones desde el estado 0
    [0.1, 0.5, 0.3, 0.1],  # Emisiones desde el estado 1
    [0.2, 0.2, 0.3, 0.3]   # Emisiones desde el estado 2
])

# ============================================
# GENERAR SECUENCIAS DE DATOS
# ============================================
# Generar una secuencia de observaciones simulada
longitud_secuencia = 10
X, estados_ocultos = modelo.sample(n_samples=longitud_secuencia)

print("Secuencia de observaciones generada:", X.ravel())
print("Estados ocultos reales:", estados_ocultos)

# ============================================
# ENTRENAR EL MODELO CON DATOS
# ============================================
# Crear datos de entrenamiento (secuencias de observaciones)
datos_entrenamiento = np.array([[0, 1, 2, 3, 0, 1, 2, 3, 0, 1]]).T  # Secuencia de observaciones
longitudes = [len(datos_entrenamiento)]  # Longitud de la secuencia

# Entrenar el modelo
modelo.fit(datos_entrenamiento, lengths=longitudes)

# ============================================
# DECODIFICAR UNA NUEVA SECUENCIA
# ============================================
# Decodificar una nueva secuencia de observaciones
nueva_secuencia = np.array([[0, 1, 2, 3, 0, 1, 2, 3]]).T
log_prob, estados_decodificados = modelo.decode(nueva_secuencia, algorithm="viterbi")

print("Nueva secuencia de observaciones:", nueva_secuencia.ravel())
print("Estados ocultos decodificados:", estados_decodificados)
print("Log-verosimilitud de la secuencia:", log_prob)