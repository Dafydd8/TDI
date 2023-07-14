# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 17:51:42 2022

@author: dafyd
"""
from typing import List

#b)
def listar_mesetas(lst:List[int]) -> List[List[int]]:
    i:int = 0
    posres:int = 0
    res:List[List[int]] = []
    
    res.append([lst[i]])
    while i < len(lst) - 1:
        if lst[i] == lst[i + 1]:
            res[posres].append(lst[i + 1])
        else:
            res.append([lst[i + 1]])
            posres = posres + 1
        i = i + 1
    return res

#a)
def larger_meseta(lst:List[int]) -> int:
    i:int = 0
    res:int = 0
    
    listada:List[List[int]] = listar_mesetas(lst)
    while i < len(listada) - 1:
        if len(listada[i]) > res:
            res = listada[i][0]
        
        i = i + 1
    return res

#c)
def cantidades(lst:List[int]) -> List[int]:
    listada:List[List[int]] = listar_mesetas(lst)
    i:int = 0
    res:List[int] = []
    while i < len(listada):
        res.append(len(listada[i]))
        i = i + 1
    return res

    
prueba:List[int] = [1,1,2,6,6,6,3,3]
print(listar_mesetas(prueba))
print(larger_meseta(prueba))
print(cantidades(prueba))

