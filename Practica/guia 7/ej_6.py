# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:07:37 2022

@author: dafyd
"""
from typing import List

prueba:List[int] = [1, 2, 8, 99, 5, 66, 126, 2]
prueba2:List[int] = prueba[:]

def menor_en_lista(ls:List[int]) -> List:
    res:int = 0
    for i in range(len(ls)):
        if ls[i] <= ls[res]:
            res = i
    return res
#print(menor_en_lista(prueba))

def selection_sort_v1(ls:List[int]) -> List:
    for i in range(len(ls)):
        sublista:List[int] = ls[i:]
        pos:int = menor_en_lista(sublista) + i
        (ls[i], ls[pos]) = (ls[pos], ls[i])
    return ls
print(selection_sort_v1(prueba))

def mayor_en_lista(ls:List[int]) -> int:
    res:int = 0
    for i in range(len(ls)):
        if ls[i] >= ls[res]:
            res = i
    return res
#print(mayor_en_lista(prueba))

def selection_sort_v2(ls:List[int]) -> List:
    for i in range(len(ls), 0, -1):
        sublista:List[int] = ls[:i]
        pos:int = mayor_en_lista(sublista)
        (ls[i-1], ls[pos]) = (ls[pos], ls[i-1])
    return ls

print(selection_sort_v2(prueba2))
        