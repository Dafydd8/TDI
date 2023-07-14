from __future__ import annotations
from pocion import Pocion
from typing import Dict, List, TextIO, Set, Tuple
import csv

class CatalogoPociones:
    def __init__(self, archivo_csv:str):
        '''
        Inicializa el catálogo de pociones, cargando las pociones
        contenidas en el archivo archivo_csv que tienen el nivel de
        dificultad definido (el resto las ignora).
        Requiere: archivo_csv es el nombre de un archivo en formato
                  CSV (valores separados por punto y coma), con cinco columnas:
                  'Name' (str), 'Known ingredients' (lista de
                  strings separados por comas), 'Effect' (str),
                  'Characteristics' (str), 'Difficulty level' (str).
        '''
        self.pociones_dificultad:Dict[str, Set[Pocion]] = dict()
        f:TextIO = open(archivo_csv, 'r', encoding=('utf-8'))
        for i in csv.DictReader(f, delimiter = ';'):
            nom:str = i['Name']
            ing:List[str] = i['Known ingredients'].split(',')
            for k in range(len(ing)):
                ing[k] = ing[k].strip() 
            efe:str = i['Effect']
            car:str = i['Characteristics']
            dif:str = i['Difficulty level']
            p:Pocion = Pocion(nom, ing, efe, car, dif)
            if p.nivel_dificultad != '':
                if p.nivel_dificultad in self.pociones_dificultad:
                    self.pociones_dificultad[p.nivel_dificultad].add(p)
                else:
                    self.pociones_dificultad[p.nivel_dificultad] = {p}
                

    def __repr__(self):
        '''
        Genera la representación de una catálogo de pociones como string.
        Requiere: nada.
        Devuelve: el string que representa al catálogo.
        '''
        return str(self.pociones_dificultad)

    def listar_por_dificultad(self, dif:str) -> List[Pocion]:
        '''
        Requiere: nada
        Devuelve: una lista de Pociones, donde dif
        correposnde a una cierta dificultad recibida como argumento que se corresponde
        con la dificultad de las pociones que se deben guardar en la lista de salida.
        Por ejemplo, si el método se invoca con el argumento 'Advanced', la lista contendrá
        pociones de tipo Advance.
        Además, en la lista las pociones aparecen
        ordenadas de acuerdo al orden definido en la clase Pocion.
        '''
        pociones:List[Pocion] = []
        for i in self.pociones_dificultad:
            if i == dif:
                pociones = list(self.pociones_dificultad[i])
        pociones.sort()
        
        return pociones

    def listar_pociones_con_n_ingredientes(self, n:int) -> List[Tuple[str,Pocion]]:
        '''
        Requiere: n > 0
        Devuelve: una lista de tuplas dónde cada tupla almacena una poción y su dificultad.
        Las pociones que conforman las tuplas de la listas son aquellas que tienen n ingredientes.
        '''
        t:Tuple[str, Pocion] = tuple()
        res:List[Tuple[str,Pocion]] = []
        for i in self.pociones_dificultad: #para cada clave en diccionario
            for j in self.pociones_dificultad[i]: #para cada pocion en conjunto
                if '' in j.ingredientes_conocidos:
                    j.ingredientes_conocidos.pop
                if len(j.ingredientes_conocidos) == n and not('' in j.ingredientes_conocidos):
                    t = (j.nivel_dificultad, j)
                    res.append(t)
        return res
a:CatalogoPociones = CatalogoPociones('Potions-mini.csv')
print(a.listar_por_dificultad('Beginner'))
print(a.listar_pociones_con_n_ingredientes(3))
        
        
        
        