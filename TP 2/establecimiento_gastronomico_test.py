import unittest
import csv
from typing import List, TextIO
from establecimiento_gastronomico import EstablecimientoGastronomico

def cargar_establecimientos(archivo_csv:str) -> List[EstablecimientoGastronomico]:
    ''' Construye una lista de EstablecimientosGastronomicos con la informacion de archivo_csv'''
    e:List[EstablecimientoGastronomico] = list()
    for i in csv.DictReader(archivo_csv):
        nom:str = i['establecimiento']
        long:float = float(i['long'])
        lat:float = float(i['lat'])
        rubro:str = i['rubro']
        calle:str = i['calle']
        altura:int = int(i['altura'])
        est:EstablecimientoGastronomico = EstablecimientoGastronomico(nom, calle, altura, rubro, long, lat)
        e.append(est)
    return e
    
class TestEstablecimientoGastronomico(unittest.TestCase):
    def test_atributos_1(self):
        f:TextIO = open('establecimientos-gastronomicos5.csv', 'r', encoding = 'utf-8')
        e:List[EstablecimientoGastronomico] = cargar_establecimientos(f)
        f.close()
        self.assertEqual(e[0].nombre , '1893')
        self.assertEqual(e[1].nombre , 'AL CARBÓN')
        self.assertEqual(e[1].calle_nombre , 'RECONQUISTA')
        self.assertEqual(e[2].calle_nombre , 'DE MAYO AV.')
        self.assertEqual(e[2].calle_altura , 1201)
        self.assertEqual(e[3].calle_altura , 372)
        self.assertEqual(e[3].rubro , 'Restaurante' )
        self.assertEqual(e[4].rubro , 'Restaurante' )
        self.assertEqual(e[4].longitud, -58.411435)
        self.assertEqual(e[5].longitud, -58.484681)
        self.assertEqual(e[5].latitud, -34.576271)
        self.assertEqual(e[6].latitud, -34.571170)
        
    def test_repre(self):
        f:TextIO = open('establecimientos-gastronomicos5.csv', 'r', encoding = 'utf-8')
        e:List[EstablecimientoGastronomico] = cargar_establecimientos(f)
        f.close()
        self.assertEqual(str(e[6]), 'ANGUS@BAEZ 444')
        self.assertEqual(str(e[7]), 'ANTA HELADOS@JUSTO, JUAN B. AV. 6357')
        self.assertEqual(str(e[8]), 'ANTIGUA TASCA DE CUCHILLEROS@CALVO, CARLOS 319')
        self.assertEqual(str(e[9]), 'ASADOR CRIOLLO LA ESTANCIA@LAVALLE 941')
        
unittest.main()
