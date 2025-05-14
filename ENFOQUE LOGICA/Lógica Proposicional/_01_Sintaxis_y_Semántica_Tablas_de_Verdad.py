from itertools import product  # Importa product para generar combinaciones de valores de verdad.

# ============================================
# GENERACIÓN DE TABLAS DE VERDAD
# ============================================
def tabla_de_verdad(proposiciones, formula):
    """
    Genera una tabla de verdad para una fórmula lógica.
    :param proposiciones: Lista de proposiciones (por ejemplo, ['P', 'Q']).
    :param formula: Fórmula lógica como una función lambda.
    :return: Imprime la tabla de verdad.
    """
    # Generar todas las combinaciones posibles de valores de verdad (True, False) para las proposiciones.
    combinaciones = list(product([True, False], repeat=len(proposiciones)))

    # Imprimir encabezado de la tabla.
    print(" | ".join(proposiciones) + " | Resultado")
    print("-" * (len(proposiciones) * 4 + 12))  # Línea separadora.

    # Evaluar la fórmula para cada combinación de valores de verdad.
    for combinacion in combinaciones:
        valores = dict(zip(proposiciones, combinacion))  # Asocia cada proposición con su valor de verdad.
        resultado = formula(**valores)  # Evalúa la fórmula lógica con los valores actuales.
        # Imprimir la combinación de valores y el resultado.
        print(" | ".join(str(valores[prop]) for prop in proposiciones) + f" | {resultado}")

# ============================================
# EJEMPLO: TABLA DE VERDAD PARA UNA FÓRMULA
# ============================================
# Lista de proposiciones
proposiciones = ['P', 'Q']

# Fórmula lógica: (P ∧ Q) → ¬P
# Se define como una función lambda que toma los valores de las proposiciones.
formula = lambda P, Q: (P and Q) <= (not P)

# Generar la tabla de verdad para la fórmula.
tabla_de_verdad(proposiciones, formula)