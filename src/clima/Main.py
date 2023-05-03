from Climas import Climas
from Interfaz import Interfaz
import tkinter as tk

class Main():
    def __init__(self):
        self.__aeropuertos = Climas()
        self.__lista = self.__aeropuertos.arregloNombres()
        self.__raiz = tk.Tk()
        self.__interfaz = Interfaz(self.__raiz, self.__lista)
        self.__raiz.mainloop()

if __name__ == "__main__":
    Main()
        