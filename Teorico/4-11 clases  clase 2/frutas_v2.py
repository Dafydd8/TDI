# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:14:32 2022

@author: dafyd
"""
from typing import Fruta
from typing import List, TextIO, Set
import csv

frutas:List[Fruta] = []
f:TextIO = open('frutas.csv')
for dic in csv.DictReader(f):
    nom:str = dic['nombre']
    pre:float = float(dic['precio'])
    est:Set[str] = set(dic['estaciones'].split('. '))
    x:Fruta = Fruta(nom, pre, est)
    frutas.append(x)
 
f.close()

