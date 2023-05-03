import csv
import Aeropuerto
from LectorIATA import LectorIATA

class Climas ():

    def __init__(self):
        """
            Clase Climas para crear un diccionario de aeropuertos leídos en un
            archivo .csv teniendo como formato columnas de IATA, coordenada latitud
            y coordenada altitud.
        """
        aeropuertos = {
            "nombres": [],
            "coordenadas": []
        }
        self.aeropuertos = aeropuertos
        sinPrimeraLinea = False
        archivo = '../datos/dataset1.csv'
        self.archivo = archivo
        self.sinPrimeraLinea = sinPrimeraLinea
        conjunto = {}
        conjunto = set()
        conjunto = self.conjuntoNombres()

        with open(archivo) as f:
            lectorcsv = csv.reader(f)
            for fila in lectorcsv:
                if self.sinPrimeraLinea:
                    if fila[0] in conjunto:
                        lector = LectorIATA(fila[0])
                        nombreAeropuerto = lector.devuelveNombre()
                        if nombreAeropuerto != None:
                            aeropuertos["nombres"].append(fila[0] + ' (' + nombreAeropuerto + ')')
                        else:
                            aeropuertos["nombres"].append(fila[0])
                        aeropuertos["coordenadas"].append(Aeropuerto.Aeropuerto(fila[0], fila[2], fila[3]))
                        conjunto.discard(fila[0])
                    if fila[1] in conjunto:

                        lector = LectorIATA(fila[1])
                        nombreAeropuerto = lector.devuelveNombre()
                        if nombreAeropuerto != None:
                            aeropuertos["nombres"].append(fila[1] + ' (' + nombreAeropuerto + ')')
                        else:
                            aeropuertos["nombres"].append(fila[1])
                        aeropuertos["coordenadas"].append(Aeropuerto.Aeropuerto(fila[1], fila[4], fila[5]))
                        conjunto.discard(fila[1])

                self.sinPrimeraLinea = True

    def conjuntoNombres(self):
        """
            Realiza el almacenamiento de las IATA's de los aeropuertos para devolver
            un conjunto y evitar repeticiones de IATA's.
        """
        archivoLect = open(self.archivo)
        lectorcsv = csv.reader(archivoLect)
        conjunto = {}
        conjunto = set()

        for fila in lectorcsv:
            if self.sinPrimeraLinea:
                conjunto.add(fila[0])
                conjunto.add(fila[1])
            self.sinPrimeraLinea = True

        self.sinPrimeraLinea = False

        return conjunto

    def arregloNombres(self):
        """
            Devuelve un arreglo con los nombres de los aeropuertos.
        """
        return self.aeropuertos["nombres"]

    def arregloAeropuertos(self):
        """
            Devuelve un arreglo con los objetos de tipo Aeropuerto.
        """
        return self.aeropuertos["coordenadas"]

    def buscaAeropuerto(self,aeropuerto):
        """
            Función que se encarga de realizar la búsqueda en el arreglo de objetos
            de tipo Aeropuerto con base en el nombre o IATA pasado como parámetro.
        """
        for i in range(1, len(self.arregloAeropuertos())):
            if aeropuerto == self.arregloNombres()[i]:
                return self.arregloAeropuertos()[i]
