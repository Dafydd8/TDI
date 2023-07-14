# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 10:11:33 2022

@author: dafyd
"""

def n_equis(n:int) -> str:
    '''
       requiere: n >= 0
       devuelve: la concatenacion de n veces el string 'x'
    '''
    txt:str = ''
    txt = 'x' * n

    txt2:str = ''
    while n > 0:
        txt2 = txt2 + 'x'
        n -= 1
     
    return txt2

print(n_equis(8))


