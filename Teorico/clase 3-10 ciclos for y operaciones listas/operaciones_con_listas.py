# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:55:44 2022

@author: dafyd
"""

#range() devuelve un elemento de tipo range. Lo
#convertimos a lista para instanciar sus enteros (para desplegar el rango),
#pero la conversión no es necesaria en general.

a = list(range(3, 10, 2))
b = range(3, 10, 2)

#.join()
c = ['Hola', 'soy', 'Dafydd']
d = ', '.join(c)
                             #Inversas
#.split()
e = 'Hola soy Dafydd'
f = e.split(' ')
print(f)


    
