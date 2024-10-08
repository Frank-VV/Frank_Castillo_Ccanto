import unittest

# Función para calcular el MCD de dos números usando el algoritmo de Euclides
def mcd(nro1, nro2):
    while nro2 != 0:
        nro1, nro2 = nro2, nro1 % nro2
    return nro1

# Función para calcular el MCD de cuatro números
def mcd_de_cuatro(nro1, nro2, nro3, nro4):
    return mcd(mcd(mcd(nro1, nro2), nro3), nro4)

# Pruebas unitarias
class TestOperaciones(unittest.TestCase):
    def test_mcd_dos_numeros(self):
        esperado = 5
        actual = mcd(10, 15)
        self.assertEqual(actual, esperado)

    def test_mcd_cuatro_numeros(self):
        esperado = 5
        actual = mcd_de_cuatro(10, 15, 20, 25)
        self.assertEqual(actual, esperado)

if __name__ == '__main__':
    unittest.main()
