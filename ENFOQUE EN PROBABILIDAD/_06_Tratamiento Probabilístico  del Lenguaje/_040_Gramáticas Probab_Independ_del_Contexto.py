import random

# ============================================
# GRAMÁTICAS PROBABILÍSTICAS INDEPENDIENTES DEL CONTEXTO (PCFG)
# ============================================
class PCFG:
    def __init__(self):
        """
        Inicializa la gramática probabilística.
        """
        self.reglas = {}  # Diccionario para almacenar las reglas de producción y sus probabilidades.

    def agregar_regla(self, no_terminal, producciones):
        """
        Agrega una regla de producción a la gramática.
        :param no_terminal: Símbolo no terminal (por ejemplo, 'S').
        :param producciones: Lista de tuplas (producción, probabilidad).
        """
        self.reglas[no_terminal] = producciones

    def generar(self, simbolo):
        """
        Genera una oración a partir de un símbolo no terminal.
        :param simbolo: Símbolo no terminal inicial.
        :return: Oración generada como una lista de palabras.
        """
        if simbolo not in self.reglas:  # Si es un símbolo terminal, devolverlo directamente.
            return [simbolo]

        # Seleccionar una producción basada en las probabilidades.
        producciones = self.reglas[simbolo]
        produccion = random.choices(
            [p[0] for p in producciones],  # Producciones posibles.
            [p[1] for p in producciones]  # Probabilidades asociadas.
        )[0]

        # Generar recursivamente para cada símbolo en la producción.
        resultado = []
        for s in produccion:
            resultado.extend(self.generar(s))
        return resultado

# ============================================
# EJEMPLO: GRAMÁTICA PROBABILÍSTICA
# ============================================
# Crear una gramática probabilística
gramatica = PCFG()

# Agregar reglas de producción
gramatica.agregar_regla('S', [
    (['NP', 'VP'], 1.0)  # La oración (S) se expande en un sintagma nominal (NP) y un sintagma verbal (VP).
])

gramatica.agregar_regla('NP', [
    (['Det', 'N'], 0.8),  # El sintagma nominal (NP) se expande en un determinante (Det) y un sustantivo (N).
    (['N'], 0.2)          # O directamente en un sustantivo (N).
])

gramatica.agregar_regla('VP', [
    (['V', 'NP'], 0.6),   # El sintagma verbal (VP) se expande en un verbo (V) y un sintagma nominal (NP).
    (['V'], 0.4)          # O directamente en un verbo (V).
])

gramatica.agregar_regla('Det', [
    (['el'], 0.5),        # El determinante (Det) puede ser "el".
    (['la'], 0.5)         # O "la".
])

gramatica.agregar_regla('N', [
    (['gato'], 0.5),      # El sustantivo (N) puede ser "gato".
    (['perro'], 0.5)      # O "perro".
])

gramatica.agregar_regla('V', [
    (['come'], 0.6),      # El verbo (V) puede ser "come".
    (['duerme'], 0.4)     # O "duerme".
])

# Generar oraciones
for _ in range(5):
    oracion = gramatica.generar('S')  # Generar una oración a partir del símbolo inicial 'S'.
    print("Oración generada:", " ".join(oracion))