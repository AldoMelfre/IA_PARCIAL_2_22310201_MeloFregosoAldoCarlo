import numpy as np

# ============================================
# CLASIFICADOR NAÏVE BAYES
# ============================================
class NaiveBayes:
    def __init__(self):
        self.prior = {}  # Probabilidades previas P(C)
        self.likelihood = {}  # Verosimilitud P(x_i | C)
        self.classes = []  # Clases únicas

    def entrenar(self, X, y):
        """
        Entrena el clasificador Naïve Bayes.
        :param X: Matriz de características (numpy array).
        :param y: Vector de etiquetas (numpy array).
        """
        self.classes = np.unique(y)  # Obtener las clases únicas
        num_muestras, num_caracteristicas = X.shape

        # Calcular las probabilidades previas P(C)
        for c in self.classes:
            X_c = X[y == c]  # Filtrar las muestras de la clase c
            self.prior[c] = len(X_c) / num_muestras  # P(C)
            self.likelihood[c] = {}

            # Calcular la verosimilitud P(x_i | C) para cada característica
            for i in range(num_caracteristicas):
                valores, conteos = np.unique(X_c[:, i], return_counts=True)
                self.likelihood[c][i] = {v: conteos[j] / len(X_c) for j, v in enumerate(valores)}

    def predecir(self, X):
        """
        Predice las clases para un conjunto de datos.
        :param X: Matriz de características (numpy array).
        :return: Vector de predicciones.
        """
        predicciones = []

        for muestra in X:
            probabilidades = {}

            # Calcular P(C | X) para cada clase
            for c in self.classes:
                prob = self.prior[c]  # P(C)
                for i, valor in enumerate(muestra):
                    prob *= self.likelihood[c][i].get(valor, 1e-6)  # P(x_i | C)
                probabilidades[c] = prob

            # Asignar la clase con la mayor probabilidad
            predicciones.append(max(probabilidades, key=probabilidades.get))

        return np.array(predicciones)

# ============================================
# EJEMPLO: CLASIFICADOR NAÏVE BAYES
# ============================================
# Datos de ejemplo (características categóricas)
X = np.array([
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0],
    [1, 1],
    [0, 0]
])

# Etiquetas de clase
y = np.array([1, 1, 0, 0, 1, 0])

# Crear y entrenar el clasificador
nb = NaiveBayes()
nb.entrenar(X, y)

# Nuevas muestras para clasificar
X_nuevas = np.array([
    [1, 0],
    [0, 1],
    [1, 1]
])

# Realizar predicciones
predicciones = nb.predecir(X_nuevas)

# Mostrar los resultados
print("Predicciones:", predicciones)