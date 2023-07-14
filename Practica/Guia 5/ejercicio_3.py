# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:17:19 2022

@author: dafyd
"""

#Ejercicio 3 

#a)
from typing import List

def maximo_en_lista(x:List[float]) -> float:
    i:int = 0
    res:float = x[i]
    while i < len(x):
        if x[i] >= res:
            res = x[i]
        i = i + 1
    
    return res

pruebaa:List[float] = [1.0, 12.7, 1.0, 8.8, 12.7, 3.0]
#print(maximo_en_lista(pruebaa))

#b)
def concatenacion_strings_en_lista(strs:List[str]) -> str:
    i:int = 0
    res:str = ''
    
    while i < len(strs):
        res = res + strs[i]     
        i = i + 1
        
    return res

pruebab:List[str] = ['ab','c','','def']
#print(concatenacion_strings_en_lista(pruebab))

#c)
def enteros_ordenados(ordenados:List[int]) -> bool:
    i:int = 0
    res:bool = True
    while i < (len(ordenados) - 1) and res:
        if ordenados[i] < ordenados[i + 1]:
            res = True
        else:
            res = False
        i = i + 1
    return res

pruebac:List[int] = [2,6,8]
print(enteros_ordenados(pruebac))

#d)
def n_impares(n:int) -> List[int]:
    res:List[int] = [] #O(1)
    i:int = 0 #O(1)
    posicion:int = 1 #O(1)
    while i < n: #O(n)
        if posicion % 2 == 1: #O(1)
            res.append(posicion) #O(1)            
            i = i + 1#O(1)
        posicion = posicion + 1#O(1)
    return res
#print(n_impares(4))

#e)
def suma_a_todos(n:int, ls:List[int]) -> List[int]:
    i:int = 0 #O(1)
    res:List[int] = ls #O(1)
    while i < len(ls): #O(len(ls))
        res[i] = res[i] + n #O(1)
        i = i + 1 #O(1)
    return res

pruebae:List[int] = [1,9,7,7]
#print(suma_a_todos(10, pruebae))

#f)
def contar_caracteres(lst:List[str]) -> int:
    res:int = 0
    i:int = 0
    while i < len(lst): #O(len(lst))
        res = res + len(lst[i]) #O(1)
        i = i + 1 #O(1)
    return res

pruebaf:List[str] = ['tor','c','ua','to']
#print(contar_caracteres(pruebaf))

#g)
def as_en_lista(lst:List[str]) -> int:
    i:int = 0
    nropalabra:int = 0
    palabra:str = ''
    res:int = 0
    while nropalabra < len(lst):
        i = 0
        palabra = lst[nropalabra]
        while i < len(palabra):
            if palabra[i] == 'a':
                res = res + 1
            i = i + 1
        nropalabra = nropalabra + 1
    return res

pruebag:List[str] = ['abba','acdc','bee gees','a-ha']
#print(as_en_lista(pruebag))        
    
#h)
def separador(txt:str, sep:str) -> List[str]:
    res:List[str] = [] #O(1)
    bloque:str = '' #O(1)
    i:int = 0 #O(1)
    while i < len(txt): #O(len(txt))
        if txt[i] == sep: #O(len(txt[i])*len(sep))
            res.append(bloque) #O(1)
            bloque = '' #O(1)
        else:
            bloque = bloque + txt[i] #O(1)
        i = i + 1
    
    if txt[i - 1] == sep:
        bloque = ''
        res.append(bloque)
    else:
        res.append(bloque)
            
    return res
     
print(separador('papepipopup', 'p'))
       
    
    
    
    
    
    
            
            
            
    
    
    
        
    