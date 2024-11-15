#METODO DE TRAZADOR CUBICO: indica si la trayectoria de la via es suave y continua en todo el recorrido



import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

class TrazadorCubico:
    def __init__(self, csv_file):
        # Cargar datos desde el archivo CSV
        datos = pd.read_csv(csv_file)
        self.x_data = np.array(datos['x_data'])
        self.y_data = np.array(datos['y_data'])
        self.spline = CubicSpline(self.x_data, self.y_data, bc_type='clamped')

    def evaluar(self, x_vals):
        return self.spline(x_vals)

    def graficar(self, x_vals):
        y_vals = self.evaluar(x_vals)
        plt.plot(self.x_data, self.y_data, 'o', label="Datos")
        plt.plot(x_vals, y_vals, '-', label="Trazador Cúbico")
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Trazador Cúbico Sujeto")
        plt.show()
