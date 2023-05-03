import unittest
from clima import LectorIATA

class PruebaLectorIATA(unittest.TestCase):
    def pruebaDevuelveNombre(self):
        """
        Prueba que el método devuelveNombre(self) funcione correctamente.
        """
        lector = LectorIATA("MEX")
        self.assertEqual(lector.devuelveNombre(), "Licenciado Benito Juarez International Airport, MX")

    def pruebaNone(self):
        """
        Prueba que el método devuelveNombre(self) devuelva None si no se encuentra el aeropuerto.
        """
        lector = LectorIATA("XXX")
        self.assertEqual(lector.devuelveNombre(), None)
    