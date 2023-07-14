import unittest

from binario_balanceado import decimal_a_binario, es_binario_balanceado, \
                      cantidad_binarios_balanceados_entre, siguiente_binario_balanceado, \
                      anterior_binario_balanceado, binario_balanceado_mas_cercano, string_inverso

class test_string_inverso(unittest.TestCase): #función auxiliar
    
    def test_general(self):
        self.assertEqual(string_inverso(''), '')
        self.assertEqual(string_inverso('hola'), 'aloh')
        self.assertEqual(string_inverso('h2! Ñ;'), ';Ñ !2h')
        self.assertEqual(string_inverso('1000'), '0001')
        
class test_decimal_a_binario(unittest.TestCase):
        
    def test_no_balanceados(self):
        self.assertEqual(decimal_a_binario(1), '1')
        self.assertEqual(decimal_a_binario(8), '1000')
        self.assertEqual(decimal_a_binario(13), '1101')
        
    def test_balanceados(self):
        self.assertEqual(decimal_a_binario(2), '10')
        self.assertEqual(decimal_a_binario(9), '1001')
        self.assertEqual(decimal_a_binario(35), '100011')
        
class test_es_binario_balanceado(unittest.TestCase):
    
    def test_true(self):
        self.assertTrue(es_binario_balanceado(2))
        self.assertTrue(es_binario_balanceado(9))
        self.assertTrue(es_binario_balanceado(50))
        
    def test_false(self):
        self.assertFalse(es_binario_balanceado(1))
        self.assertFalse(es_binario_balanceado(5))
        self.assertFalse(es_binario_balanceado(84))
        
class test_cantidad_binarios_balanceados_entre(unittest.TestCase):
    
    def test_n_igual_m(self):
        self.assertEqual(cantidad_binarios_balanceados_entre(9, 9), 1)
        self.assertEqual(cantidad_binarios_balanceados_entre(11, 11), 0)
        
    def test_existen_intermedios(self):
        self.assertEqual(cantidad_binarios_balanceados_entre(2, 10), 3)
        self.assertEqual(cantidad_binarios_balanceados_entre(1, 3), 1)
        self.assertEqual(cantidad_binarios_balanceados_entre(2, 8), 1)
        self.assertEqual(cantidad_binarios_balanceados_entre(41, 60), 7)
        
    def test_no_existen_intermedios(self):
        self.assertEqual(cantidad_binarios_balanceados_entre(3, 8), 0)
        self.assertEqual(cantidad_binarios_balanceados_entre(15, 30), 0) 
        
class test_siguiente_binario_balanceado(unittest.TestCase):
    
    def test_general(self):
        self.assertEqual(siguiente_binario_balanceado(1), 2)
        self.assertEqual(siguiente_binario_balanceado(2), 9)
        self.assertEqual(siguiente_binario_balanceado(3), 9)
        self.assertEqual(siguiente_binario_balanceado(27), 35)
    
class test_anterior_binario_balanceado(unittest.TestCase):
    
    def test_n_igual_a_3(self):
        self.assertEqual(anterior_binario_balanceado(3), 2)
    
    def test_n_mayor_a_3(self):
        self.assertEqual(anterior_binario_balanceado(5), 2)
        self.assertEqual(anterior_binario_balanceado(10), 9)
        
class test_binario_balanceado_mas_cercano(unittest.TestCase):
    
    def test_n_igual_a_1(self):
        self.assertEqual(binario_balanceado_mas_cercano(1), 2)
    
    def test_balanceados(self):
        self.assertEqual(binario_balanceado_mas_cercano(2), 2)
        self.assertEqual(binario_balanceado_mas_cercano(50), 50)
    
    def test_no_balanceados(self):
        self.assertEqual(binario_balanceado_mas_cercano(3), 2)
        self.assertEqual(binario_balanceado_mas_cercano(20), 12)
        self.assertEqual(binario_balanceado_mas_cercano(28), 35)
        self.assertEqual(binario_balanceado_mas_cercano(51), 52)

unittest.main()
