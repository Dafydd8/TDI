# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 00:24:43 2022

@author: dafyd
"""
#ejercicio 3
#a)
def raiz_cuadrada(n:int) -> int:
    '''
        Requiere: n mayor o igual a 0
        Devuelve: La parte entera de la raiz cuadrada de n
    '''
    import math
    res:int = int(math.sqrt(n))
    return res

#b)
def factorial(n:int) -> int:
    i:int = n
    res:int = 1
    while n >= i and i != 0:
        res = res * i
        i = i - 1
    return res

#e)
def asteriscos(n:int) -> str:
    '''
       Requiere: n es entero mayor o igual a 0
       Devuelve: un string de n asteriscos
    '''
    res:str = n * '*'
    return res

#f)
def cuadrado_asteriscos(n:int) -> str:
    '''
       Requiere: n es un entero mayor o igual a 0
       Devuelve: un cuadrado de asteriscos de lado n
    '''
    res:str = n * (n * '*' + '\n')
    return res

#g)
def string_inverso(t:str) -> str:
    '''
       Requiere: nada
       Devuelve: el string ingresado con las letras re-ordenadas de atras
       hacia adelante.
    '''
    pos:int = len(t) - 1
    res:str = ''
    
    while pos >= 0:
        res = res + t[pos]
        pos = pos - 1
        
    return res

#h)
def contar_a(t:str) -> int:
    '''
       Requiere: nada
       Devuelve: la cantidad de veces que la letra a aparece en t
    '''
    pos:int = len(t) - 1
    res:int = 0
    while pos >= 0:
        if t[pos] == 'a' or t[pos] == 'A':
            res = res + 1
            pos = pos - 1
        else:
            pos = pos - 1
    return res

        
        