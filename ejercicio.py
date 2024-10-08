import unittest

def suma(nro1, nro2):
    return nro1 + nro2

def resta(nro1, nro2):
    return nro1 - nro2

def multiplicacion(nro1, nro2):
    return nro1 * nro2

def division(nro1, nro2):
    return nro1 / nro2
    
class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        esperado = 20
        actual = suma(5, 15)
        self.assertEqual(actual, esperado)

    def test_resta(self):
        esperado = 5
        actual = resta (15, 10)
        self.assertEqual(actual, esperado)

    def test_multiplicacion(self):
        esperado = 20
        actual = multiplicacion (4, 5)
        self.assertEqual(actual, esperado)

    def test_division(self):
        esperado = 5
        actual = division (20, 4)
        self.assertEqual(actual, esperado)

if __name__=='__main__':
    unittest.main()

