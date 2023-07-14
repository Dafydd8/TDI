# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:23:06 2022

@author: dafyd
"""

import random

basta:bool = True

while basta:
    n:int = random.randint(10, 20)
    m:int = random.randint(10, 20)
    res = int(input('Ingresar el resultado de ' + str(n) + '*' + str(m) + ': '))
    if res ==  n*m:
        print('Bien!')
    else:
        print('Mal! Resultado correcto: ' + str(n*m))
    
    sigo = input('Ingrese c para continuar y g para finalizar: ')
    
    if sigo.upper() == 'G':
        basta = False
        
        