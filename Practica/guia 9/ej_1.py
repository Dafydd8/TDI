# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:14:45 2022

@author: dafyd
"""
import math

class Punto:
    def __init__(self, equis:float, ye:float): #a)
        self.x:float = equis
        self.y:float = ye
    
    def __repr__(self) -> str: #f)
        return '(' + str(self.x) + ', ' + str(self.y) + ')' 
    
    def distancia_a(self, other) -> float: #b)
        distancia:float = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distancia
    
    def distancia_al_origen(self) -> float: #c)
        distancia:float = math.sqrt(self.x**2 + self.y**2)
        return distancia
    
    def __add__(self, other): #d)
        res:Punto = Punto(self.x + other.x, self.y + other.y)
        return res
    
    def __eq__(self, other): #e)
        return self.x == other.x and self.y == other.y
    
