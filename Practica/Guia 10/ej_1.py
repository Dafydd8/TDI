# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 23:32:36 2022

@author: dafyd
"""

#a)
def pot2(n) -> int:
    if n == 0:
        return 1
    else:
        return 2 * pot2(n-1)
print(pot2(3))

#b)
def pot_a(a, n):
    if n == 0 and a == 0:
        return 1
    if n == 0:
        return 1
    else:
        return a * pot_a(a, n-1)
print(pot_a(2, 3))

#c)
def producto(n, m):
    if n == 1:
        return m
    else:
        return n * m / (m* (n-1))  * producto(n-1, m)
print(producto(4, 3))

#d)
def es_par(n):
    if n == 1:
        return False
    elif n == 0:
        return True
    else:
        return es_par(n-2)
print(es_par(53))



