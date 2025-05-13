import random  # Importa la biblioteca random para seleccionar palabras basadas en probabilidades.

# ============================================
# TRADUCCIÓN AUTOMÁTICA ESTADÍSTICA
# ============================================
class TraductorEstadistico:
    def __init__(self):
        """
        Inicializa el traductor estadístico con un diccionario probabilístico.
        """
        self.diccionario = {}  # Diccionario para almacenar las probabilidades de traducción.

    def entrenar(self, corpus_paralelo):
        """
        Entrena el modelo de traducción con un corpus paralelo.
        :param corpus_paralelo: Lista de pares (oración en idioma origen, oración en idioma destino).
        """
        for origen, destino in corpus_paralelo:  # Itera sobre cada par de oraciones en el corpus paralelo.
            palabras_origen = origen.split()  # Divide la oración en idioma origen en palabras.
            palabras_destino = destino.split()  # Divide la oración en idioma destino en palabras.

            for palabra_origen in palabras_origen:  # Itera sobre cada palabra en el idioma origen.
                if palabra_origen not in self.diccionario:  # Si la palabra no está en el diccionario:
                    self.diccionario[palabra_origen] = {}  # Inicializa un diccionario para las traducciones.

                for palabra_destino in palabras_destino:  # Itera sobre cada palabra en el idioma destino.
                    if palabra_destino not in self.diccionario[palabra_origen]:  # Si no existe la traducción:
                        self.diccionario[palabra_origen][palabra_destino] = 0  # Inicializa la frecuencia en 0.
                    self.diccionario[palabra_origen][palabra_destino] += 1  # Incrementa la frecuencia.

        # Normalizar las probabilidades
        for palabra_origen in self.diccionario:  # Itera sobre cada palabra en el idioma origen.
            total = sum(self.diccionario[palabra_origen].values())  # Suma las frecuencias de todas las traducciones.
            for palabra_destino in self.diccionario[palabra_origen]:  # Itera sobre las traducciones posibles.
                self.diccionario[palabra_origen][palabra_destino] /= total  # Calcula la probabilidad normalizada.

    def traducir(self, texto_origen):
        """
        Traduce un texto del idioma origen al idioma destino.
        :param texto_origen: Texto en el idioma origen.
        :return: Traducción al idioma destino.
        """
        palabras_origen = texto_origen.split()  # Divide el texto de entrada en palabras.
        traduccion = []  # Lista para almacenar las palabras traducidas.

        for palabra_origen in palabras_origen:  # Itera sobre cada palabra en el texto de entrada.
            if palabra_origen in self.diccionario:  # Si la palabra tiene traducción en el diccionario:
                # Seleccionar la palabra destino con mayor probabilidad
                palabras_destino = list(self.diccionario[palabra_origen].keys())  # Obtiene las palabras destino.
                probabilidades = list(self.diccionario[palabra_origen].values())  # Obtiene las probabilidades.
                palabra_destino = random.choices(palabras_destino, probabilidades)[0]  # Selecciona una palabra basada en las probabilidades.
                traduccion.append(palabra_destino)  # Añade la palabra traducida a la lista.
            else:
                # Si no hay traducción, mantener la palabra original
                traduccion.append(palabra_origen)  # Añade la palabra original si no hay traducción.

        return " ".join(traduccion)  # Une las palabras traducidas en una sola cadena y la devuelve.

# ============================================
# EJEMPLO: TRADUCCIÓN AUTOMÁTICA ESTADÍSTICA
# ============================================
# Corpus paralelo de ejemplo (idioma origen -> idioma destino)
corpus_paralelo = [
    ("el gato come pescado", "the cat eats fish"),  # Par de oraciones alineadas (español -> inglés).
    ("el perro ladra", "the dog barks"),  # Otro par de oraciones.
    ("el gato duerme", "the cat sleeps"),  # Otro par de oraciones.
    ("el perro come hueso", "the dog eats bone")  # Otro par de oraciones.
]

# Crear y entrenar el traductor
traductor = TraductorEstadistico()  # Crea una instancia del traductor estadístico.
traductor.entrenar(corpus_paralelo)  # Entrena el modelo con el corpus paralelo.

# Traducir texto
texto_origen = "el gato come"  # Texto en español que se desea traducir.
traduccion = traductor.traducir(texto_origen)  # Traduce el texto al inglés.
print(f"Texto original: {texto_origen}")  # Imprime el texto original.
print(f"Traducción: {traduccion}")  # Imprime la traducción generada.