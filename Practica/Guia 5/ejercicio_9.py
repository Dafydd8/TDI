# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:52:14 2022

@author: dafyd
"""

#a)
from typing import List

def maximo_en_lista(x:List[float]) -> float:
    i:int = 0
    res:float = x[i]
    for i in range(len(x)):
        if x[i] >= res:
            res = x[i]
    return res

pruebaa:List[float] = [1.0, 12.7, 1.0, 8.8, 12.7, 3.0]
#print(maximo_en_lista(pruebaa))

#b)
def concatenacion_strings_en_lista(strs:List[str]) -> str:
    res:str = ''
    for i in range(len(strs)):
        res = res + strs[i]       
    return res

pruebab:List[str] = ['ab','c','','def']
#print(concatenacion_strings_en_lista(pruebab))

#g)
def as_en_lista(lst:List[str]) -> int:
    palabra:str = ''
    res:int = 0
    for m in range(len(lst)):
        palabra = lst[m]
        for j in range(len(palabra)):
            if palabra[j] == 'a':
                res = res + 1
    return res

pruebag:List[str] = ['abba','acdc','bee gees','a-ha']
#print(as_en_lista(pruebag))

#h)
def separador(txt:str, sep:str) -> List[str]:
    res:List[str] = []
    bloque:str = ''
    i:int = 0
    for i in range(len(txt)):
        if txt[i] == sep:
            res.append(bloque)
            bloque = ''
        else:
            bloque = bloque + txt[i]
    
    if txt[i] == sep:
        bloque = ''
        res.append(bloque)
    else:
        res.append(bloque)
            
    return res
     
print(separador('papepipopup', 'p'))