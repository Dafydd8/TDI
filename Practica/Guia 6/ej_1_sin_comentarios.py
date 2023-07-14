
"""
Created on Wed Oct 19 17:38:00 2022

@author: dafyd
"""

from typing import List
from typing import TextIO


def caracteres_en_linea(nombre_archivo:str) -> List[int]:
    res:List[int] = []
    t:TextIO = open(nombre_archivo)
    for i in t:
        res.append(len(i.rstrip()))
    return res




def caracteres_en_linea_v2(archivo_leido:str, archivo_a_escribir) -> List[int]:
    f:TextIO = open(archivo_a_escribir, 'w')
    t:TextIO = open(archivo_leido)
    for i in t:
        f.write(str(len(i.rstrip())) + '\n')
    f.close()

print(caracteres_en_linea_v2('provincias.txt', 'cantidad_lineas_en_provs.txt'))

