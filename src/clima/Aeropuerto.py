class Aeropuerto():

    def __init__(self, nombre, latitud, altitud):
        """
            Clase para obtener un objeto de tipo Aeropuerto con su nombre o clave
            IATA y sus coordenadas.

            nombre = string - El código IATA del aeropuerto.

            latitud = float - La coordenada latitud del aeropuerto.

            altitud = float - La coordenada altitud del aeropuerto.
        """
        self.nombre = nombre
        self.latitud = latitud
        self.altitud = altitud
