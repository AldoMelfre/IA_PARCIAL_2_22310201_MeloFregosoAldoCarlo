# ============================================
# PERCEPTRÓN
# ============================================
# El Perceptrón es el modelo más simple de red neuronal.
# Es un clasificador lineal que utiliza una función de activación escalón para decidir entre dos clases.
# Fue introducido por Frank Rosenblatt en 1958.
# Limitación: Solo puede resolver problemas linealmente separables.

class Perceptron:
    def __init__(self, eta=0.01, epochs=100):
        self.eta = eta  # Tasa de aprendizaje
        self.epochs = epochs  # Número de iteraciones

    def entrenar(self, X, y):
        """
        Entrena el modelo Perceptrón.
        :param X: Matriz de características (numpy array).
        :param y: Vector de etiquetas (numpy array).
        """
        self.w = np.zeros(X.shape[1])  # Inicializar pesos
        self.b = 0  # Inicializar sesgo

        for _ in range(self.epochs):
            for xi, yi in zip(X, y):
                y_pred = self.predecir(xi)
                self.w += self.eta * (yi - y_pred) * xi  # Actualizar pesos
                self.b += self.eta * (yi - y_pred)  # Actualizar sesgo

    def predecir(self, X):
        """
        Realiza predicciones.
        :param X: Vector o matriz de características.
        :return: Predicciones (1 o -1).
        """
        return np.where(np.dot(X, self.w) + self.b >= 0, 1, -1)

# ============================================
# ADALINE (Adaptive Linear Neuron)
# ============================================
# ADALINE es una mejora del Perceptrón que utiliza una función de activación lineal.
# Introducido por Bernard Widrow y Marcian Hoff en 1960.
# Utiliza el error cuadrático medio (MSE) como criterio de aprendizaje.
# Ventaja: Puede aprender incluso si los datos no son perfectamente linealmente separables.

class Adaline:
    def __init__(self, eta=0.01, epochs=100):
        self.eta = eta  # Tasa de aprendizaje
        self.epochs = epochs  # Número de iteraciones

    def entrenar(self, X, y):
        """
        Entrena el modelo ADALINE.
        :param X: Matriz de características (numpy array).
        :param y: Vector de etiquetas (numpy array).
        """
        self.w = np.zeros(X.shape[1])  # Inicializar pesos
        self.b = 0  # Inicializar sesgo
        self.losses = []  # Lista para almacenar el error cuadrático medio

        for _ in range(self.epochs):
            y_pred = self.activacion(X)
            errores = y - y_pred
            self.w += self.eta * np.dot(X.T, errores)  # Actualizar pesos
            self.b += self.eta * errores.sum()  # Actualizar sesgo
            self.losses.append((errores**2).mean())  # Calcular el error cuadrático medio

    def activacion(self, X):
        """
        Calcula la salida lineal.
        :param X: Vector o matriz de características.
        :return: Salida lineal.
        """
        return np.dot(X, self.w) + self.b

# ============================================
# MADALINE (Multiple ADALINE)
# ============================================
# MADALINE es una red neuronal multicapa que utiliza múltiples unidades ADALINE.
# Fue introducido por Bernard Widrow en 1962.
# Es capaz de resolver problemas no lineales mediante el uso de múltiples capas.
# Utiliza un algoritmo de entrenamiento llamado "Regla de Correlación de Mínimos".

class Madaline:
    def __init__(self):
        """
        Inicializa el modelo MADALINE.
        """
        pass  # Implementación de MADALINE no incluida en este ejemplo.

# ============================================
# EJEMPLO: PERCEPTRÓN Y ADALINE
# ============================================
# Datos de ejemplo (AND lógico)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([-1, -1, -1, 1])  # Etiquetas (1 para True, -1 para False)

# Entrenar y probar el Perceptrón
print("=== Perceptrón ===")
perceptron = Perceptron(eta=0.1, epochs=10)
perceptron.entrenar(X, y)
print("Pesos:", perceptron.w)
print("Sesgo:", perceptron.b)
print("Predicciones:", perceptron.predecir(X))

# Entrenar y probar el ADALINE
print("\n=== ADALINE ===")
adaline = Adaline(eta=0.1, epochs=10)
adaline.entrenar(X, y)
print("Pesos:", adaline.w)
print("Sesgo:", adaline.b)
print("Predicciones:", np.where(adaline.activacion(X) >= 0, 1, -1))