import unittest
from alojamiento_turistico import AlojamientoTuristico
from armar_lista import cargar_establecimientos
from typing import List, Dict, TextIO
from dataset import DataSetTuristico

####################################################################

file1: TextIO = open("alojamientos-turisticos-propios.csv", encoding = "utf-8")
lista_test: List[AlojamientoTuristico] = cargar_establecimientos(file1)
file1.close()

file2: TextIO = open("alojamientos_tino.csv", encoding = "utf-8")
lista_test2: List[AlojamientoTuristico] = cargar_establecimientos(file2)
file2.close()

file3: TextIO = open("abc.csv", encoding = "utf-8")
lista_test_3: List[AlojamientoTuristico] = cargar_establecimientos(file3)
file3.close()

dataset1: DataSetTuristico = DataSetTuristico("alojamientos-turisticos-propios.csv", "establecimientos_gastronomicos_propios.csv")
dataset2: DataSetTuristico = DataSetTuristico("alojamientos_tino.csv", "gastronomicos_tino.csv")
dataset3: DataSetTuristico = DataSetTuristico("abc.csv", "def.csv")

class TestDataSetTuristico(unittest.TestCase):

    def test_lista_de_alojamientos(self):
        self.assertEqual(dataset1.alojamientos, lista_test)
        self.assertEqual(dataset2.alojamientos, lista_test2)
        self.assertEqual(dataset3.alojamientos, lista_test_3)

    def test_alojamiento(self):
        self.assertEqual(dataset1.alojamiento_por_nombre("SANTA MARIA DE LA SALUD"), "ALOJAMIENTO:SANTA MARIA DE LA SALUD")
        self.assertEqual(dataset2.alojamiento_por_nombre("HOSTAL EL CANDIL"), "ALOJAMIENTO:HOSTAL EL CANDIL")
        self.assertEqual(dataset3.alojamiento_por_nombre("RESIDENCIA GODOY CRUZ"), "ALOJAMIENTO:RESIDENCIA GODOY CRUZ")

    def test_boliche_proximo_de_rubro(self):
        self.assertEqual(dataset1.boliche_proximo_de_rubro(dataset1.alojamientos_t[0], "Restaurante"), "ANTIGUA TASCA DE CUCHILLEROS@CALVO, CARLOS 319")
        self.assertEqual(dataset1.boliche_proximo_de_rubro(dataset1.alojamientos_t[0], "Heladería"), "ANTA HELADOS@JUSTO, JUAN B. AV. 6357")
        self.assertEqual(dataset2.boliche_proximo_de_rubro(dataset2.alojamientos_t[1], "Restaurante"), "")
        self.assertEqual(dataset2.boliche_proximo_de_rubro(dataset2.alojamientos_t[1], "Bar Notable"))
        

## y así con el resto de los métodos a testear.
        
####################################################################

unittest.main()
