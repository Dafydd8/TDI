from __future__ import annotations

import csv

from usuario import Usuario
from viaje import Viaje
from typing import Dict, List, TextIO

class DatasetViajes:
    def __init__(self, usuarios_filename: str, viajes_filename: str):
        u:TextIO = open(usuarios_filename, 'r', encoding = 'utf-8')
        v:TextIO = open(viajes_filename, 'r', encoding = 'utf-8')
        
        self.usuarios: Dict[int, Usuario] = {}
        for i in csv.DictReader(u):
            iden:int = int(i['id_usuario'])
            edad:int = int(i['edad_usuario'])
            usuario:Usuario = Usuario(iden, edad)
            self.usuarios[iden] = usuario
        u.close()    
        self.viajes_por_usuario: Dict[int, List[Viaje]] = {}
        for i in csv.DictReader(v):
            iden:int = int(i['id_usuario'])
            dur:int = int(i['duracion_recorrido'])
            origen:str = i['nombre_estacion_origen']
            destino:str = i['nombre_estacion_destino']
            viajes:List[Viaje] = []
            viaje:Viaje = Viaje(dur, origen, destino)
            viajes.append(viaje)
            if iden in self.viajes_por_usuario:
                self.viajes_por_usuario[iden].append(viaje)
            else:
                self.viajes_por_usuario[iden] = viajes
        v.close()

        # Importamos los usuarios primero
       	# recorro los usuarios
        # Tomo los datos y los convierto 
        # Creo el usuario y lo almaceno
        # Luego completamos con los datos de los viajes
        # Cierro ambos archivos

    def minutos_pedaleando(self, id_usuario: int) -> float:
        """Devuelve la cantidad de minutos acumulados en los viajes del usuario
        Pre: id_usuario in self.usuarios
        Post: Devuelve la suma de la duración de todos los viajes del usuario
              con id_usuario en minutos
        """
        res:float = 0
        for i in self.viajes_por_usuario[id_usuario]:
            res = res + i.duracion
        return res

    def minutos_promedio_para_edad(self, edad: int) -> float:
        """Devuelve el promedio de minutos pedaleados para los usuarios con cierta edad
        Pre: ninguna
        Post: Devuelve el promedio de los minutos pedaleados por todos los usuarios
              cuya edad es igual a la edad pasada por parámetro
        """
        res:float = 0
        contador:int = 0
        for i in self.usuarios:
            contador = contador + 1
            if self.usuarios[i].edad == edad:
                res = res + self.usuarios[i].edad
            
            
        

a = DatasetViajes('test-usuarios-data.csv', 'test-viajes-data.csv')
print(a.usuarios)
print(a.viajes_por_usuario)
print(a.minutos_pedaleando(1))