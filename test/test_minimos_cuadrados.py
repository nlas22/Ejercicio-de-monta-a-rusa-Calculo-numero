import sys
import os
import unittest
import numpy as np


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


from minimos_cuadrados import MinimosCuadrados


class TestMinimosCuadrados(unittest.TestCase):
    def setUp(self):
       
        self.pol_minimos = MinimosCuadrados('datos/minimos_cuadrados_datos.csv', grado=2)

    def test_evaluacion(self):
        x_vals = np.linspace(0, 4, 10)
        y_vals = self.pol_minimos.evaluar(x_vals)
        self.assertEqual(len(y_vals), len(x_vals))
        
    def test_coefs(self):
        self.assertEqual(len(self.pol_minimos.coeficientes), 3)

if __name__ == '__main__':
    unittest.main()
