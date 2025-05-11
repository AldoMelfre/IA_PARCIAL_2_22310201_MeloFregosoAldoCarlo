import numpy as np
from scipy.stats import multivariate_normal

class EMAlgorithm:
    def __init__(self, num_clusters, max_iter=100, tol=1e-6):
        self.num_clusters = num_clusters  # Número de clusters (componentes gaussianas)
        self.max_iter = max_iter  # Número máximo de iteraciones
        self.tol = tol  # Tolerancia para la convergencia

    def inicializar_parametros(self, X):
        """
        Inicializa los parámetros del modelo: pesos, medias y covarianzas.
        """
        num_muestras, num_caracteristicas = X.shape
        self.pesos = np.ones(self.num_clusters) / self.num_clusters  # Pesos iniciales
        self.medias = X[np.random.choice(num_muestras, self.num_clusters, replace=False)]  # Medias iniciales
        self.covarianzas = np.array([np.eye(num_caracteristicas) for _ in range(self.num_clusters)])  # Covarianzas iniciales

    def expectation(self, X):
        """
        Paso E: Calcula las responsabilidades (probabilidades posteriores).
        """
        num_muestras = X.shape[0]
        self.responsabilidades = np.zeros((num_muestras, self.num_clusters))

        for k in range(self.num_clusters):
            self.responsabilidades[:, k] = self.pesos[k] * multivariate_normal.pdf(X, mean=self.medias[k], cov=self.covarianzas[k])

        # Normalizar para obtener probabilidades
        self.responsabilidades /= self.responsabilidades.sum(axis=1, keepdims=True)

    def maximization(self, X):
        """
        Paso M: Actualiza los parámetros del modelo.
        """
        num_muestras = X.shape[0]
        Nk = self.responsabilidades.sum(axis=0)  # Suma de responsabilidades para cada cluster

        # Actualizar pesos
        self.pesos = Nk / num_muestras

        # Actualizar medias
        self.medias = np.dot(self.responsabilidades.T, X) / Nk[:, np.newaxis]

        # Actualizar covarianzas
        for k in range(self.num_clusters):
            X_centrado = X - self.medias[k]
            self.covarianzas[k] = np.dot((self.responsabilidades[:, k][:, np.newaxis] * X_centrado).T, X_centrado) / Nk[k]

    def log_verosimilitud(self, X):
        """
        Calcula la log-verosimilitud del modelo.
        """
        log_likelihood = 0
        for k in range(self.num_clusters):
            log_likelihood += self.pesos[k] * multivariate_normal.pdf(X, mean=self.medias[k], cov=self.covarianzas[k])
        return np.sum(np.log(log_likelihood))

    def ajustar(self, X):
        """
        Ajusta el modelo a los datos utilizando el algoritmo EM.
        """
        self.inicializar_parametros(X)
        log_likelihood_anterior = None

        for iteracion in range(self.max_iter):
            self.expectation(X)
            self.maximization(X)
            log_likelihood_actual = self.log_verosimilitud(X)

            # Verificar convergencia
            if log_likelihood_anterior is not None and abs(log_likelihood_actual - log_likelihood_anterior) < self.tol:
                print(f"Convergencia alcanzada en la iteración {iteracion}")
                break

            log_likelihood_anterior = log_likelihood_actual

    def predecir(self, X):
        """
        Asigna cada muestra al cluster con mayor responsabilidad.
        """
        self.expectation(X)
        return np.argmax(self.responsabilidades, axis=1)

# ============================================
# EJEMPLO: ALGORITMO EM PARA GMM
# ============================================
# Generar datos de ejemplo
np.random.seed(42)
X1 = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 100)
X2 = np.random.multivariate_normal([3, 3], [[1, -0.5], [-0.5, 1]], 100)
X = np.vstack([X1, X2])

# Aplicar el algoritmo EM
em = EMAlgorithm(num_clusters=2)
em.ajustar(X)

# Predecir las etiquetas
etiquetas = em.predecir(X)
print("Etiquetas predichas:", etiquetas)