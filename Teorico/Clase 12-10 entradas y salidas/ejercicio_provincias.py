# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:44:58 2022

@author: dafyd
"""

from typing import TextIO
from typing import List

f:TextIO = open('provincias.txt')

for linea in f:
    linea = linea.strip()
    provincias:List[str] = linea.split('___')
    print(provincias[1])

