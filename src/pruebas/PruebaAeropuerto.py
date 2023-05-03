import unittest
import csv
from clima import Aeropuerto

class PruebaAeropuerto(unittest.TestCase):

    def pruebaConstructorAeropuerto(self):
        """
        Prueba que el constructor de la ciudad sea correcto.
        """
        ciudad = Aeropuerto('ciudad', 90.0, -10.0)
        self.assertEqual(ciudad.nombre, 'ciudad', 'Diferencia entre nombres')
        self.assertEqual(ciudad.latitud, 90.0, 'Diferencia entre latitudes')
        self.assertEqual(ciudad.altitud, -10.0, 'Diferencia entre altitudes')
