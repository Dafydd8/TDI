# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:42:58 2022

@author: dafyd
"""
from typing import List

def contar_strings_sin_repetir(ls:List[str]) -> int:
    c:set = set(ls)
    res:int = len(c)
    return res
#print(contar_strings_sin_repetir(['abc', 'd', 'ef', 'abc', 'ef', 'ef']))
    