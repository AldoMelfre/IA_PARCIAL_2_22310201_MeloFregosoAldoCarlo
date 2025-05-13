import numpy as np
import matplotlib.pyplot as plt

# ============================================
# MAPAS AUTOORGANIZADOS DE KOHONEN (SOM)
# ============================================
class SOM:
    def __init__(self, filas, columnas, dimensiones, tasa_aprendizaje=0.5, epochs=1000):
        """
        Inicializa el mapa autoorganizado.
        :param filas: Número de filas en la cuadrícula de neuronas.
        :param columnas: Número de columnas en la cuadrícula de neuronas.
        :param dimensiones: Dimensiones del espacio de entrada.
        :param tasa_aprendizaje: Tasa de aprendizaje inicial.
        :param epochs: Número de iteraciones de entrenamiento.
        """
        self.filas = filas
        self.columnas = columnas
        self.dimensiones = dimensiones
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epochs = epochs
        self.pesos = np.random.rand(filas, columnas, dimensiones)  # Inicializar pesos aleatorios

    def encontrar_bmu(self, muestra):
        """
        Encuentra la neurona ganadora (BMU).
        :param muestra: Punto de entrada.
        :return: Coordenadas de la BMU.
        """
        distancias = np.linalg.norm(self.pesos - muestra, axis=2)  # Distancia euclidiana
        return np.unravel_index(np.argmin(distancias), (self.filas, self.columnas))

    def actualizar_pesos(self, muestra, bmu, iteracion):
        """
        Actualiza los pesos de la BMU y sus vecinas.
        :param muestra: Punto de entrada.
        :param bmu: Coordenadas de la BMU.
        :param iteracion: Iteración actual.
        """
        radio_inicial = max(self.filas, self.columnas) / 2  # Radio inicial de vecindad
        radio = radio_inicial * np.exp(-iteracion / self.epochs)  # Reducir radio con el tiempo
        tasa = self.tasa_aprendizaje * np.exp(-iteracion / self.epochs)  # Reducir tasa de aprendizaje

        for i in range(self.filas):
            for j in range(self.columnas):
                distancia = np.linalg.norm(np.array([i, j]) - np.array(bmu))  # Distancia a la BMU
                if distancia <= radio:
                    influencia = np.exp(-distancia**2 / (2 * (radio**2)))  # Función de vecindad
                    self.pesos[i, j] += tasa * influencia * (muestra - self.pesos[i, j])  # Actualizar pesos

    def entrenar(self, datos):
        """
        Entrena el SOM con los datos de entrada.
        :param datos: Conjunto de datos de entrada.
        """
        for iteracion in range(self.epochs):
            muestra = datos[np.random.randint(0, len(datos))]  # Seleccionar muestra aleatoria
            bmu = self.encontrar_bmu(muestra)  # Encontrar la BMU
            self.actualizar_pesos(muestra, bmu, iteracion)  # Actualizar pesos

    def graficar(self):
        """
        Grafica el SOM en 2D.
        """
        plt.imshow(self.pesos[:, :, 0], cmap='coolwarm')  # Graficar la primera dimensión de los pesos
        plt.colorbar()
        plt.title("Mapa Autoorganizado (SOM)")
        plt.show()

# ============================================
# EJEMPLO: ENTRENAMIENTO DE UN SOM
# ============================================
# Generar datos de ejemplo
datos = np.random.rand(100, 3)  # 100 puntos en un espacio de 3 dimensiones

# Crear y entrenar el SOM
som = SOM(filas=10, columnas=10, dimensiones=3, tasa_aprendizaje=0.5, epochs=500)
som.entrenar(datos)

# Graficar el SOM
som.graficar()