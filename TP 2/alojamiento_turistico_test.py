import unittest
from typing import List, TextIO
import csv

from alojamiento_turistico import AlojamientoTuristico

def cargar_alojamientos(archivo_csv:str) -> List[AlojamientoTuristico]:
    lista:List[AlojamientoTuristico] = []
    for i in csv.DictReader(archivo_csv):
        if i['Lat'] != '' and i['Lat'] != ' ' and i['Long'] != '' and i['Long'] != ' ':
            nombre:str = i["nombre"]
            calle:str = i["calle"]
            altura:int = int(i["altura"])
            latitud:float = float(i["Lat"])
            longitud:float = float(i["Long"])
            telefono:str = i["telefono"]
            email: str = i["email"]
        obj: AlojamientoTuristico = AlojamientoTuristico(nombre, latitud, longitud, calle, altura, telefono, email)
        lista.append(obj)
    return lista

class TestAlojamientoTuristico(unittest.TestCase):

    def test_atributos(self):
        file:TextIO = open("alojamientos-turisticos1.csv", 'r', encoding = "utf-8")
        lista:List[AlojamientoTuristico] = cargar_alojamientos(file)
        file.close()
        self.assertEqual(lista[0].nombre, "BOLIVAR")
        self.assertEqual(lista[4].nombre, 'HOTEL 26 DE JULIO')
        self.assertEqual(lista[0].latitud, -34.618212)
        self.assertEqual(lista[4].latitud, -34.621526)
        self.assertEqual(lista[0].longitud, -58.373013)
        self.assertEqual(lista[3].longitud, -58.383766)
        self.assertEqual(lista[1].calle_nombre, "PERU")
        self.assertEqual(lista[3].calle_nombre, 'AV. BELGRANO ')
        self.assertEqual(lista[1].calle_altura, 1022)
        self.assertEqual(lista[5].calle_altura, 1241)
        self.assertEqual(lista[2].telefono, "4943-0031")
        self.assertEqual(lista[5].telefono, '4943-0053')
        self.assertEqual(lista[10].telefono, 'N/D')
        self.assertEqual(lista[2].email, 'ventas@hotel-splendid.com.ar')
        self.assertEqual(lista[5].email, 'hotelesfattsa@sanidad.org.ar')
        self.assertEqual(lista[9].email, 'N/D')

    def test_contacto(self):
        file:TextIO = open("alojamientos-turisticos1.csv", 'r', encoding = "utf-8")
        lista:List[AlojamientoTuristico] = cargar_alojamientos(file)
        file.close()
        self.assertEqual(lista[0].contacto(), "4361 5105 | reservas@hotel-bolivar.com.ar")
        self.assertEqual(lista[1].contacto(), "4307-9593 | info@paradorbue.com")
        self.assertEqual(lista[2].contacto(), "4943-0031 | ventas@hotel-splendid.com.ar")
        self.assertEqual(lista[3].contacto(), "4383-8414 | info@lacasadelmedico.com.ar")
        self.assertEqual(lista[6].contacto(), '4902-5983 | obrasocial@aomaosam.org.ar')
        self.assertEqual(lista[10].contacto(), 'N/D')
        self.assertEqual(lista[9].contacto(), '4381-8691')
        self.assertEqual(lista[11].contacto(), 'nuveenvios@gmail.com')
        
    def test_distancia(self):
        file:TextIO = open("alojamientos-turisticos1.csv", 'r', encoding = "utf-8")
        lista:List[AlojamientoTuristico] = cargar_alojamientos(file)
        file.close()
        self.assertEqual(lista[0].distancia(-34.619917, -58.374235), 220.10841365697047)
        self.assertEqual(lista[1].distancia(-34.619917, -58.374235), 0.0)
        self.assertEqual(lista[10].distancia(-34.610676, -58.390339), 0.0)
        self.assertEqual(lista[3].distancia(-34.608270, -58.396890), 1319.657130915268)

    def test_repr(self):
        file:TextIO = open("alojamientos-turisticos1.csv", 'r', encoding = "utf-8")
        lista:List[AlojamientoTuristico] = cargar_alojamientos(file)
        file.close()
        self.assertEqual(str(lista[0]), "ALOJAMIENTO:BOLIVAR")
        self.assertEqual(str(lista[1]), "ALOJAMIENTO:SANTA MARIA DE LA SALUD")
        self.assertEqual(str(lista[2]), "ALOJAMIENTO:SPLENDID")
        self.assertEqual(str(lista[3]), "ALOJAMIENTO:LA CASA DEL MÉDICO")
        self.assertEqual(str(lista[5]), 'ALOJAMIENTO:OBRA SOCIAL DEL PERSONAL DE LA SANIDAD ARGENTINA')
        self.assertEqual(str(lista[6]), 'ALOJAMIENTO:OBRA SOCIAL DE LA ACTIVIDAD MINERA OSAM')
        self.assertEqual(str(lista[9]), 'ALOJAMIENTO:PETIT HOTEL SANTA ISABEL')

unittest.main() 