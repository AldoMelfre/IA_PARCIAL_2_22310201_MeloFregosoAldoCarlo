from itertools import product  # Importa product para generar combinaciones de valores de verdad.

# ============================================
# FUNCIONES PARA EQUIVALENCIA, VALIDEZ Y SATISFACIBILIDAD
# ============================================
def generar_tabla(proposiciones, formula):
    """
    Genera una tabla de verdad para una fórmula lógica.
    :param proposiciones: Lista de proposiciones (por ejemplo, ['P', 'Q']).
    :param formula: Fórmula lógica como una función lambda.
    :return: Lista de resultados de la fórmula para cada combinación de valores de verdad.
    """
    combinaciones = list(product([True, False], repeat=len(proposiciones)))  # Todas las combinaciones posibles.
    resultados = []  # Lista para almacenar los resultados de la fórmula.

    for combinacion in combinaciones:
        valores = dict(zip(proposiciones, combinacion))  # Asocia cada proposición con su valor de verdad.
        resultado = formula(**valores)  # Evalúa la fórmula lógica con los valores actuales.
        resultados.append(resultado)  # Almacena el resultado.
    
    return resultados  # Devuelve los resultados de la fórmula.

def es_equivalente(proposiciones, formula1, formula2):
    """
    Verifica si dos fórmulas son equivalentes lógicamente.
    :param proposiciones: Lista de proposiciones.
    :param formula1: Primera fórmula lógica como función lambda.
    :param formula2: Segunda fórmula lógica como función lambda.
    :return: True si son equivalentes, False en caso contrario.
    """
    resultados1 = generar_tabla(proposiciones, formula1)  # Resultados de la primera fórmula.
    resultados2 = generar_tabla(proposiciones, formula2)  # Resultados de la segunda fórmula.
    return resultados1 == resultados2  # Verifica si las tablas de verdad son idénticas.

def es_valida(proposiciones, formula):
    """
    Verifica si una fórmula es válida (tautología).
    :param proposiciones: Lista de proposiciones.
    :param formula: Fórmula lógica como función lambda.
    :return: True si es válida, False en caso contrario.
    """
    resultados = generar_tabla(proposiciones, formula)  # Resultados de la fórmula.
    return all(resultados)  # Es válida si todos los resultados son True.

def es_satisfacible(proposiciones, formula):
    """
    Verifica si una fórmula es satisfacible.
    :param proposiciones: Lista de proposiciones.
    :param formula: Fórmula lógica como función lambda.
    :return: True si es satisfacible, False en caso contrario.
    """
    resultados = generar_tabla(proposiciones, formula)  # Resultados de la fórmula.
    return any(resultados)  # Es satisfacible si al menos un resultado es True.

# ============================================
# EJEMPLO: EQUIVALENCIA, VALIDEZ Y SATISFACIBILIDAD
# ============================================
# Lista de proposiciones
proposiciones = ['P', 'Q']

# Fórmulas lógicas
formula1 = lambda P, Q: P or Q  # Fórmula 1: P ∨ Q
formula2 = lambda P, Q: Q or P  # Fórmula 2: Q ∨ P (equivalente a fórmula 1)
formula3 = lambda P, Q: P and not P  # Fórmula 3: P ∧ ¬P (contradicción)

# Verificar equivalencia
print("¿Formula1 es equivalente a Formula2?", es_equivalente(proposiciones, formula1, formula2))  # True

# Verificar validez
print("¿Formula1 es válida?", es_valida(proposiciones, formula1))  # False
print("¿Formula3 es válida?", es_valida(proposiciones, formula3))  # False

# Verificar satisfacibilidad
print("¿Formula1 es satisfacible?", es_satisfacible(proposiciones, formula1))  # True
print("¿Formula3 es satisfacible?", es_satisfacible(proposiciones, formula3))  # False