# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:54:44 2022

@author: dafyd
"""
from es_primo_facil import es_primo
from typing import TextIO

def n_primos(n:int, archivo:str):
    f:TextIO = open(archivo, 'w')
    for i in range(2, n + 1):
        if es_primo(i):
            f.write(str(i) + '\n')
    f.close()
    
n_primos(13, 'n_primos.txt')