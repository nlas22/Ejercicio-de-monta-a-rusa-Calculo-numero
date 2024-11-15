from src.trazador_cubico import TrazadorCubico
from src.minimos_cuadrados import MinimosCuadrados
from src.polinomios_ortogonales import PolinomiosOrtogonales
from src.sistema_ecuaciones import SistemaEcuaciones
import numpy as np

def ejecutar_trazador_cubico():
    print("Ejecutando Trazador Cúbico Sujeto...")
    trazador = TrazadorCubico('datos/trazador_cubico_datos.csv')
    x_vals = np.linspace(0, 5, 100)
    trazador.graficar(x_vals)

def ejecutar_minimos_cuadrados():
    print("Ejecutando Polinomio de Mínimos Cuadrados...")
    minimos_cuadrados = MinimosCuadrados('datos/minimos_cuadrados_datos.csv', grado=2)
    x_vals = np.linspace(0, 4, 100)
    minimos_cuadrados.graficar(x_vals)

def ejecutar_polinomios_ortogonales():
    print("Ejecutando Polinomio Ortogonal de Chebyshev...")
    pol_ortogonal = PolinomiosOrtogonales(grado=3, csv_file='datos/polinomios_ortogonales_datos.csv')
    pol_ortogonal.graficar()

def ejecutar_sistema_ecuaciones():
    print("Resolviendo Sistema de Ecuaciones...")
    sistema = SistemaEcuaciones('datos/sistema_ecuaciones_datos.csv')
    solucion = sistema.resolver()
    print("Solución del sistema de ecuaciones:", solucion)

if __name__ == "__main__":
    ejecutar_trazador_cubico()
    ejecutar_minimos_cuadrados()
    ejecutar_polinomios_ortogonales()
    ejecutar_sistema_ecuaciones()
