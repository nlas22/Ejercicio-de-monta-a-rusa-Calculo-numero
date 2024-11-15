import unittest
import numpy as np
from src.trazador_cubico import TrazadorCubico

class TestTrazadorCubico(unittest.TestCase):
    def setUp(self):
        self.trazador = TrazadorCubico('datos/trazador_cubico_datos.csv')

    def test_evaluacion(self):
        x_vals = np.linspace(0, 5, 10)
        y_vals = self.trazador.evaluar(x_vals)
        self.assertEqual(len(y_vals), len(x_vals))

if __name__ == '__main__':
    unittest.main()
