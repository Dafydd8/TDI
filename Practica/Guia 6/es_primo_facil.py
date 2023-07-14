# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 01:06:56 2022

@author: dafyd
"""

def es_primo(n:int) -> bool:

    res:bool = True
    divisor:int = n - 1
    
    while divisor > 1 and res:
        if n % divisor == 0:
            res = False
        divisor = divisor - 1
    return res

print(es_primo(8))