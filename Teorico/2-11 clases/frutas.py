# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 09:53:22 2022

@author: dafyd
"""

from typing import Tuple, List, Set, Dict

PRI = 'primavera' 
VER = 'verano'
OTO = 'otoño'
INV = 'invierno'

# b = ('banana de ecuador', 150.0, {INV, OTO, VER})
# p = ('pera williams', 70.0, {VER})
# u = ('uva verde', 60.0, {PRI, VER})

# fruteria:Dict[str, Tuple[str, float, Set[str]]] = dict()
# fruteria['banana'] = b
# fruteria['pera'] = p
# fruteria['uva'] = u

class Fruta:
    def __init__(self, nom:str, pre:float, est:Set[str]): #DEFINO EL CONSTRUCTOR
      self.nombre:str = nom
      self.precio:float = pre
      self.estaciones:Set[str] = est
    
    def disponible_en(self, estacion:str) -> bool:
        ''' Requiere: estacion es 'verano', 'otoño', 'invierno' o 'verano'
            Devuelve: True si estacion esta en las estaciones de la Fruta. False en caso contrario
        '''
        return estacion in self.estaciones
    
    def __repr__(self) -> str:
        '''devuelve representacion en str de la fruta'''
        return self.nombre + '($' + str(self.precio) + '/kg)'
    
    def __lt__(self, other) -> bool: #lt por less than... le indico a python como se ordenan mis frutas (por precio)
        return self.precio < other.precio
        





  