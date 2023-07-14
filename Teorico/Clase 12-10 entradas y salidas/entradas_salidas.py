# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 09:53:09 2022

@author: dafyd
"""

def sumar_un0(x:int) -> int:
    '''
        Requiere: Nada
        Devuelve: x+1
    '''
    return x + 1

#hasta ahora, las entradas de los programas estaban determinadas en el codigo (hardcodeados, literales)
#y salidas con print. A partir de ahora vamos a ver interaccion con LECTURA Y ESCRITURA de archivos de texto
#y mediante entrada por teclado durante ejecucion.

#Archivo: Agrupacion logica. Coleccion numerada y ordenada de bytes. ALmacena datos procesabeles por un programa.
#se almacenan en en medio fisico (disco rigido o whatever).
#Son leidos o escritos por un programa en ejecucion, el cual almacena sus datos en variables, en la memoria de la computadora.

#Archivos dividos (a grandes rasgos en):
    #texto: solo tiene caracteres de acuerdo a alguna codificacion (ASCII, Unicode). Lo lees con editor de texto (spyder, notepad o whatever. Word NO!).
    #binarios: los que no son de texto. Videos, imagenes, archivos de word (por fuentes, negrita, justificado, imagenes, etc.)
               #musica, o lo que sea.

#Los de texto ls vmaos a abrir con un file handler

#Para usar typehints de tipos de archivos hay q importar from typing import textIO

from typing import TextIO

f:TextIO = open('provincias.txt')
texto:str = f.read()
#print(texto)

#Los archivos de texto son iterables. Tiene ventaja que uso menos memoria. Voy cargando y descartando.
f:TextIO = open('provincias.txt')
for linea in f:
    linea = linea.rstrip() #elimina los espacios (el /n en este caso) a la derecha del str (linea ya es un str, ya no es archivo). lstrip() elimina lo de la izquierda lol, y strip() todo.
    print(linea)
    
