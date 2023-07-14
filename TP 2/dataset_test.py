import unittest
from dataset import DataSetTuristico

dataset1:DataSetTuristico = DataSetTuristico("alojamientos-turisticos1.csv", "establecimientos-gastronomicos1.csv")
dataset2:DataSetTuristico = DataSetTuristico("alojamientos-turisticos2.csv", "establecimientos-gastronomicos2.csv")
dataset3:DataSetTuristico = DataSetTuristico("alojamientos-turisticos3.csv", "establecimientos-gastronomicos3.csv")
dataset4:DataSetTuristico = DataSetTuristico('alojamientos-turisticos4.csv', 'establecimientos-gastronomicos4.csv')

class TestDataSetTuristico(unittest.TestCase):
    
    def test_init(self):
        self.assertEqual(dataset2.alojamientos_t, [dataset2.alojamientos_t[0], dataset2.alojamientos_t[1], dataset2.alojamientos_t[2], dataset2.alojamientos_t[3]])
        self.assertEqual(dataset4.alojamientos_t, [dataset4.alojamientos_t[0], dataset4.alojamientos_t[1], dataset4.alojamientos_t[2]])
        self.assertEqual(dataset1.establecimientos_g, [dataset1.establecimientos_g[0], dataset1.establecimientos_g[1], dataset1.establecimientos_g[2],dataset1.establecimientos_g[3]])
        self.assertEqual(dataset4.establecimientos_g, [dataset4.establecimientos_g[0], dataset4.establecimientos_g[1],dataset4.establecimientos_g[2]])

    def test_alojamiento(self):
        self.assertEqual(dataset2.alojamientos(), [dataset2.alojamientos_t[0], dataset2.alojamientos_t[1], dataset2.alojamientos_t[2], dataset2.alojamientos_t[3]])
        self.assertEqual(dataset4.alojamientos(), [dataset4.alojamientos_t[0], dataset4.alojamientos_t[1], dataset4.alojamientos_t[2]])

    def test_alojamiento_por_nombre(self):
        self.assertEqual(dataset4.alojamiento_por_nombre('BOLIVAR'), dataset4.alojamientos_t[0])
        self.assertEqual(dataset3.alojamiento_por_nombre('JUNCAL PALACE HOTEL'), dataset3.alojamientos_t[5])
        self.assertEqual(dataset1.alojamiento_por_nombre('NUVE'), dataset1.alojamientos_t[5])
        
    def test_tres_boliches_cercanos(self):
        self.assertEqual(dataset1.tres_boliches_cercanos(dataset1.alojamientos_t[4]), (dataset1.establecimientos_g[3], dataset1.establecimientos_g[0], dataset1.establecimientos_g[2]))
        self.assertEqual(dataset1.tres_boliches_cercanos(dataset1.alojamientos_t[10]), (dataset1.establecimientos_g[0], dataset1.establecimientos_g[2], dataset1.establecimientos_g[3]))
        
    def test_cercano_por_rubro(self):    
        self.assertEqual(dataset2.boliche_proximo_de_rubro(dataset1.alojamientos_t[2], "Restaurante"), dataset2.establecimientos_g[2])
        self.assertEqual(dataset2.boliche_proximo_de_rubro(dataset1.alojamientos_t[0], "Tanguería"), dataset2.establecimientos_g[3])
        self.assertEqual(dataset2.boliche_proximo_de_rubro(dataset1.alojamientos_t[3], "Bar Temático"), dataset2.establecimientos_g[5])
        
unittest.main()