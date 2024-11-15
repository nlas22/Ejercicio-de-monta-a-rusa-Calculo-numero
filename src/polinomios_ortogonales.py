#POLINOMIOS ORTOGONALES  para optimizar la forma de ciertos tramos de la vía y mejorar la experiencia del usuario.

#Importar las librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial import Chebyshev

class PolinomiosOrtogonales:
    def __init__(self, grado, csv_file=None):
        self.grado = grado
        self.pol_chebyshev = Chebyshev.basis(grado) #aqui creo mi polinomio de chebyshev con su base
        if csv_file:
            datos = pd.read_csv(csv_file)
            self.x_vals = np.array(datos['x_vals'])
        else:
            self.x_vals = np.linspace(-1, 1, 100)  #mi intervalo del polinomio de chevishev

    def evaluar(self, x_vals=None):#esta es mi funcion que evalua el polinomio con los valores de la columna x
        if x_vals is None:
            x_vals = self.x_vals
        return self.pol_chebyshev(x_vals)

    def graficar(self):#aqui ubico mmis criterios para la grafica
        y_vals = self.evaluar()
        plt.plot(self.x_vals, y_vals, label=f"Polinomio Chebyshev grado {self.grado}")
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Polinomio Ortogonal de Chebyshev")
        plt.show()

