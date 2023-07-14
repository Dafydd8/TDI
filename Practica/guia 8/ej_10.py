# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 16:31:16 2022

@author: dafyd
"""

from typing import List, Dict

def deletrear(s:str) -> str:
    letras:str = 'abcdefghijklmnñopqrstuvwxyz'
    pronunciaciones:Dict[str, str] = dict()
    pronunciaciones_lista:List[str] = ['a', 'be', 'ce', 'de', 'e', 'efe', 'ge', 'ache', 'i', 'jota', 'ka', 'ele', 'eme', 'ene', 'eñe', 'o', 'pe', 'qu', 'erre', 'ese', 'te', 'u', 've', 'doble ve', 'equis', 'ye', 'zeta']
    for i in range(len(letras)):
        pronunciaciones[letras[i]] = pronunciaciones_lista[i]
        
    res:str = ''
    for i in range(len(s)):
        res = res + pronunciaciones[s[i]] + ' '
    return res

print(deletrear('hola'))
    
    

    