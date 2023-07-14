# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:08:01 2022

@author: dafyd
"""

def escribir_hasta_primer_numeral(s:str) -> str:
    res:str = ''
    i:int = 0
    ver:bool = True
    while i < len(s) and ver:
        if s[i] != '#':
            res = res + s[i]
        else:
            ver = False
        i = i + 1
    return res
#print(escribir_hasta_primer_numeral('hajsajdh#kkadh'))

from typing import TextIO

def limpiador_de_comentarios(leido:str, escrito:str):
    t:TextIO = open(leido)
    f:TextIO = open(escrito, 'w')
    for m in t:
        if len(m) == 0:
            f.write('\n')
        else:
            f.write(escribir_hasta_primer_numeral(m).rstrip() + '\n')
    f.close()
    
limpiador_de_comentarios('ej_1.py', 'ej_1_sin_comentarios.py')