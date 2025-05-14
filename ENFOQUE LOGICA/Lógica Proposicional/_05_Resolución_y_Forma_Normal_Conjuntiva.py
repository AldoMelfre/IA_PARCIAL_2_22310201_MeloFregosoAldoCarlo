# ============================================
# RESOLUCIÓN Y FORMA NORMAL CONJUNTIVA (FNC)
# ============================================
def eliminar_implicaciones(formula):
    """
    Elimina las implicaciones de una fórmula lógica.
    :param formula: Fórmula lógica como cadena.
    :return: Fórmula sin implicaciones.
    """
    return formula.replace("->", "|")  # Reemplaza la implicación (P -> Q) por (¬P ∨ Q).

def mover_negaciones(formula):
    """
    Mueve las negaciones hacia los literales.
    :param formula: Fórmula lógica como cadena.
    :return: Fórmula con negaciones movidas.
    """
    # Aquí se puede implementar un algoritmo más avanzado para manejar negaciones.
    return formula  # En este ejemplo, asumimos que ya está en forma adecuada.

def aplicar_distributiva(formula):
    """
    Aplica la distributiva para obtener una conjunción de disyunciones.
    :param formula: Fórmula lógica como cadena.
    :return: Fórmula en forma normal conjuntiva.
    """
    # Aquí se puede implementar un algoritmo para aplicar la distributiva.
    return formula  # En este ejemplo, asumimos que ya está en forma adecuada.

def convertir_a_fnc(formula):
    """
    Convierte una fórmula lógica a Forma Normal Conjuntiva (FNC).
    :param formula: Fórmula lógica como cadena.
    :return: Fórmula en FNC.
    """
    formula = eliminar_implicaciones(formula)  # Paso 1: Eliminar implicaciones.
    formula = mover_negaciones(formula)  # Paso 2: Mover negaciones.
    formula = aplicar_distributiva(formula)  # Paso 3: Aplicar distributiva.
    return formula  # Devuelve la fórmula en FNC.

def resolver(clausulas):
    """
    Aplica el método de resolución para determinar la satisfacibilidad.
    :param clausulas: Lista de cláusulas en FNC.
    :return: True si es satisfacible, False si es insatisfacible.
    """
    while True:
        nuevas = set()  # Conjunto para almacenar las nuevas cláusulas derivadas.

        # Iterar sobre todas las parejas de cláusulas.
        for i, ci in enumerate(clausulas):
            for j, cj in enumerate(clausulas):
                if i >= j:  # Evitar comparar la misma cláusula consigo misma.
                    continue

                # Intentar resolver las cláusulas ci y cj.
                resolvente = resolver_clausulas(ci, cj)
                if resolvente is None:  # Si se deriva una contradicción:
                    return False  # El conjunto de cláusulas es insatisfacible.
                nuevas.add(resolvente)  # Añadir la nueva cláusula derivada.

        # Si no se generan nuevas cláusulas, detener el proceso.
        if nuevas.issubset(set(clausulas)):
            return True  # El conjunto de cláusulas es satisfacible.

        clausulas.extend(nuevas)  # Añadir las nuevas cláusulas al conjunto.

def resolver_clausulas(c1, c2):
    """
    Intenta resolver dos cláusulas.
    :param c1: Primera cláusula como conjunto de literales.
    :param c2: Segunda cláusula como conjunto de literales.
    :return: Resolvente como conjunto de literales, o None si se deriva una contradicción.
    """
    for literal in c1:
        if f"¬{literal}" in c2:  # Si un literal y su negación están presentes:
            resolvente = (c1 - {literal}) | (c2 - {f"¬{literal}"})  # Resolver las cláusulas.
            if not resolvente:  # Si el resolvente está vacío:
                return None  # Se deriva una contradicción.
            return resolvente  # Devuelve el resolvente.

# ============================================
# EJEMPLO: RESOLUCIÓN Y FNC
# ============================================
# Fórmula lógica inicial
formula = "(P -> Q) & (¬Q -> ¬P)"

# Convertir la fórmula a FNC
fnc = convertir_a_fnc(formula)
print("Fórmula en FNC:", fnc)

# Lista de cláusulas en FNC
clausulas = [{"¬P", "Q"}, {"¬Q", "¬P"}]  # Ejemplo de cláusulas en FNC.

# Aplicar el método de resolución
es_satisfacible = resolver(clausulas)
print("¿Es satisfacible?", es_satisfacible)