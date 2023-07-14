# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:35:50 2022

@author: dafyd
"""
a = []
for i in range(33):
    a.append(i)

from typing import List
def buscar(x:int, ls:List[int]) -> bool:
    izq:int = 0
    der:int = len(ls)
    while izq < der:
        med:int = (izq + der) // 2
        if ls[med] == x:
            return True
        elif ls[med] < x:
            izq = med + 1
        else:
            der = med
    return False
prueba = [1, 2, 3, 4, 5, 6, 7, 8]
print(buscar(3, prueba))
        