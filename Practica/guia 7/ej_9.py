# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:28:39 2022

@author: dafyd
"""
from typing import List
import math

def menor_en_lista(ls:List[int]) -> List: #funcion aux
    res:int = 0
    for i in range(len(ls)):
        if ls[i] <= ls[res]:
            res = i
    return res

def selection_sort_v1(ls:List[int]) -> List: #funcion aux
    for i in range(len(ls)):
        sublista:List[int] = ls[i:]
        pos:int = menor_en_lista(sublista) + i
        (ls[i], ls[pos]) = (ls[pos], ls[i])
    return ls
#print(selection_sort_v1(prueba))

def buscar(x:int, ls:List[int]) -> bool: #funcion aux
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

#a)
def media_lista(ls:List[int]) -> int:
    suma:int = 0
    for i in ls:
        suma = suma + i
    return suma / len(ls)
#print(media_lista([1,2,3,4]))

#b)
def mediana_lista(ls:List[int]) -> int:
    a = selection_sort_v1(ls)
    return a[len(a) // 2]
#print(mediana_lista([1,3,6,1,5,8,4]))        

#c)
def es_primo_god(n:int) -> bool:
    i = math.sqrt(n)
    divisor = i // 1
    res:bool = True
    if n == 1 or n == 0:
        return False
    while divisor > 1 and res:
        if n % divisor == 0:
            res = False
        divisor = divisor - 1
    return res
#print(es_primo_god(0))

#d)
def binario_decimal(A:List[int]) -> int:
    res:int = 0 #O(1)
    B:List[int] = A[::-1] #O(len(A))
    for i in range(0, len(B)): #O(len(A))
        if B[i] == 0:
            res = res + 0
        else:
            res = res + 2 ** i
    return res
#print(binario_decimal([1, 0, 1, 0]))

#e)
def positivo_o_negativo(ls:List[int]) -> bool:
    '''
        Requiere: los elementos de ls estan ordenados de menor a mayor.
        Devuelve:
    '''
    return ls[0] > 0
prueba = [-2, 5, 6, 8]
#print(positivo_o_negativo(prueba)

#f)
def buscar_en_listas_listadas(x:int, ls:List[List[int]]) -> int:
    res:int = 0
    for i in range(len(ls)):
        if buscar(x, ls[i]):
            res = res + 1
    return res
#print(buscar_en_listas_listadas(1, [[1, 2, 3], [2, 2, 2], [1, 1, 1], [3, 1]]))
            
