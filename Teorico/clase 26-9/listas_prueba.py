# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:12:49 2022

@author: dafyd
"""

from typing import List

frutas:List[str] = ['pera', 'banana', 'durazno', 'futilla']
print(frutas)

frutas[3] = 'frutilla'
print(frutas[3])

frutas.append('uva')
print(frutas)

list.append(frutas, 'uva')
print(frutas)

frutas.insert(0, 'anana')
print(frutas)

ultima_fruta:str = frutas.pop(1)
print(frutas)
print(ultima_fruta)