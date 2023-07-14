# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:53:47 2022

@author: dafyd
"""
from typing import List

lista_abc = ['alta', 'altura', 'bandida', 'coqueta', 'dinamita', 'expensiva']
padron: List[List[str]] = [['Smith Alice', 'Smith Bob'],
                           ['Smith Carl', 'Smith Lee'],
                           ['Smith Alice', 'Smith Carl']]

import unittest
from P13_funciones import esta_en , padrones_donde_vota


class  test_esta_en(unittest.TestCase):
    def trues(self):
        self.assertTrue(esta_en('coqueta', lista_abc))
    def falses(self):
        self.assertFalse(esta_en('guapa', lista_abc))
        self.assertFalse(esta_en('racineta', lista_abc))
        
class test_padrones(unittest.TestCase):
    def trues(self):
        self.assertEqual(padrones_donde_vota(padron, 'Smith Alice'), [0, 2])
        self.assertEqual(padrones_donde_vota(padron, 'Smith Lee'), [1])
    

unittest.main()