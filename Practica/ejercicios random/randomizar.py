# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:53:12 2022

@author: dafyd
"""
from typing import List
import random
def generar():  
    resultados = []
    for i in range(10001):
        m:int = random.randint(0,10)
        resultados.append(m)
    return resultados
    
def ordenar(ls:List[int]) -> List:
    ceros = 0
    unos = 0
    dos = 0
    tres = 0
    cuatro = 0
    cinco = 0
    seis = 0
    siete = 0
    ocho = 0
    nueve = 0
    diez = 0
    for i in ls:
        if i == 0:
            ceros = ceros + 1
        if i == 1:
            unos = unos + 1
        if i == 2:
            dos = dos + 1
        if i == 3:
            tres = tres + 1
        if i == 4:
            cuatro = cuatro + 1
        if i == 5:
            cinco = cinco + 1
        if i == 6 :
            seis = seis + 1
        if i == 7:
            siete = siete + 1
        if i == 8:
            ocho = ocho + 1
        if i == 9:
            nueve = nueve + 1
        if i == 10:
            diez = diez + 1
    res_ordenados = [ceros, unos, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez]
    return res_ordenados
a = generar()
b =ordenar(a)
def mayor_en_lista(ls:List[int]) -> int:
    res:int = 0
    for i in range(len(ls)):
        if ls[i] >= ls[res]:
            res = i
    return res
print(mayor_en_lista(b))