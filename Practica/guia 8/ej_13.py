# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 17:56:27 2022

@author: dafyd
"""
from typing import Dict
from typing import List

def construir_tabla ( n : int ) -> Dict [ int , int ]:
    ''' ... completar ... '''
    r : Dict [ int , int ] = dict ()
    i : int = 1
    while i <= n :
        r [ i ] = i * i
        i = i + 1
    return r

def filtrar ( tabla : Dict [ int , int ] , digito : int ) :
    ''' ... completar ... '''
    claves_a_eliminar : List [ int ] = []
    for k in tabla :
        valor : int = tabla [ k ]
        ultimo_digito : int = int ( str ( valor ) [ -1])
        if ultimo_digito != digito :
            claves_a_eliminar . append ( k )
    for k in claves_a_eliminar :
        tabla . pop ( k )

tabla : Dict [ int , int ] = construir_tabla (10)
otra : Dict [ int , int ] = tabla


#c)
def filtrar_v2 ( tabla : Dict [ int , int ] , digito : int ) :
    ''' ... completar ... '''
    res:Dict[int, int] = dict()
    claves_resultado : List [ int ] = []
    for k in tabla :
        valor : int = tabla [ k ]
        ultimo_digito : int = int ( str ( valor ) [ -1])
        if ultimo_digito == digito :
            claves_resultado . append ( k )
    for k in claves_resultado :
        res[k] = tabla[k]
    return res

nuevo = filtrar_v2 ( tabla , 9)
print(nuevo)
print ( tabla )
print ( otra )
