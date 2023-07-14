# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 19:29:26 2022

@author: dafyd
"""

def potenciade2(n):
    if n == 0:
        return 1
    else:
        return 2 * potenciade2(n-1)
print(potenciade2(4))

def potenciadea(n, a):
    if n == 0:
        return 1
    else:
        return a * potenciadea(n-1,a)

print(potenciadea(3, 2))

def producto(n,m):
    if n == 0:
        return 0
    if n == 1 :
        return m
    else:
        return m + producto(n-1, m)
    
print(producto(5, 8))

def espar(n):
    if n == 2:
        return True
    elif n==-1:
        return False
    else:
        return espar(n-2)
print(espar(48))

def productoria(xs):
    if len(xs) == 1:
        return xs[0]
    else:
        return xs[0] * productoria(xs[1:])
print(productoria([9,8,3]))

def cantidadocurrencias(xs, x):
    if len(xs) == 0:
        return 0
    elif len(xs) == 1:
        if xs[0] == x:
            return 1
        else:
            return 0
    else:
        if xs[0] == x:
            return 1 + cantidadocurrencias(xs[1:], x)
        else:
            return cantidadocurrencias(xs[1:], x)
        
print(cantidadocurrencias([1,2,3,1,2,2,3], 2))

def maxpos(xs):
    if len(xs) == 1:
        return len(xs)-1
    else:
        if xs[len(xs)-1] > xs[:len(xs)-1][maxpos(xs[:len(xs)-1])]:
            return len(xs)-1
        else:
            return maxpos(xs[:len(xs)-1])
print(maxpos([1,2,3,1,2,4,1]))

def coincidencias(xs):
    if len(xs) == 0:
        return 0
    elif len(xs) == 1:
        if xs[0] == 0:
            return 1
        else:
            return 0
    else:
        if xs[len(xs)-1] == len(xs)-1:
            return 1 + coincidencias(xs[:len(xs)-1])
        else:
            return coincidencias(xs[:len(xs)-1])
print(coincidencias([0,1,2,6,4,1]))

def sumarpospares(xs):
    if len(xs) == 1:
        return xs[0]
    else:
        if len(xs) % 2 == 0:
            return sumarpospares(xs[:len(xs)-1])
        else:
            return xs[len(xs)-1] + sumarpospares(xs[:len(xs)-1])
print(sumarpospares([1,2,3,2,5]))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))
    
    
    