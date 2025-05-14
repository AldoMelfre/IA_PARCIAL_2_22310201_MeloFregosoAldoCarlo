# ============================================
# BASE DE CONOCIMIENTO CON INFERENCIA LÓGICA
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

    def agregar_regla(self, regla):
        """
        Agrega una regla lógica a la base de conocimiento.
        :param regla: Regla lógica como una función lambda.
        """
        self.reglas.append(regla)  # Añade la regla a la lista de reglas.

    def inferir(self):
        """
        Realiza inferencias basadas en los hechos y reglas de la base de conocimiento.
        """
        nuevos_hechos = set()  # Conjunto para almacenar los nuevos hechos inferidos.

        for regla in self.reglas:  # Itera sobre cada regla en la base de conocimiento.
            for hecho in self.hechos:  # Itera sobre cada hecho conocido.
                resultado = regla(hecho)  # Aplica la regla al hecho actual.
                if resultado and resultado not in self.hechos:  # Si se infiere un nuevo hecho:
                    nuevos_hechos.add(resultado)  # Añade el nuevo hecho al conjunto.

        self.hechos.update(nuevos_hechos)  # Actualiza la base de conocimiento con los nuevos hechos.
        return nuevos_hechos  # Devuelve los nuevos hechos inferidos.

    def mostrar_hechos(self):
        """
        Muestra todos los hechos conocidos en la base de conocimiento.
        """
        print("Hechos conocidos:")  # Encabezado para los hechos conocidos.
        for hecho in self.hechos:  # Itera sobre cada hecho conocido.
            print(f"- {hecho}")  # Imprime cada hecho.

# ============================================
# EJEMPLO: INFERENCIA LÓGICA PROPOSICIONAL
# ============================================
# Crear una base de conocimiento
kb = BaseDeConocimiento()  # Instancia de la base de conocimiento.

# Agregar hechos iniciales
kb.agregar_hecho("P")  # Hecho: 'P' es verdadero.

# Agregar reglas lógicas
# Regla: Si 'P' es verdadero, entonces 'Q' también es verdadero.
kb.agregar_regla(lambda x: "Q" if x == "P" else None)

# Regla: Si 'Q' es verdadero, entonces 'R' también es verdadero.
kb.agregar_regla(lambda x: "R" if x == "Q" else None)

# Inferir nuevos hechos
nuevos_hechos = kb.inferir()  # Realiza inferencias basadas en los hechos y reglas.
print("Nuevos hechos inferidos:", nuevos_hechos)  # Imprime los nuevos hechos inferidos.

# Mostrar todos los hechos conocidos
kb.mostrar_hechos()  # Muestra todos los hechos en la base de conocimiento.