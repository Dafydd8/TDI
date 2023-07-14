# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:33:40 2022

@author: dafyd
"""
from typing import Set
from typing import Dict

def caracteres(s:str) -> Set[str]:
    '''
        requiere: nada.
        devuelve: el conjunto de  los caracteres en s
    '''
    res:Set[str] = set()
    for i in range(len(s)):
        res.add(s[i])
    return res
print(caracteres('zaracatunga'))

def caracteres_en_comun(s:str, t:str) -> Set[str]:
    ''' Requiere: nada.
        Devuelve: el conjunto de los caracteres que aparecen
        tanto en s como en t.
        Ej: caracteres_en_comun('bananas', 'peras') → {'a', 's'}
    '''
    eses:Set[str] = caracteres(s)
    tes:Set[str] = caracteres(t)
    return eses & tes
print(caracteres_en_comun('hola', 'pasas'))

def recitar(n:int ) -> str :
    ''' Requiere: n >= 0
         Devuelve: un string con la recitación de los dígitos de n,
         en minúsculas y separados por espacios en blanco.
    '''
    ent:Dict = dict()
    res:str = ''
    ent[str(1)] = 'uno'
    ent[str(2)] = 'dos'
    ent[str(3)] = 'tres'
    ent[str(4)] = 'cuatro'
    ent[str(5)] = 'cinco'
    ent[str(6)] = 'seis'
    ent[str(7)] = 'siete'
    ent[str(8)] = 'ocho'
    ent[str(9)] = 'nueve'
    ent[str(0)] = 'cero'
    for i in str(n):
        res = res + ent[i] + ' '
    return res
print(recitar(1234))
    