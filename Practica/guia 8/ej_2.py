# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:24:17 2022

@author: dafyd
"""
from typing import Tuple
import math

#a)
def distancia_al_origen(p:Tuple[float, float]) -> float:
    res:int = math.sqrt(p[0]**2 + p[1]**2)
    return res
#print(distancia_al_origen((3,5)))

#b)
def suma_puntos(p1:Tuple[float, float], p2:Tuple[float, float]) -> Tuple[float, float]:
    res:Tuple[float,float] = (p1[0] + p2[0], p1[1] + p2[1])
    return res
#print(suma_puntos((4,3), (5,2)))

#c)
def sumar_float(p:Tuple[float, float], x:float) -> Tuple[float, float]:
    res:Tuple[float, float] = (p[0] + x, p[1] + x)
    return res
#print(sumar_float((1,3), 2))

#d)
def punto_entero_mas_cercano(p:Tuple[float, float]) -> Tuple[float, float]:
    res:Tuple[float, float] = (round(p[0]), round(p[1]))
    return res
#print(punto_entero_mas_cercano((2.3,8.9)))

