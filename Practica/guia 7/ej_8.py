# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 01:03:05 2022

@author: dafyd
"""

from typing import List

prueba = [1, 2, 3, 5, 6, 7, 8, 9]

def buscar_menores_v1(x:int, ls:List[int]) -> List[int]:
    res:List[int] = []
    for i in range(len(ls)):
        if ls[i] <= x:
            res.append(ls[i])
    return res

print(buscar_menores_v1(4, prueba))

def buscar_menores_v2(x:int, ls:List[int]) -> List[int]:
    izq:int = 0
    der:int = len(ls)
    res:List[int] = []
    terminar:bool = True
    if ls[len(ls)-1] < x:
        return ls
    while izq < der and terminar:
        med:int = (izq + der) // 2
        if ls[med] == x:
            res = ls[:med+1]
            terminar = False
        elif ls[med] < x:
            izq = med + 1
        else:
            der = med
    res = ls[:med]
    return res

prueba2 = [1, 2, 3, 5, 6, 7, 8, 9]
print(buscar_menores_v2(4, prueba2))




