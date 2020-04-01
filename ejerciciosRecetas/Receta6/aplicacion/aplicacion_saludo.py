'''
Created on 1 abr. 2020

@author: Sidney

'''
from random import randint
from PyQt5.QtWidgets import QDialog
from Receta6.ventanas.ventana_saludo import Ui_DialogoSaludar

#Generamos una clase que será el dialogo de la aplicación
class AplicacionSaludo(QDialog):
    #Generamos el constructor
    def __init__(self):
        #Heredamos de QDialog
        super().__init__()
        self.ui_saludo = Ui_DialogoSaludar()
        self.ui_saludo.setupUi(self)
        
        #En caso de que se pulse el botón, llamaremos a la función
        self.ui_saludo.btn_saludar.clicked.connect(self.mostrar_saludo)
        self.show()
    #end __init__
    
    
    def mostrar_saludo(self):
        #Recojemos el nombre del usuario
        nombre = self.ui_saludo.txt_nombre.text()
        
        #Si nombre tiene un valor diferente de "" lo mostraremos
        if nombre != "":
            
            saludos = ("Bienvenido","Muy buenas","Ponte cómod@","Estás en tu casa","¡Cuánto tiempo!")
            rand_saludo = randint(0,4)  
            self.ui_saludo.lbl_mostrar_saludo.setText("{}, {}.".format(saludos[rand_saludo],nombre))        
    #end mostrar_saludo
#end AplicacionSaludo