# ============================================
# ENCANDENAMIENTO HACIA ADELANTE Y HACIA ATRÁS
# ============================================

class BaseDeConocimiento:
    def __init__(self):
        """
        Inicializa una base de conocimiento vacía.
        """
        self.hechos = set()  # Conjunto para almacenar los hechos conocidos.
        self.reglas = []  # Lista para almacenar las reglas lógicas.

    def agregar_hecho(self, hecho):
        """
        Agrega un hecho a la base de conocimiento.
        :param hecho: Hecho a agregar (por ejemplo, 'P').
        """
        self.hechos.add(hecho)  # Añade el hecho al conjunto de hechos.

    def agregar_regla(self, condicion, conclusion):
        """
        Agrega una regla lógica a la base de conocimiento.
        :param condicion: Condición de la regla (lista de hechos necesarios).
        :param conclusion: Conclusión de la regla (hecho deducido).
        """
        self.reglas.append((condicion, conclusion))  # Añade la regla como una tupla.

    def encadenamiento_hacia_adelante(self, objetivo):
        """
        Realiza encadenamiento hacia adelante para alcanzar un objetivo.
        :param objetivo: Hecho objetivo que se desea deducir.
        :return: True si el objetivo se deduce, False en caso contrario.
        """
        while True:
            nuevos_hechos = set()  # Conjunto para almacenar nuevos hechos deducidos.

            for condicion, conclusion in self.reglas:  # Itera sobre las reglas.
                if all(hecho in self.hechos for hecho in condicion):  # Si la condición se cumple:
                    if conclusion not in self.hechos:  # Si la conclusión no está en los hechos conocidos:
                        nuevos_hechos.add(conclusion)  # Añadir la conclusión como nuevo hecho.

            if objetivo in nuevos_hechos:  # Si el objetivo se deduce:
                return True  # El objetivo se alcanzó.

            if not nuevos_hechos:  # Si no se deducen nuevos hechos:
                return False  # No se puede alcanzar el objetivo.

            self.hechos.update(nuevos_hechos)  # Actualizar los hechos conocidos.

    def encadenamiento_hacia_atras(self, objetivo):
        """
        Realiza encadenamiento hacia atrás para verificar un objetivo.
        :param objetivo: Hecho objetivo que se desea verificar.
        :return: True si el objetivo se verifica, False en caso contrario.
        """
        if objetivo in self.hechos:  # Si el objetivo ya es un hecho conocido:
            return True  # El objetivo se verifica.

        for condicion, conclusion in self.reglas:  # Itera sobre las reglas.
            if conclusion == objetivo:  # Si la conclusión de la regla es el objetivo:
                if all(self.encadenamiento_hacia_atras(hecho) for hecho in condicion):  # Verificar las condiciones.
                    return True  # El objetivo se verifica.

        return False  # No se puede verificar el objetivo.

# ============================================
# EJEMPLO: ENCANDENAMIENTO HACIA ADELANTE Y HACIA ATRÁS
# ============================================
# Crear una base de conocimiento
kb = BaseDeConocimiento()

# Agregar hechos iniciales
kb.agregar_hecho("P")  # Hecho: 'P' es verdadero.

# Agregar reglas lógicas
kb.agregar_regla(["P"], "Q")  # Regla: Si 'P', entonces 'Q'.
kb.agregar_regla(["Q"], "R")  # Regla: Si 'Q', entonces 'R'.

# Encadenamiento hacia adelante
objetivo = "R"
print("Encadenamiento hacia adelante:")
if kb.encadenamiento_hacia_adelante(objetivo):
    print(f"El objetivo '{objetivo}' se alcanzó.")
else:
    print(f"El objetivo '{objetivo}' no se pudo alcanzar.")

# Encadenamiento hacia atrás
print("\nEncadenamiento hacia atrás:")
if kb.encadenamiento_hacia_atras(objetivo):
    print(f"El objetivo '{objetivo}' se verificó.")
else:
    print(f"El objetivo '{objetivo}' no se pudo verificar.")