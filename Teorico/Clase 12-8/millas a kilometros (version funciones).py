# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 10:26:17 2022

@author: dafyd
"""

#Definicion de la funcion
def millas_a_kilometros(d: float) -> float:
    #esto es el docstring
    '''Requiere: d >= 0
       Devuelve: el resultado (aproximado) de
       convertir d de millas a kilómetros, sabiendo que 1 mi~1.60934 km.
    '''
    res:float = d * 1.60934
    return res

def f2c(f: float) -> float:
    '''rquiere: f >= -460
       Devuelve: el resultado (aprox) de convertir f grados fahrenheit
       a grados celsius.
    '''
    cel:float = (f-32)*5/9
    return cel
    
#Cuerpo principal del programa
mi:float = 22.3
km:float = millas_a_kilometros(mi)

msg:str = str(mi) + ' mi equivalen a ' + str(km) + ' km.'
print(msg)



