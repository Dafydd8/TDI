# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 16:14:07 2022

@author: dafyd
"""
from typing import Dict

def repeticion_caracteres(s:str) -> Dict[str, int]:
    res:Dict[str, int] = dict()
    for i in range(len(s)):
        res[s[i]] = 0
    for i in range(len(s)):
        res[s[i]] = res[s[i]] + 1
    return res
print(repeticion_caracteres('hola mundo'))
    