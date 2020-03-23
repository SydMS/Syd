'''
Calculadora con Tkinter
'''

from tkinter import Tk
from interface import Interfaz
 
 
ventana_calculadora = Tk()
calculadora = Interfaz(ventana_calculadora)
ventana_calculadora.mainloop()