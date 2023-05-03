import json
import os
import requests
from datetime import datetime
class Peticion:

    def __init__(self, lat:float, lon:float, AeropuertoNombre):
        """Método que hace la petición a OpenWheather

            alt = float -la altitud del aeropuerto a la que queremos solicitar el clima

            lon = float -la longitud de la ciudad a la que queremos solicitar el clima

            aeropuertoNombre = string - el aeropuerto correspondiente a las coordenadas dadas

        """
        self.__lat = lat
        self.__lon = lon
        self.cantidadPeticiones = 0
        try:
            llave = self.__leeLlave()
            diccionarioClimaCiudad = self.__solicitaInfo(llave)
            ruta = "../caché/peticiones/"+AeropuertoNombre+".json"
            existeArchivo = os.path.isfile(ruta)
            if(existeArchivo):
                with open(ruta) as file:
                    info = json.load(file)
                    if(self.__necesitaActualizarse(info)):
                        self.__escribeFechaActual(diccionarioClimaCiudad)
                        self.__creaArchivo(diccionarioClimaCiudad, ruta)
            else:
                self.__escribeFechaActual(diccionarioClimaCiudad)
                self.__creaArchivo(diccionarioClimaCiudad, ruta)
        except Exception as e:
            print("solicitud rechazada")

    def __solicitaInfo(self, llave):
        """Funcion para solicitar la informacion de la ciudad a OpenWheather

           llave = string - la llave para hacer la peticion a OpenWheather

           Devuelve un diccionario con la informacion de la ciudad
        """ 
        url = 'https://api.openweathermap.org/data/2.5/weather?lat='+str(self.__lat)+'&lon='+str(self.__lon)+'&units=metric&lang=es&appid='+llave
        respuesta = requests.get(url)
        diccionarioCiudad = respuesta.json()
        return diccionarioCiudad

    def __leeLlave(self):
        """Funcion para leer la llave

            Devuelve un string con la llave
        """
        rutaLlave= open("../datos/key.txt", mode='r')
        llave=rutaLlave.read()
        rutaLlave.close()
        return llave

    def __escribeFechaActual(self, diccionarioCiudad):
        """Funcion para escribir la fecha actual en el archivo

            diccionarioCiudad = diccionario - el diccionario con la informacion de la ciudad
        """
        fecha = datetime.now()
        diccionarioCiudad["ano"] = fecha.year
        diccionarioCiudad["mes"] = fecha.month                    
        diccionarioCiudad["dia"] =fecha.day
        diccionarioCiudad["hora"] =fecha.hour
        diccionarioCiudad["minuto"] =fecha.minute

    def __creaArchivo(self,diccionarioAeropuerto,ruta):
        """Funcion para crear archivo

            diccionarioCiudad = diccionario - el diccionario con la informacion de la ciudad

            ruta = string - la ruta donde se va a crear el archivo
        """
        if(self.cantidadPeticiones >3000):
            print("Máximo de solicitudes alcanzado")
            return
        self.cantidadPeticiones= self.cantidadPeticiones+1
        with open(ruta, "w") as i:
                    json.dump(diccionarioAeropuerto,i, indent=2)

    def __necesitaActualizarse(self, fechas:dict):
        """
        Método auxiliar que indica cuando es necesario
        actualizar el archivo en el caché.

        fechas = dict - diccionario con las fechas de la última actualización,

        en el formato {"ano":int, "mes":int, "dia":int, "hora":int, "minuto":int}

        Devuelve True si es necesario actualizar el archivo, False en caso contrario.
        """
        actual = datetime.now()
        año = actual.year
        mes = actual.month
        dia = actual.day
        hora = actual.hour
        minuto = actual.minute
        if(año != fechas["ano"]):
            return True
        if(mes != fechas["mes"]):
            return True
        if(dia != fechas["dia"]):
            return True
        if(hora != fechas["hora"]):
            return True
        if(minuto > fechas["minuto"]+5):
            return True
        return False  
      
