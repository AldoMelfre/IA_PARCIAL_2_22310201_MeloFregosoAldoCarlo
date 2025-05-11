import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage

# ============================================
# 1. k-NN (k-Nearest Neighbors)
# ============================================
# Generar datos de ejemplo para clasificación
X, y = make_classification(n_samples=200, n_features=2, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo k-NN
k = 3
knn = KNeighborsClassifier(n_neighbors=k)

# Entrenar el modelo
knn.fit(X_train, y_train)

# Predecir y evaluar
y_pred = knn.predict(X_test)
print("Precisión del modelo k-NN:", accuracy_score(y_test, y_pred))

# Visualizar los datos y la clasificación
plt.figure(figsize=(8, 6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm', label='Predicciones')
plt.title("Clasificación con k-NN")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.legend()
plt.show()

# ============================================
# 2. k-Medias (k-Means)
# ============================================
# Generar datos de ejemplo para clustering
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.6, random_state=42)

# Crear el modelo k-Means
kmeans = KMeans(n_clusters=3, random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Visualizar los resultados
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis', marker='o', label='Puntos')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x', s=200, label='Centroides')
plt.title("Agrupamiento con k-Means")
plt.legend()
plt.show()

# ============================================
# 3. Clustering Jerárquico
# ============================================
# Generar datos de ejemplo para clustering jerárquico
X, _ = make_blobs(n_samples=100, centers=3, cluster_std=0.6, random_state=42)

# Crear el modelo de clustering jerárquico
Z = linkage(X, method='ward')

# Visualizar el dendrograma
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title("Dendrograma - Clustering Jerárquico")
plt.xlabel("Puntos de datos")
plt.ylabel("Distancia Euclidiana")
plt.show()