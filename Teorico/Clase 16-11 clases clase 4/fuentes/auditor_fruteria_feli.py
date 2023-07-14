from fruta import Fruta
from typing import List, Tuple, TextIO
import csv

class AuditorFruteria:
    ''' Clase para controlar los precios de una frutería '''

    def __init__(self, precios_maximos_csv:str, catalogo_fruteria_csv:str):
        ''' Inicializan auditor. 
            Requiere: - los archivos tienen dos columnas: NOMBRE y PRECIO
                      - en los archivos de entrada no hay dos renglones 
                        distintos que refieran a la misma fruta.
                      - todas las frutas listadas en catalogo_fruteria_csv
                        tienen definido un precio máximo en precios_maximos_csv
        '''
        m: TextIO = open(precios_maximos_csv, 'r', encoding = 'utf-8') #precios maximos
        c: TextIO = open(catalogo_fruteria_csv, 'r', encoding = 'utf-8') #precios de comercializaci�n
        self.preciosmax: List[Tuple[str, float]] = []
        self.precioscom: List[Fruta] = []
        for i in csv.DictReader(m):
            fru: str = i['FRUTA']
            pre: float = float(i['PRECIO'])
            maximo: Tuple[str, float] = [fru, pre]
            self.preciosmax.append(maximo)
        m.close()
        for e in csv.DictReader(c):
            fru: str = i['FRUTA']
            pre: float = float(i['PRECIO'])
            comerc: Fruta = Fruta(fru, pre)
            self.precioscom.append(comerc)
        c.close()
            
    def fruteria_en_regla(self) -> bool:
        '''
        Requiere: nada
        Devuelve: True, si los precios de todas las frutas son 
                  menores o iguales a los precios máximos; 
                  False en caso contrario.
        '''
        for i in self.preciosmax: #O(N) 
            if i[0] == self.precioscom[i].nombre: #O(N)
                if i[1] <= self.precioscom[i].precios: #O(N)
                    return False
        return True #si pasa el ciclo, debe returnear true.
    
    def cant_precios_excedidos(self) -> int:
        '''
        Requiere: nada
        Devuelve: la cantidad de frutas de la frutería cuyo precio excede
                  al máximo permitido.
        '''
        contador: int = 0
        for i in self.preciosmax: 
            if i[0] == self.preciocom[i].nombre:
                if i[1] > self.precioscom[i].precios:
                    contador = contador + 1
        return contador
    
