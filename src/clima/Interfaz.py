import json
from functools import partial
from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from Peticion import Peticion
from Climas import Climas


class Interfaz(ttk.Frame):

    def __init__(self, raiz, lista):
        """Metodo para construir la interfaz.

        raiz = tt.Tk() - la ventana principal

        lista = list - una lista de paises.

        """
        try:
            super().__init__(raiz)
            self.__lista = lista
            self.__configuraRaiz(raiz)
            self.__cuadro=Frame(width=650, height= 500,bd=10,relief="groove",bg="light blue")
            self.__cuadro.pack()
            self.__creaSeleccioneCiudad()
            self.__desplegable = self.__creaDesplegable()
        except TypeError:
            print("raiz no es un tt.Tk() o lista no es una lista")

    def __configuraRaiz(self, raiz):
        """Configura la raiz de la interfaz.

          raiz = tt.Tk() - la ventana principal
        """
        raiz.title("Clima")
        raiz.resizable(False,False)
        raiz.geometry("700x500")
        raiz.config(bg="light blue")

    def __creaSeleccioneCiudad(self):
        """
        Crea un Label con el texto "Seleccione una ciudad"
        """

        seleccioneCiudadLabel=Label(self.__cuadro, text='Seleccione la ciudad para consultar su clima:',
                         justify="center",bg="light blue", fg='blue', font=("C059", 18))
        seleccioneCiudadLabel.place(x=15, y=5)
    
    def __creaDesplegable(self):
        """
        Crea un desplegable con las ciudades de la lista.
        """
        desplegable = ttk.Combobox(state="readonly", values=self.__lista)
        desplegable.bind("<<ComboboxSelected>>",self.__muestraEscogido)
        desplegable.place(x=50,y=70)
        return desplegable


    def __muestraEscogido(self,event):
            """
            Muestra el elemento escogido en una ventanita, además, crea un botón. 
            """
            escogido = self.__desplegable.get()
            climas =Climas()
            ciudad = climas.buscaAeropuerto(escogido)
            boton = ttk.Button(text="mostrar clima", command=partial(self.__muestraClima,
                                         self, ciudad.latitud,ciudad.altitud, escogido))
            boton.place(x=280,y=65)
            messagebox.showinfo(title="Selección",message="Ha seleccionado: "+escogido)

    def __muestraClima(self,event, lat:float,lon:float, nombre):
        """
        Despliega un label con el clima del aeropuerto solicitado
        """
        try:
            solicitud = Peticion(lat,lon,nombre)
            ruta = "../caché/peticiones/"+nombre+".json"
            with open(ruta, 'r') as j:
                info = json.load(j)
                climainfo = info['weather']
                descripcion = climainfo[0]["description"] 
                climaLabel = Label(self.__cuadro,
                     text="Temperatura:  "+ str(info['main']['temp'])+ " °C"
                     +"\n"+"Máxima de  "+ str(info["main"]["temp_max"])+ " °C"
                     +"\n"+"Mínima de  " + str(info["main"]["temp_min"])+ " °C"
                     +"\n"+ descripcion+ "\n"+ "Percepción térmica: "
                     + str(info["main"]["feels_like"])+ " °C",
                     justify= "center",bg="light blue" ,
                     fg="black", font=("C059",18))
                climaLabel.place(x=160,y=140)      
        except FileNotFoundError:
             print("Archivo json no encontrado")

