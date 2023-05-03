import json

class LectorIATA():

    def __init__(self, iata):
        """
            Clase para obtener el nombre del aeropuerto dada su clave IATA.
            iata = String - El código IATA del aeropuerto.
        """
        ruta = "../datos/IATACodes.json"

        with open(ruta) as file:
            archivoIATA = json.load(file)
            try:
                aeropuertoDatos = archivoIATA[iata]
                if aeropuertoDatos["name"] != None:
                    self.__info = str(aeropuertoDatos["name"]) +", " + str(aeropuertoDatos["iso"])
                else:
                    self.__info = None
            except KeyError:
                self.__info = None        

    def devuelveNombre(self):
        """
            Devuelve el nombre del aeropuerto o 'None' si no se cuenta con su nombre.
        """
        return self.__info
