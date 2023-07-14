# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 16:48:13 2022

@author: dafyd
"""
from typing import Dict
from typing import List
from typing import Set

def maximo_en_lista(x:List[float]) -> float:
    i:int = 0
    res:float = x[i]
    while i < len(x):
        if x[i] >= res:
            res = x[i]
        i = i + 1
    return res

def maximo_en_diccionario(d:Dict[str, int]) -> Set[str]:
    res:Set = set()

    llaves:List[str] = list(d)
    valores:List[int] = []

    for i in llaves:
        valores.append(d[i])
    
    maximo:int = maximo_en_lista(valores)
    
    for i in llaves:
        if d[i] == maximo:
            res.add(i)
    return res


prueba:Dict[str, int] = {'a':10, 'b':14, 'c':9, 'd':14, 'e':7}
print(maximo_en_diccionario(prueba))
        
        
    