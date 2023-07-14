import unittest
from auditor_fruteria import AuditorFruteria

class TestAuditor(unittest.TestCase):

    def test_verduleria_la_soledad(self):
        a:AuditorFruteria = AuditorFruteria('precios-maximos.csv', 'verduleria-la-soledad.csv')
        self.assertTrue(a.fruteria_en_regla())
        self.assertEqual(a.cant_precios_excedidos(),0)

    def test_verduleria_sol_y_luna(self):
        a:AuditorFruteria = AuditorFruteria('precios-maximos.csv', 'verduleria-sol-y-luna.csv')
        self.assertFalse(a.fruteria_en_regla())
        self.assertEqual(a.cant_precios_excedidos(),1)

    def test_verduleria_huerta_fertil(self):
        a:AuditorFruteria = AuditorFruteria('precios-maximos.csv', 'verduleria-huerta-fertil.csv')
        self.assertFalse(a.fruteria_en_regla())
        self.assertEqual(a.cant_precios_excedidos(),4)


unittest.main()
