# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:44:15 2022

@author: dafyd
"""
import time
from typing import List

# def saludar(n:int):
#     print('Hola', n)
#     time.sleep(1) #pausa de un segundo
#     saludar(n+1)
# saludar(1)

# def despegar(n:int):
#     if n == 0:
#         print('despegue')
#     elif n > 0:
#         print(n)
#         despegar(n-1)
#despegar(10)

# def factorial(n):
#     res:int = 1
#     i:int = n
#     while i > 0:
#         res = res *i
#         i = i - 1
#     return res
# print(factorial(3))

def factorial_v2(n):
    if n == 0:
        return 1
    else:    
        return n * factorial_v2(n-1)
    
print(factorial_v2(3))

def sumatoria(n):
    if n == 0 :
        return 0
    else:
        return n + sumatoria(n-1)
print(sumatoria(10))

def sumatoria_lista_rec(ls:List[int]):
    if ls == []:
        return 0
    else:
        return ls[0] + sumatoria_lista_rec(ls[1:])
print(sumatoria_lista_rec([1,2,3]))

def max_rec(ls:List[int]):
    if len(ls) == 1:
        return ls[0]
    else:
        if ls[0] < max_rec(ls[1:len(ls)]):
           return max_rec(ls[1:len(ls)])
        else:
           return ls[0]
print(max_rec([1,8,5,9,10,2,22,7]))
        
       
        
       