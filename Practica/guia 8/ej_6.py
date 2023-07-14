# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:47:42 2022

@author: dafyd
"""

from typing import List

def es_programa(t:str) -> bool:
    abecedario:set = {"a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    for i in range(len(t)):
        if t[i] in abecedario:
            abecedario.remove(t[i])
    if len(abecedario) == 0:
        return True
    else:
        return False
    
print(es_programa('extraño pan de col y kiwi se quemo bajo fugaz vaho'))
