import unittest
from clima import Interfaz
from clima import Climas
import tkinter as tk

class PruebaInterfaz(unittest.TestCase):
    
    def pruebaConstructor(self):
        """
        Prueba que el constructor de la clase Interfaz funcione correctamente.
        """
        aeropertos = Climas()
        lista = aeropertos.arregloNombres()
        raiz = tk.Tk()
        interfaz = Interfaz(raiz, lista)
        self.assertEqual(raiz, interfaz.raiz)