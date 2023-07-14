# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 10:28:11 2022

@author: dafyd
"""

def n_equis2(n:int) -> str:
    '''
       requiere: n >= 0
       devuelve: la concatenacion de n veces el string 'x'
    '''
    i:int = 0 
    txt:str = ''
    while i < n:
        txt = txt + 'x'
        i = i + 1
    return txt

print(n_equis2(8))