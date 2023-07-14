from alojamiento_turistico import AlojamientoTuristico
from establecimiento_gastronomico import EstablecimientoGastronomico
from typing import List, TextIO, Tuple
import csv

class DataSetTuristico:
    
    def __init__(self, 
                 filename_alojamientos:str, 
                 filename_est_gastronomicos:str):
        ''' Inicializa un Dataset Turistico que englova a las clases Alojamiento Turistico
            y Establecimento Gastronomico, con atributos:
            -lista ordenada de Alojamientos Turisticos alojamientos_t
            -lista ordenada de Establecimientos Gastronomicos establecimientos_g
        '''
            
        a:TextIO = open(filename_alojamientos, 'r', encoding = 'utf-8')
        e:TextIO = open(filename_est_gastronomicos, 'r', encoding = 'utf-8')
        self.alojamientos_t:List[AlojamientoTuristico] = []
        self.establecimientos_g:List[EstablecimientoGastronomico] = []
        for i in csv.DictReader(a):
            if i['Lat'] != '' and i['Lat'] != ' ' and i['Long'] != '' and i['Long'] != ' ':
                nom:str = i['nombre']
                lat:float = float(i['Lat'])
                long:float = float(i['Long'])
                nom_calle:str = i['calle']
                alt_calle:int = int(i['altura'])
                tel:str = i['telefono']
                email:str = i['email']
                alo:AlojamientoTuristico = AlojamientoTuristico(nom, lat, long, nom_calle, alt_calle, tel, email)
                self.alojamientos_t.append(alo)
        a.close() 
        self.alojamientos_t.sort()
        for i in csv.DictReader(e):
            if i['lat'] != '' and i['lat'] != ' ' and i['long'] != '' and i['long'] != ' ' and i['altura'] != '' and i['altura'] != ' ':
                nom:str = i['establecimiento']
                lat:float = float(i['lat'])
                long:float = float(i['long'])
                rubro:str = i['rubro']
                calle:str = i['calle']
                altura:int = int(i['altura'])
                est:EstablecimientoGastronomico = EstablecimientoGastronomico(nom, calle, altura, rubro, long, lat)
                self.establecimientos_g.append(est)
        e.close()
        
    def alojamientos(self) -> List[AlojamientoTuristico]:
        ''' Requiere: Nada.
            Devuelve: Una lista con los alojamientos en el dateset ordenados alfabeticamente.
        '''
        return self.alojamientos_t
        
    def alojamiento_por_nombre(self, nom:str) -> AlojamientoTuristico:
        ''' Requiere: nom es el nombre de un alojamiento existente en dataset.
            Devuelve: El AlojamientoTuristico correspondiente al nombre dado.
        '''
        izq:int = 0
        ls:List[AlojamientoTuristico] = self.alojamientos_t
        der:int = len(ls)
        while izq < der:
            med:int = (izq + der) // 2
            if ls[med].nombre == nom:
                return ls[med]
            elif ls[med].nombre < nom:
                izq = med + 1
            else:
                der = med
                
    def tres_boliches_cercanos(self, aloj:AlojamientoTuristico) -> Tuple[EstablecimientoGastronomico, 
                                                                         EstablecimientoGastronomico, EstablecimientoGastronomico]:
        ''' Requiere: aloj es un Alojamiento Turistico existente en el Dataset.
            Devuelve: los Establecimientos Gastronomicos mas cercanos a aloj.
        '''
        res:Tuple[EstablecimientoGastronomico, EstablecimientoGastronomico, EstablecimientoGastronomico] = tuple()
        distancias:List[Tuple[EstablecimientoGastronomico, float]] = []
        menores:List[Tuple[EstablecimientoGastronomico, float]] = []
        
        for i in self.establecimientos_g:
            distancia:Tuple[EstablecimientoGastronomico, float] = (i, aloj.distancia(i.latitud, i.longitud))
            distancias.append(distancia)
          
        for j in range(3):
            pos:int = 0
            for i in range(len(distancias)):
                if distancias[i][1] < distancias[pos][1]:
                    pos = i
            menores.append(distancias[pos])
            distancias.pop(pos)
                
        res = (menores[0][0], menores[1][0], menores[2][0])
        return res
    
    def boliche_proximo_de_rubro(self, aloj:AlojamientoTuristico, rub:str) -> EstablecimientoGastronomico:
        '''Requiere: aloj es un Alojamiento Turistico existente en el Dataset,
            y rub es un rubro pertenciente a algun Establecimento Gastronomico en el Dataset.
            Devuelve: el Establecimiento Gastronomico con rubro rub mas cercano a aloj.
        '''
        
        candidatos:List[EstablecimientoGastronomico] = []
        distancias:List[Tuple[EstablecimientoGastronomico, float]] = []
        pos:int = 0
        for i in self.establecimientos_g:
            if i.rubro == rub:
                candidatos.append(i)
        for i in candidatos:
            distancia:Tuple[EstablecimientoGastronomico, float] = (i, aloj.distancia(i.latitud, i.longitud))
            distancias.append(distancia)
        for i in range(0, len(distancias)):
            if distancias[i][1] < distancias[pos][1]:
                pos = i
        res:EstablecimientoGastronomico = distancias[pos][0]
        return res

a = DataSetTuristico('alojamientos-turisticos1.csv', 'establecimientos-gastronomicos2.csv')