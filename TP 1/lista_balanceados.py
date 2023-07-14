# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 15:16:50 2022

@author: dafyd
"""
from binario_balanceado import es_binario_balanceado, decimal_a_binario, string_inverso

from typing import List

def lista_balanceados():
    
    i = 0
    rv = []
    while i < 200:
        if es_binario_balanceado(i):
            rv.append(i)
        i = i + 1
    
    return rv

print(lista_balanceados())
