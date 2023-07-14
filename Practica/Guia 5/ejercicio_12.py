# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:41:42 2022

@author: dafyd
"""

from typing import List

def primera_ocurrencia(elem:int, ls:List[int]) -> int:
    '''
        Requiere : ls contiene al menos una ocurrencia de elem .
        Devuelve : el índice de la primera ocurrencia de elem en ls .
    '''
    for m in range(len(ls)):
        if ls[m] == elem:
            return m


        