# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 20:56:47 2022

@author: dafyd
"""

from ej_1 import Punto
from typing import List

class ConjuntoDePuntos():
    def __init__(self):
        self.puntos:List[Punto] = []
        self.sumaconjunto:Punto = Punto(0,0)
    
    def agregar(self, punto:Punto):
        self.puntos.append(punto)
        (self.sumaconjunto.x, self.sumaconjunto.y) = (self.sumaconjunto.x + punto.x, self.sumaconjunto.y + punto.y)
    
    def centro(self) -> Punto:
        p:Punto = Punto(self.sumaconjunto.x / len(self.puntos), self.sumaconjunto.y / len(self.puntos))
        return p
        