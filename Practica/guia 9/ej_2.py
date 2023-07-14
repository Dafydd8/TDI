# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:43:59 2022

@author: dafyd
"""
from random import randint
from typing import List

#a)
class Dado:
    def __init__(self, caras:int):
        self.n:int = caras
        self.valor_actual:int = 1
     
    def tirar(self):
        self.valor_actual = randint(1, self.n)
    
    def __repr__(self):
        return str(self.valor_actual)

#b)
class Cubilete:
    def __init__(self):
        self.dados:List[Dado] = []
        for i in range(5):
            i = Dado(6)
            self.dados.append(i)
        
    def tirar_todos(self):
        for i in self.dados:
            i.tirar()
    
    def __repr__(self) -> str:
        res:str = str(self.dados[0])
        for i in range(1,5):
            res = res + ', ' + str(self.dados[i])      
        return '[' + res + ']'
    
#c)
def generala():
    a:Cubilete = Cubilete()
    
    a.tirar_todos()
    print(a)
    
    r = input('Ingrese posiciones (0-4) de los dados a volver a tirar (para pasar presione P): ')
    if r.upper() == 'P':
        pass
    else:
        repetir:List[int] = r.split(',')
        for i in repetir:
            pos:int = int(i)
            a.dados[pos].tirar()
        print(a)
    
        r = input('Ingrese posiciones (0-4) de los dados a volver a tirar (para pasar presione P): ')
    
        repetir.clear()
        repetir = r.split(',')
        if r.upper() == 'P':
            pass
        else:
            repetir:List[int] = r.split(',')
            for i in repetir:
                pos:int = int(i)
                a.dados[pos].tirar()
            print(a)
    
    print('Fin del Turno')

print('Bienvenido a la Generala de Dafydd!')
start = input('Para comenzar a jugar ingrese S: ')
seguir:bool = True

if start.upper() == 'S':
    while seguir:
        generala()
        continuar = input('Para el siguiente turno ingrese C, para salir ingrese cualquier otra letra: ')
        if continuar.upper() == 'C':
            seguir = True
        else:
            seguir = False
        

   
                    
        
        
        

    
    