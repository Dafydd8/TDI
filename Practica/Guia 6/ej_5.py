# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:32:33 2022

@author: dafyd
"""
import ejercicio_3_guia_4
import ejercicio_3_guia_5
from typing import List
continuar: bool = True

print("Funciones disponibles \n------------------------------")
print("A. Cuadrado\nB. Inverso \nC. Creciente \nG. Finalizar")

accion = (input('Elija funcion: '))
if accion.upper() == 'G':
    continuar = False
    
while (continuar):
    if accion.upper() == 'A':
        n:int = int(input("Ingrese n: "))
        print(ejercicio_3_guia_4.cuadrado_asteriscos(n))
        print("Presione enter para continuar")
        input()
        accion = input("Elija funcion: ")
        
    elif accion.upper() == 'B':
        t:str = input("Ingrese un texto: ")
        print(ejercicio_3_guia_4.string_inverso(t))
        print("Presione enter para continuar")
        input()
        accion = input("Elija funcion: ")
    
    elif accion.upper() == 'C':
        t:str = input('Ingrese una lista de enteros separados por comas: ')
        ls:List[str] = t.split(', ')
        lsfinal:List[int] = []
        for i in range(len(ls)):
            lsfinal.append(int(ls[i]))
        if ejercicio_3_guia_5.enteros_ordenados(lsfinal):
            print('La lista ingresada está ordenada en forma estrictamente creciente.')
        else:
            print('La lista ingresada no está ordenada en forma estrictamente creciente.')
        print("Presione enter para continuar")
        input()
        accion = input("Elija funcion: ")
          
    elif(accion.upper() == "G"):
        continuar = False
        