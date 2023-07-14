# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:01:26 2022

@author: dafyd
"""

def cuantas_veces(t1:str , t2:str) -> int:
    lon:int = len(t2)
    i1 = 0
    i2 = 0
    ver = True
    completo = 0
    res = 0
    while i2 < lon:
        i1 = 0
        ver = True
        while ver:
            if t1[i1] == t2[i2]:
                ver =True
                completo = completo + 1
                i1 = i1 + 1
                i2 = i2 + 1
            else:
                ver = False
                i2 = i2 + 1
            if completo == len(t1):
                res = res + 1
                ver = False
        #i2 = i2 + 1
    return res

print(cuantas_veces('h', 'hhh'))