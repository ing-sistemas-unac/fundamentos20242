import unittest

def sumar(a, b):
    return a + b
# Clase para definir los casos de prueba de la función
class TestFuncionSumar(unittest.TestCase):
    # caso 1
    def test_sumar_numeros_positivos(self):
        self.assertEqual(sumar(3,4), 7) # assertEqual(llamar a la función, resultado esperado)
    # caso 2
    def test_sumar_numeros_negativos(self):
        self.assertEqual(sumar(-1, -2), -3) 
    # caso 3
    def test_sumar_numero_cero(self):
        self.assertEqual(sumar(1, 0), 1) 

if __name__ == "__main__":
    unittest.main()
