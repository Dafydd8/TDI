# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:08:07 2022

@author: dafyd
"""

from typing import List

xs:List[str] = ['a', 'b', 'c', 'd', 'e', 'f']
#                0    1    2    3    4    5
#                -6   -5   -4   -3   -2   -1

print(xs[-1]) #arroja 'f'
print(xs[1:5]) #arroja del elemento 1 incluido hasta 5 sin incluir. Esto es un SLICE
print(xs[1:5:2]) #arroja del elemento 1 a 5 (sin incluir) en saltos de a 2
print(xs[1:]) #arroja del elemnto 1 hasta el ultimo incluido
print(xs[:4]) #arroja del primero hasta el 4 (sin incluir)
print(xs[:]) #arroja todos los elementos, pero no es xs, es una lista nueva, raro...





