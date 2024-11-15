import unittest
import numpy as np
from src.sistema_ecuaciones import SistemaEcuaciones

class TestSistemaEcuaciones(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaEcuaciones('datos/sistema_ecuaciones_datos.csv')

    def test_resolver(self):
        solucion = self.sistema.resolver()
        self.assertEqual(len(solucion), self.sistema.A.shape[1])

    def test_resultado(self):
        solucion = self.sistema.resolver()
        resultado = np.dot(self.sistema.A, solucion)
        np.testing.assert_array_almost_equal(resultado, self.sistema.b, decimal=5)

if __name__ == '__main__':
    unittest.main()
