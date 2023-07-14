# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:37:33 2022

@author: dafyd
"""
from typing import Tuple, List

def buscar ( elem : int , lista : List [ int ]) -> Tuple [ bool , int ]:
    ''' Requiere : nada .
        Devuelve : ( True , p ) si elem aparece en la lista por primera vez
        en la posición p ; o bien ( False , None ) si no aparece nunca .
    '''
    res:Tuple[bool, int] = (False, None)
    for i in range(len(lista)):
        if lista[i] == elem:
            res = (True, i)
    return res
print(buscar(3, [1,3,4,5]))