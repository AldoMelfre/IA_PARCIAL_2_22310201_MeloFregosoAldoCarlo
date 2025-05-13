import numpy as np  # Importa NumPy para realizar operaciones matemáticas y trabajar con probabilidades.
from collections import defaultdict, Counter  # Importa estructuras para contar frecuencias y manejar datos.

# ============================================
# MODELO PROBABILÍSTICO DEL LENGUAJE: N-GRAMAS
# ============================================
class ModeloLenguaje:
    def __init__(self, n=2):
        """
        Inicializa el modelo de lenguaje basado en n-gramas.
        :param n: Tamaño del n-grama (por defecto 2 para bigramas).
        """
        self.n = n  # Define el tamaño del n-grama (por ejemplo, 2 para bigramas, 3 para trigramas).
        self.ngramas = defaultdict(Counter)  # Almacena las frecuencias de los n-gramas en un diccionario.
        self.total_ngrams = Counter()  # Almacena las frecuencias totales de los contextos.

    def entrenar(self, corpus):
        """
        Entrena el modelo de lenguaje con un corpus.
        :param corpus: Lista de oraciones (cada oración es una lista de palabras).
        """
        for oracion in corpus:
            # Añade tokens de inicio (<s>) y fin (</s>) para marcar los límites de las oraciones.
            oracion = ["<s>"] * (self.n - 1) + oracion + ["</s>"]
            for i in range(len(oracion) - self.n + 1):
                # Divide la oración en contexto (n-1 palabras) y palabra actual.
                contexto = tuple(oracion[i:i + self.n - 1])  # Contexto del n-grama.
                palabra = oracion[i + self.n - 1]  # Palabra actual.
                self.ngramas[contexto][palabra] += 1  # Incrementa la frecuencia del n-grama.
                self.total_ngrams[contexto] += 1  # Incrementa la frecuencia del contexto.

    def probabilidad(self, contexto, palabra):
        """
        Calcula la probabilidad de una palabra dado un contexto.
        :param contexto: Contexto (n-1 palabras).
        :param palabra: Palabra actual.
        :return: Probabilidad condicional P(palabra | contexto).
        """
        contexto = tuple(contexto)  # Asegura que el contexto sea una tupla (clave del diccionario).
        # Calcula la probabilidad con suavizado de Laplace para evitar probabilidades cero.
        return (self.ngramas[contexto][palabra] + 1) / (self.total_ngrams[contexto] + len(self.ngramas))

    def generar(self, longitud=10):
        """
        Genera una secuencia de palabras utilizando el modelo de lenguaje.
        :param longitud: Longitud de la secuencia generada.
        :return: Lista de palabras generadas.
        """
        contexto = ["<s>"] * (self.n - 1)  # Inicializa el contexto con tokens de inicio.
        resultado = []  # Lista para almacenar las palabras generadas.

        for _ in range(longitud):
            # Obtiene las palabras posibles y sus probabilidades condicionales.
            palabras = list(self.ngramas[tuple(contexto)].keys())
            probabilidades = [self.probabilidad(contexto, palabra) for palabra in palabras]
            # Selecciona una palabra basada en las probabilidades.
            palabra = np.random.choice(palabras, p=probabilidades)
            if palabra == "</s>":  # Detiene la generación si se alcanza el token de fin.
                break
            resultado.append(palabra)  # Añade la palabra generada al resultado.
            contexto = contexto[1:] + [palabra]  # Actualiza el contexto para la siguiente iteración.

        return resultado  # Devuelve la secuencia generada.

# ============================================
# EJEMPLO: ENTRENAMIENTO Y GENERACIÓN
# ============================================
# Corpus de ejemplo
corpus = [
    ["el", "gato", "come", "pescado"],  # Primera oración del corpus.
    ["el", "perro", "ladra"],  # Segunda oración del corpus.
    ["el", "gato", "duerme"],  # Tercera oración del corpus.
    ["el", "perro", "come", "hueso"]  # Cuarta oración del corpus.
]

# Crear y entrenar el modelo de lenguaje
modelo = ModeloLenguaje(n=2)  # Crea un modelo basado en bigramas (n=2).
modelo.entrenar(corpus)  # Entrena el modelo con el corpus.

# Calcular probabilidades
contexto = ["el"]  # Contexto para calcular la probabilidad.
palabra = "gato"  # Palabra cuya probabilidad queremos calcular.
# Imprime la probabilidad condicional P('gato' | 'el').
print(f"P('{palabra}' | '{contexto}') =", modelo.probabilidad(contexto, palabra))

# Generar texto
texto_generado = modelo.generar(longitud=10)  # Genera una secuencia de 10 palabras.
# Imprime el texto generado.
print("Texto generado:", " ".join(texto_generado))