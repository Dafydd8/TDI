from fruta import Fruta
from typing import TextIO, List
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
        maxs:TextIO = open(precios_maximos_csv, 'r', encoding = 'utf-8')
        cata:TextIO = open(catalogo_fruteria_csv, 'r', encoding = 'utf-8')
        self.maximos:List[Fruta] = []
        self.catalogo:List[Fruta] = []
        for i in csv.DictReader(maxs):
            fru:Fruta = i['FRUTA']
            pre:float = float(i['PRECIO'])
            nueva_fruta:Fruta = Fruta(fru, pre)
            self.maximos.append(nueva_fruta)
        maxs.close()
        for i in csv.DictReader(cata):
            fru:Fruta = i['FRUTA']
            pre:float = float(i['PRECIO'])
            nueva_fruta:Fruta = Fruta(fru, pre)
            self.catalogo.append(nueva_fruta)
        cata.close()
        
    def fruteria_en_regla(self) -> bool:
        '''
        Requiere: nada
        Devuelve: True, si los precios de todas las frutas son 
                  menores o iguales a los precios máximos; 
                  False en caso contrario.
        '''
        for catalogada in self.catalogo:
            for referencia in self.maximos:
                if catalogada.nombre == referencia.nombre:
                    if catalogada.precio > referencia.precio:
                        return False
        return True
    
    def cant_precios_excedidos(self) -> int:
        '''
        Requiere: nada
        Devuelve: la cantidad de frutas de la frutería cuyo precio excede
                  al máximo permitido.
        '''
        res:int = 0
        for catalogada in self.catalogo:
            for referencia in self.maximos:
                if catalogada.nombre == referencia.nombre:
                    if catalogada.precio > referencia.precio:
                        res = res + 1
        return res
