# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:04:32 2022

@author: dafyd
"""
from ej_1 import Punto
from ej_4 import ConjuntoDePuntos

p:Punto = Punto(1.0, 5.0)
q:Punto = Punto(3.0, -5.0)
r:Punto = Punto(0.5, 9.9)

puntos:ConjuntoDePuntos = ConjuntoDePuntos()

puntos.agregar(p)
puntos.agregar(q)
puntos.agregar(r)

h:Punto = puntos.centro()
print(h)

