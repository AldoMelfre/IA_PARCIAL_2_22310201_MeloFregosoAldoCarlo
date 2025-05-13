import numpy as np

# ============================================
# FUNCIONES DE ACTIVACIÓN
# ============================================
def sigmoide(z):
    """
    Función de activación Sigmoide.
    :param z: Entrada (numpy array o escalar).
    :return: Salida transformada.
    """
    return 1 / (1 + np.exp(-z))

def derivada_sigmoide(z):
    """
    Derivada de la función Sigmoide.
    :param z: Entrada (numpy array o escalar).
    :return: Derivada de la salida.
    """
    return sigmoide(z) * (1 - sigmoide(z))

# ============================================
# RED NEURONAL MULTICAPA
# ============================================
class RedMulticapa:
    def __init__(self, tamanos, tasa_aprendizaje=0.1, epochs=10000):
        """
        Inicializa la red neuronal multicapa.
        :param tamanos: Lista con el número de neuronas por capa (incluye entrada, ocultas y salida).
        :param tasa_aprendizaje: Tasa de aprendizaje para la actualización de pesos.
        :param epochs: Número de iteraciones de entrenamiento.
        """
        self.tamanos = tamanos
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epochs = epochs
        self.pesos = []  # Lista para almacenar los pesos
        self.sesgos = []  # Lista para almacenar los sesgos

        # Inicializar pesos y sesgos aleatoriamente
        for i in range(len(tamanos) - 1):
            self.pesos.append(np.random.randn(tamanos[i], tamanos[i + 1]))
            self.sesgos.append(np.random.randn(tamanos[i + 1]))

    def propagacion_adelante(self, X):
        """
        Realiza la propagación hacia adelante.
        :param X: Datos de entrada.
        :return: Salidas de cada capa.
        """
        activaciones = [X]  # Lista para almacenar las activaciones
        entradas = []  # Lista para almacenar las entradas ponderadas (z)

        for w, b in zip(self.pesos, self.sesgos):
            z = np.dot(activaciones[-1], w) + b  # Entrada ponderada
            entradas.append(z)
            activaciones.append(sigmoide(z))  # Aplicar función de activación

        return activaciones, entradas

    def propagacion_atras(self, X, y, activaciones, entradas):
        """
        Realiza la propagación hacia atrás (backpropagation).
        :param X: Datos de entrada.
        :param y: Etiquetas reales.
        :param activaciones: Salidas de cada capa.
        :param entradas: Entradas ponderadas (z) de cada capa.
        """
        # Inicializar gradientes
        gradientes_pesos = [np.zeros_like(w) for w in self.pesos]
        gradientes_sesgos = [np.zeros_like(b) for b in self.sesgos]

        # Calcular el error en la capa de salida
        error = activaciones[-1] - y  # Diferencia entre predicción y etiqueta real
        delta = error * derivada_sigmoide(entradas[-1])  # Gradiente de la capa de salida

        # Propagar el error hacia atrás
        for i in reversed(range(len(self.pesos))):
            gradientes_pesos[i] = np.dot(activaciones[i].T, delta)
            gradientes_sesgos[i] = np.sum(delta, axis=0)
            if i > 0:
                delta = np.dot(delta, self.pesos[i].T) * derivada_sigmoide(entradas[i - 1])

        return gradientes_pesos, gradientes_sesgos

    def entrenar(self, X, y):
        """
        Entrena la red neuronal.
        :param X: Datos de entrada.
        :param y: Etiquetas reales.
        """
        for _ in range(self.epochs):
            activaciones, entradas = self.propagacion_adelante(X)
            gradientes_pesos, gradientes_sesgos = self.propagacion_atras(X, y, activaciones, entradas)

            # Actualizar pesos y sesgos
            for i in range(len(self.pesos)):
                self.pesos[i] -= self.tasa_aprendizaje * gradientes_pesos[i]
                self.sesgos[i] -= self.tasa_aprendizaje * gradientes_sesgos[i]

    def predecir(self, X):
        """
        Realiza predicciones con la red neuronal.
        :param X: Datos de entrada.
        :return: Predicciones.
        """
        activaciones, _ = self.propagacion_adelante(X)
        return activaciones[-1]

# ============================================
# EJEMPLO: RED MULTICAPA
# ============================================
# Datos de ejemplo (XOR lógico)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# Crear y entrenar la red neuronal
red = RedMulticapa(tamanos=[2, 4, 1], tasa_aprendizaje=0.1, epochs=10000)
red.entrenar(X, y)

# Realizar predicciones
predicciones = red.predecir(X)
print("Predicciones:")
print(predicciones)