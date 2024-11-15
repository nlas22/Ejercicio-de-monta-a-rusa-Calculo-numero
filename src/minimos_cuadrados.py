#MINIMOS CUADRADOS análisis de la estabilidad estructural de la vía




#Importar las librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class MinimosCuadrados:
    def __init__(self, csv_file, grado):
        datos = pd.read_csv(csv_file)#desde aqui leo los datos del csv
        self.x_data = np.array(datos['x_data'])
        self.y_data = np.array(datos['y_data'])
        self.grado = grado
        self.coeficientes = np.polyfit(self.x_data, self.y_data, grado) #mi funcion de minimos cuadrados

    def evaluar(self, x_vals):
        return np.polyval(self.coeficientes, x_vals)

    def graficar(self, x_vals):  #los criterios para la grafica
        y_vals = self.evaluar(x_vals)
        plt.plot(self.x_data, self.y_data, 'o', label="Datos")
        plt.plot(x_vals, y_vals, '-', label="Polinomio de Mínimos Cuadrados")
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Ajuste de Mínimos Cuadrados")
        plt.show()
