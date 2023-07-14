# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:40:03 2022

@author: dafyd
"""

def f ( b : str ) -> int :
    ''' Requiere : b es un string de 0 s y 1 s . '''
    if len ( b ) ==0:
        return 0
    else :
        aux : int = f ( b [: -1])
        return aux * 2 + int ( b [ -1])
print ( f ( '1100') )
print ( f ( '111111') )
