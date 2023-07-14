# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:11:04 2022

@author: dafyd
"""

def solo_consonantes(l:str):
    if len(l) == 1:
        if l[0] in 'aeiou':
            return ''
        else:
            return l[0]
    else:
        if l[0] in 'aeiou':
            return solo_consonantes(l[1:])
        else:
            return l[0] + solo_consonantes(l[1:])
print(solo_consonantes('logaritmo'))
        