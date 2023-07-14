# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 23:56:06 2022

@author: dafyd
"""
from typing import List

#a)
def productoria(xs:List[int]):
    if len(xs) == 1:
        return xs[0]
    else:
        return xs[0] * productoria(xs[1:])
print(productoria([1,2,3,5,6]))

#b)
def cant_ocurrencias(x, xs):
    if len(xs) == 1:
        if xs[0] == x:    
            return 1
        else:
            return 0
    else:
        if xs[0] == x:
            return 1 + cant_ocurrencias(x, xs[1:])
        else:
             return cant_ocurrencias(x, xs[1:])
print(cant_ocurrencias(3, [1,2,3,1,2,1,1]))

#c)
def max_pos(xs):
    if len(xs) == 1:
        return 0
    else:
        if xs[0] > xs[1:][max_pos(xs[1:])]:
            return 0
        else:
            return max_pos(xs[1:]) + 1
print(max_pos([1,4,2,3,55,3,6,78,59,12]))

#d)
def conta_coincidencias(xs):
    if len(xs) == 1:
        if xs[0] == 0:
            return 1
        else:
            return 0
    else:
        if xs[len(xs)-1] == len(xs)-1:
            return 1 + conta_coincidencias(xs[:len(xs)-1])
        else:
            return conta_coincidencias(xs[:len(xs)-1])
print(conta_coincidencias([0,1,3,3,8,5]))

#e)
def sumar_posiciones_pares(xs):
    if len(xs) == 1:
        return xs[0]
    else:
        if len(xs) % 2 == 0:
            return sumar_posiciones_pares(xs[:len(xs)-1])
        else:
            return xs[len(xs)-1] + sumar_posiciones_pares(xs[:len(xs)-1])
print(sumar_posiciones_pares([1,2,9,2,4]))
    
    
    
    