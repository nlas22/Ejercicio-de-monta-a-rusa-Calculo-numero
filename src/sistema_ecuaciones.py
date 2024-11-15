#SISTEMA DE ECUACIONES para determinar las fuerzas que actúan en los puntos críticos de la estructura.
import numpy as np
import pandas as pd

class SistemaEcuaciones:
    def __init__(self, csv_file):
        datos = pd.read_csv(csv_file, header=None)
        self.A = datos.iloc[:, :-1].values  # Aqui quiero tomar todos los elementos menos la última columna
        self.b = datos.iloc[:, -1].values   # Esta es mi ultima columna

    def resolver(self):
        return np.linalg.solve(self.A, self.b) #Lo que regresa mi funcionresolviendo el sistema de ecuaciones
