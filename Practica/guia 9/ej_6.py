# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:52:12 2022

@author: dafyd
"""

from typing import List, TextIO
import csv

#a)
class Provincia():
    def __init__(self, nom:str, abre:str, area:float, p_prov:int, cap:str, p_cap:int):
        self.nom = nom
        self.abre = abre
        self.area = area
        self.p_prov = p_prov
        self.cap = cap
        self.p_cap = p_cap
        
    def __lt__(self, other):
        densidad1:float = int(self.p_prov) / float(self.area)
        densidad2:float = int(other.p_prov) / float(other.area)
        return densidad1 < densidad2
    
    def __repr__(self):
        return self.nom + '. ' + str(int(self.p_prov) / float(self.area) // 1) + '\n'
    
#b)
def listar_provincias(archivo_csv:str) -> List[Provincia]:
    provincias:List[Provincia] = []
    s:TextIO = open(archivo_csv)
    for i in csv.DictReader(s):
        nom:str = i['Provincia']
        abre:str = i['Abreviatura']
        area:float = i['Area']
        p_prov:int = i['PoblacionProvincia']
        cap:str = i['Capital']
        p_cap:int = ['PoblacionCapital']
        x:Provincia = Provincia(nom, abre, area, p_prov, cap, p_cap)
        provincias.append(x)
    return provincias

#c)
a:List[Provincia] = listar_provincias('provincias_2.csv')
a.sort()
a.reverse()
print(a)  