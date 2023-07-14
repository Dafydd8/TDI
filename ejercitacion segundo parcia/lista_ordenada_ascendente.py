# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:27:48 2022

@author: dafyd
"""
from typing import List
def lista_ordenada_ascendente( xs : List [ int ]) -> bool :
    ''' Requiere : nada .
    Devuelve : True , si xs está ordenada en forma ascendente ;
    False en caso contrario .
    '''
    if len(xs) == 1 or len(xs) == 0:
        return True
    else:
        if xs[0] <= xs[1]:
            return True and lista_ordenada_ascendente(xs[1:])
        else:
            return False

a = [1,2,2,3,3,4,5,6]
print(lista_ordenada_ascendente(a))