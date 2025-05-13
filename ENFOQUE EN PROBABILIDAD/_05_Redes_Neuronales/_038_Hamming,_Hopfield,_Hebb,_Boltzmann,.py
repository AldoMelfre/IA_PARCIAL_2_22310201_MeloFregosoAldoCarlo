import numpy as np

# ============================================
# RED DE HAMMING
# ============================================
class RedHamming:
    def __init__(self, patrones):
        """
        Inicializa la red de Hamming.
        :param patrones: Lista de patrones almacenados.
        """
        self.patrones = np.array(patrones)

    def reconocer(self, entrada):
        """
        Encuentra el patrón más cercano a la entrada.
        :param entrada: Vector de entrada.
        :return: Patrón más cercano.
        """
        distancias = np.sum(np.abs(self.patrones - entrada), axis=1)  # Distancia de Hamming
        return self.patrones[np.argmin(distancias)]

# ============================================
# RED DE HOPFIELD
# ============================================
class RedHopfield:
    def __init__(self):
        """
        Inicializa la red de Hopfield.
        """
        self.pesos = None

    def entrenar(self, patrones):
        """
        Entrena la red utilizando los patrones dados.
        :param patrones: Lista de patrones binarios.
        """
        n = patrones.shape[1]
        self.pesos = np.zeros((n, n))
        for p in patrones:
            self.pesos += np.outer(p, p)
        np.fill_diagonal(self.pesos, 0)  # Evitar auto-conexiones

    def recuperar(self, entrada, iteraciones=10):
        """
        Recupera un patrón a partir de una entrada.
        :param entrada: Vector de entrada.
        :param iteraciones: Número de iteraciones para actualizar.
        :return: Patrón recuperado.
        """
        salida = entrada.copy()
        for _ in range(iteraciones):
            salida = np.sign(np.dot(salida, self.pesos))
        return salida

# ============================================
# REGLA DE HEBB
# ============================================
class ReglaHebb:
    def __init__(self):
        """
        Inicializa el modelo basado en la regla de Hebb.
        """
        self.pesos = None

    def entrenar(self, X, y):
        """
        Entrena los pesos utilizando la regla de Hebb.
        :param X: Matriz de características.
        :param y: Vector de etiquetas.
        """
        self.pesos = np.dot(X.T, y)

    def predecir(self, X):
        """
        Realiza predicciones.
        :param X: Matriz de características.
        :return: Predicciones.
        """
        return np.sign(np.dot(X, self.pesos))

# ============================================
# MÁQUINA DE BOLTZMANN
# ============================================
class MaquinaBoltzmann:
    def __init__(self, n_visible, n_ocultas):
        """
        Inicializa la máquina de Boltzmann.
        :param n_visible: Número de unidades visibles.
        :param n_ocultas: Número de unidades ocultas.
        """
        self.n_visible = n_visible
        self.n_ocultas = n_ocultas
        self.pesos = np.random.randn(n_visible, n_ocultas) * 0.1

    def energia(self, visible, oculta):
        """
        Calcula la energía del sistema.
        :param visible: Estado de las unidades visibles.
        :param oculta: Estado de las unidades ocultas.
        :return: Energía del sistema.
        """
        return -np.dot(visible, np.dot(self.pesos, oculta))

# ============================================
# EJEMPLOS
# ============================================
# Red de Hamming
print("=== Red de Hamming ===")
hamming = RedHamming(patrones=[[1, 0, 1], [0, 1, 0]])

# ============================================
# RED DE HAMMING
# ============================================
class RedHamming:
    def __init__(self, patrones):
        """
        Inicializa la red de Hamming.
        :param patrones: Lista de patrones almacenados.
        """
        self.patrones = np.array(patrones)

    def reconocer(self, entrada):
        """
        Encuentra el patrón más cercano a la entrada.
        :param entrada: Vector de entrada.
        :return: Patrón más cercano.
        """
        distancias = np.sum(np.abs(self.patrones - entrada), axis=1)  # Distancia de Hamming
        return self.patrones[np.argmin(distancias)]

# ============================================
# RED DE HOPFIELD
# ============================================
class RedHopfield:
    def __init__(self):
        """
        Inicializa la red de Hopfield.
        """
        self.pesos = None

    def entrenar(self, patrones):
        """
        Entrena la red utilizando los patrones dados.
        :param patrones: Lista de patrones binarios.
        """
        n = patrones.shape[1]
        self.pesos = np.zeros((n, n))
        for p in patrones:
            self.pesos += np.outer(p, p)
        np.fill_diagonal(self.pesos, 0)  # Evitar auto-conexiones

    def recuperar(self, entrada, iteraciones=10):
        """
        Recupera un patrón a partir de una entrada.
        :param entrada: Vector de entrada.
        :param iteraciones: Número de iteraciones para actualizar.
        :return: Patrón recuperado.
        """
        salida = entrada.copy()
        for _ in range(iteraciones):
            salida = np.sign(np.dot(salida, self.pesos))
        return salida

# ============================================
# REGLA DE HEBB
# ============================================
class ReglaHebb:
    def __init__(self):
        """
        Inicializa el modelo basado en la regla de Hebb.
        """
        self.pesos = None

    def entrenar(self, X, y):
        """
        Entrena los pesos utilizando la regla de Hebb.
        :param X: Matriz de características.
        :param y: Vector de etiquetas.
        """
        self.pesos = np.dot(X.T, y)

    def predecir(self, X):
        """
        Realiza predicciones.
        :param X: Matriz de características.
        :return: Predicciones.
        """
        return np.sign(np.dot(X, self.pesos))

# ============================================
# MÁQUINA DE BOLTZMANN
# ============================================
class MaquinaBoltzmann:
    def __init__(self, n_visible, n_ocultas):
        """
        Inicializa la máquina de Boltzmann.
        :param n_visible: Número de unidades visibles.
        :param n_ocultas: Número de unidades ocultas.
        """
        self.n_visible = n_visible
        self.n_ocultas = n_ocultas
        self.pesos = np.random.randn(n_visible, n_ocultas) * 0.1

    def energia(self, visible, oculta):
        """
        Calcula la energía del sistema.
        :param visible: Estado de las unidades visibles.
        :param oculta: Estado de las unidades ocultas.
        :return: Energía del sistema.
        """
        return -np.dot(visible, np.dot(self.pesos, oculta))

# ============================================
# EJEMPLOS
# ============================================
# Red de Hamming
print("=== Red de Hamming ===")
hamming = RedHamming(patrones=[[1, 0, 1],])