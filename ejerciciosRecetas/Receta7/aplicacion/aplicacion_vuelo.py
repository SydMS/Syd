'''
Created on 1 abr. 2020

@author: Sidney


'''
from PyQt5.QtWidgets import QDialog
from Receta7.ventanas.ventana_vuelo import Ui_ventana_vuelo

#Generamos una clase que contendrá los elementos de la ventana
class AplicacionVuelos(QDialog):
    #Definimos el constructor
    def __init__(self):
        #Hacemos que herede de QDialog
        super().__init__()
        self.ui_vuelos = Ui_ventana_vuelo()
        self.ui_vuelos.setupUi(self)
        
        #En caso de que cambie el estado de estos botones se ejecutará 
        #la función mostrar_info
        
        self.ui_vuelos.rad_first.toggled.connect(self.mostrar_info)
        self.ui_vuelos.rad_business.toggled.connect(self.mostrar_info)
        self.ui_vuelos.rad_economic.toggled.connect(self.mostrar_info)
        
        self.show()
    #end __init__
        
    def mostrar_info(self):
        #Definimos la variable que almacenará el valor
        precio_billete = 0

        #Dependiendo del botón seleccionado se guardará su valor en la variable
        if self.ui_vuelos.rad_first.isChecked():
            precio_billete = 220
        elif self.ui_vuelos.rad_business.isChecked():
            precio_billete = 150
        elif self.ui_vuelos.rad_economic.isChecked():
            precio_billete = 80
        
        #Mostramos en pantalla la selección
        self.ui_vuelos.lbl_motrar_seleccion.setText("La opción seleccionada tiene un precio de {} €.".format(precio_billete))
    #end mostrar_info
#end_AplicacionVuelos