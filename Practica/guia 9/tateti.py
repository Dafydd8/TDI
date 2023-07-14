# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 00:41:41 2022

@author: dafyd
"""

from ej_5 import Tateti
from typing import List, Tuple
from random import choice



print('Bienvenido al Tateti de Dafydd!')
input('Presione Enter para empezar: ')

seguir:bool = True
while seguir:
    tab:Tateti = Tateti()
    
    ficha_elegida:str = input('Ingrese X para jugar con cruz y O para jugar con circulo: ').upper()
    
    fi:str = ''
    if ficha_elegida == 'X':
        fi = 'O'
    else:
        fi = 'X'
    print(tab)
  
    while not(tab.fin()):
        
        juega:str = tab.turno_de()
        input('Turno de ' + juega)
        if juega == ficha_elegida:
            f:str = input('Ingrese su ficha como (fila,columna): ')
            valores:List[str] = f.split(',')
            x:int = int(valores[0])
            y:int = int(valores[1])
            tab.jugada(ficha_elegida, x, y)
            print(tab)
            
        else:
            lugares_seleccionables:List[Tuple[int, int]] = []
            for i in range(len(tab.tab)):
                for j in range(len(tab.tab[i])):
                    if tab.tab[i][j] == ' ':
                        lugares_seleccionables.append((i, j))         
            x:Tuple[int, int] = choice(lugares_seleccionables)
            tab.jugada(fi, x[0], x[1])        
            print(tab)
            
    print(tab)
    print('Fin del juego!')
    print('Ganador: ' + tab.gana())
    seg:str = input('Para volver a jugar presione Enter, para salir ingrese S: ')
    if seg.upper() == 'S':
        seguir = False
        
        
        
    

