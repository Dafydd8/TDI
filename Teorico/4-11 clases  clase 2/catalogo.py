# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:44:25 2022

@author: dafyd
"""
from frutas import Fruta
from typing import List, TextIO, Set, Dict, Tuple
import csv

class Catalogo:
    def __init__(self, archivo_csv:str):
        self.frutas:List[Fruta] = []
        f:TextIO = open(archivo_csv)
        for dic in csv.DictReader(f):
            nom:str = dic['nombre']
            pre:float = float(dic['precio'])
            est:Set[str] = set(dic['estaciones'].split('. '))
            x:Fruta = Fruta(nom, pre, est)
            self.frutas.append(x)
        f.close()
        
    def frutas_de_estacion(self, estacion:str) -> List[Fruta]:
        res:List[Fruta] = []
        for i in self.frutas:
            if i.disponible_en(estacion):
                res.append(i)
        return res
    
    
class Carrito:
    def __init__(self):
        self.kilos:Dict[Fruta, int] = dict()
        self.precio_total:int = 0
    
    def agregar(self, f:Fruta, p:int):
        '''Modifica: agrega p kilos ade la fruta f al carrito
            requiere: p > 0
        '''
        if f in self.kilos:
            self.kilos[f] = self.kilos[f] + p
        else:
            self.kilos[f] = p
        self.precio_total = self.precio_total + f.precio * p
            
    def calcular_precio(self) -> float:
        vr:float = 0.0
        for i in self.kilos:
            vr = vr + self.kilos[i] * i.precio
        return vr
    def calcular_precio_v2(self) -> float:
        vr:float = 0.0
        for fruta, peso in self.kilos.items():
            vr = vr + peso * fruta.precio
        return vr
    def calcular_precio_v3(self) -> float:
        return self.precio_total
    
a=Fruta('banana', 2, {'verano', 'primavera'})
b = Fruta('cereza', 3, {'verano'})
c = Fruta('uva', 4, {'otoño', 'primavera'})
        
def fruta_mas_cara(lis:List[Fruta], est:str) -> Fruta:
    maximo:Tuple[Fruta, float] = (lis[0], 0)
    for i in lis:
        if i.disponible_en(est):
            if i.precio > maximo[1]:
                maximo = (i, i.precio)
    return maximo[0]
print(fruta_mas_cara([a,b,c],'verano'))
    
    
        
        
                
        