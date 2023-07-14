# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:55:18 2022

@author: dafyd
"""
from typing import List
from random import choice

class Tateti():
    def __init__(self):
        self.tab:List[List[str]] = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        self.juega:str = choice(['X','O'])
        self.lugares = 9
        
    def __repr__(self):
        return str(self.tab[0]) + '\n' + str(self.tab[1]) + '\n' + str(self.tab[2]) + '\n'
    
    def turno_de(self):
        if self.juega == 'X':
            self.juega = 'O'
        elif self.juega == 'O':
            self.juega = 'X'
        return self.juega
    
    def jugada(self, ficha:str, fila:int, columna:int):
        '''
            Requiere: ficha = 'X' o ficha = 'O'
            modifica: el tablero (self.tab)
        '''
        self.tab[fila][columna] = ficha
        self.lugares = self.lugares - 1

        
    def fin(self) -> bool:
        if self.tab[0][0] == self.tab[0][1] == self.tab[0][2] and not (' ' in (self.tab[0][0], self.tab[0][1], self.tab[0][2])):
            return True
        elif self.tab[0][0] == self.tab[1][0] == self.tab[2][0] and not (' ' in (self.tab[0][0], self.tab[1][0], self.tab[2][0])):
            return True
        elif self.tab[0][0] == self.tab[1][1] == self.tab[2][2] and not (' ' in (self.tab[0][0], self.tab[1][1], self.tab[2][2])):
            return True
        elif self.tab[0][1] == self.tab[1][1] == self.tab[2][1] and not (' ' in (self.tab[0][1], self.tab[1][1], self.tab[2][1])):
            return True
        elif self.tab[0][2] == self.tab[1][2] == self.tab[2][2] and not (' ' in (self.tab[0][2], self.tab[1][2], self.tab[2][2])):
            return True
        elif self.tab[0][2] == self.tab[1][1] == self.tab[2][0] and not (' ' in (self.tab[0][2], self.tab[1][1], self.tab[2][0])):
            return True
        elif self.tab[1][2] == self.tab[1][1] == self.tab[1][0] and not (' ' in (self.tab[1][2], self.tab[1][1], self.tab[1][0])):
            return True
        elif self.tab[2][2] == self.tab[2][1] == self.tab[2][0] and not (' ' in (self.tab[2][2], self.tab[2][1], self.tab[2][0])):
            return True
        if self.lugares == 0:
            return True

    
    def gana(self) -> str:
        ganador:str = ''
        if self.tab[0][0] == self.tab[0][1] == self.tab[0][2]:
            ganador = self.tab[0][0]
        elif self.tab[0][0] == self.tab[1][0] == self.tab[2][0]:
            ganador = self.tab[0][0]
        elif self.tab[0][0] == self.tab[1][1] == self.tab[2][2]:
            ganador = self.tab[0][0]
        elif self.tab[0][1] == self.tab[1][1] == self.tab[2][1]:
            ganador = self.tab[0][1]
        elif self.tab[0][2] == self.tab[1][2] == self.tab[2][2]:
            ganador = self.tab[0][2]
        elif self.tab[0][2] == self.tab[1][1] == self.tab[2][0]:
            ganador = self.tab[0][2]
        elif self.tab[1][2] == self.tab[1][1] == self.tab[1][0]:
            ganador = self.tab[1][1]
        elif self.tab[2][2] == self.tab[2][1] == self.tab[2][0]:
            ganador = self.tab[2][2]
        else:
            ganador = 'empate'
        return ganador
