# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 10:00:48 2022

@author: dafyd
"""

def clasificar_por_longitud(palabra:str) -> str:
    '''Requiere:
       Devuelve:
    '''
    if len(palabra) == 0:
        vr:str = 'no existe'
    elif len(palabra) >= 10:
        vr:str = ' es larga'
    elif len(palabra) >= 6:
        vr:str = ' es mediana'
    else:
        vr:str = ' es corta'
        
    return vr

pal:str = 'Linguistica'
msj:str = 'La palabra ' + pal + clasificar_por_longitud(pal)
print(msj)