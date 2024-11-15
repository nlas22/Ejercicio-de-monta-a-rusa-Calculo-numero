import unittest
import numpy as np
from src.polinomios_ortogonales import PolinomiosOrtogonales

class TestPolinomiosOrtogonales(unittest.TestCase):
    def setUp(self):
        self.pol_ortogonal = PolinomiosOrtogonales(grado=3)

    def test_evaluacion(self):
        x_vals = np.linspace(-1, 1, 10)
        y_vals = self.pol_ortogonal.evaluar(x_vals)
        self.assertEqual(len(y_vals), len(x_vals))

    def test_valores(self):
        y_central = self.pol_ortogonal.evaluar(np.array([0]))
        self.assertAlmostEqual(y_central[0], 0, places=5)

if __name__ == '__main__':
    unittest.main()
