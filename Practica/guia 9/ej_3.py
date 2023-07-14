# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 16:49:32 2022

@author: dafyd
"""

from naipes import Naipe , Mazo

mazo : Mazo = Mazo ()
mazo . agregar ( Naipe (7 , 'oros') )
mazo . agregar ( Naipe (1 , 'espadas') )
mazo . agregar ( Naipe (12 , 'copas') )
mazo . agregar ( Naipe (4 , 'bastos') )
mazo . ordenar ()

print(mazo)
