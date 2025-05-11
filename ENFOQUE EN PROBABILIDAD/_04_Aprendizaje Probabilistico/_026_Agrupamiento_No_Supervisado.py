import numpy as np
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, num_clusters, max_iter=100, tol=1e-4):
        """
        Inicializa el algoritmo K-Means.
        :param num_clusters: Número de clusters (k).
        :param max_iter: Número máximo de iteraciones.
        :param tol: Tolerancia para la convergencia.
        """
        self.num_clusters = num_clusters
        self.max_iter = max_iter
        self.tol = tol

    def inicializar_centroides(self, X):
        """
        Inicializa los centroides seleccionando aleatoriamente puntos del conjunto de datos.
        """
        indices = np.random.choice(X.shape[0], self.num_clusters, replace=False)
        return X[indices]

    def asignar_clusters(self, X, centroides):
        """
        Asigna cada punto al cluster más cercano.
        """
        distancias = np.linalg.norm(X[:, np.newaxis] - centroides, axis=2)
        return np.argmin(distancias, axis=1)

    def actualizar_centroides(self, X, etiquetas):
        """
        Calcula los nuevos centroides como el promedio de los puntos asignados a cada cluster.
        """
        nuevos_centroides = []
        for k in range(self.num_clusters):
            puntos_cluster = X[etiquetas == k]
            if len(puntos_cluster) > 0:
                nuevos_centroides.append(puntos_cluster.mean(axis=0))
            else:
                # Si un cluster queda vacío, se reasigna aleatoriamente
                nuevos_centroides.append(X[np.random.choice(X.shape[0])])
        return np.array(nuevos_centroides)

    def ajustar(self, X):
        """
        Ajusta el modelo K-Means a los datos.
        :param X: Matriz de características (numpy array).
        :return: Etiquetas de los clusters para cada punto.
        """
        # Inicializar los centroides
        self.centroides = self.inicializar_centroides(X)

        for i in range(self.max_iter):
            # Asignar puntos a los clusters más cercanos
            etiquetas = self.asignar_clusters(X, self.centroides)

            # Actualizar los centroides
            nuevos_centroides = self.actualizar_centroides(X, etiquetas)

            # Verificar convergencia
            if np.all(np.abs(nuevos_centroides - self.centroides) < self.tol):
                print(f"Convergencia alcanzada en la iteración {i}")
                break

            self.centroides = nuevos_centroides

        return etiquetas

    def predecir(self, X):
        """
        Predice el cluster más cercano para nuevos datos.
        """
        return self.asignar_clusters(X, self.centroides)

# ============================================
# EJEMPLO: K-MEANS PARA AGRUPAMIENTO
# ============================================
# Generar datos de ejemplo
np.random.seed(42)
X1 = np.random.normal(loc=[2, 2], scale=0.5, size=(100, 2))
X2 = np.random.normal(loc=[8, 8], scale=0.5, size=(100, 2))
X3 = np.random.normal(loc=[5, 5], scale=0.5, size=(100, 2))
X = np.vstack([X1, X2, X3])

# Aplicar K-Means
kmeans = KMeans(num_clusters=3)
etiquetas = kmeans.ajustar(X)

# Visualizar los resultados
plt.scatter(X[:, 0], X[:, 1], c=etiquetas, cmap='viridis', marker='o', label='Puntos')
plt.scatter(kmeans.centroides[:, 0], kmeans.centroides[:, 1], c='red', marker='x', s=200, label='Centroides')
plt.title("Agrupamiento con K-Means")
plt.legend()
plt.show()