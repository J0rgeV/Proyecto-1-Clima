import unittest
import csv
from clima import Climas
class PruebaClima(unittest.TestCase):

    def pruebaClima1(self):
        """
            Prueba que el diccionario no contenga elementos repetidos.
        """
        sinPrimeraLinea = False
        with open('dataset1.csv') as f:
            lector = csv.reader(f)
            conjunto = {}
            conjunto = set()

            for fila1 in lector:
                if sinPrimeraLinea:
                    conjunto.add(fila1[0])
                    conjunto.add(fila1[1])
                sinPrimeraLinea = True

        conjuntocopia = conjunto.copy()
        climas = Climas()
        arreglo1 = climas.arregloNombres()

        while len(arreglo1) != 0:
            if len(conjunto) == 0:
                break
            for elemento in arreglo1:
                if elemento[:3] in conjunto:
                    conjunto.discard(elemento[:3])
                    arreglo1.remove(elemento)

        self.assertEqual(len(arreglo1), 0, 'El arreglo de nombres no quedó vacío o hay elementos repetidos')

        arreglo2 = climas.arregloAeropuertos()
        while len(arreglo2) != 0:
            if len(conjuntocopia) == 0:
                break
            for elemento in arreglo2:
                if elemento.nombre in conjuntocopia:
                    conjuntocopia.discard(elemento)
                    arreglo2.remove(elemento)


        self.assertEqual(len(arreglo2), 0, 'El arreglo de objetos de tipo Aeropuerto no quedó vacío o hay elementos repetidos')

    def testBuscaAeropuerto(self):
        """
            Prueba que la función de buscaAeropuerto() no devuelva algo al pasarle como
            parámetro un aeropuerto que no está dentro del diccionario.
        """
        climas = Climas()
        resultado = climas.buscaAeropuerto('...')
        self.assertEqual(resultado, None)
