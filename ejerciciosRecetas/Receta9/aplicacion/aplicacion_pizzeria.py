'''
Created on 1 abr. 2020

@author: Sidney

'''
from PyQt5.QtWidgets import QDialog
from Receta9.ventanas.ventana_pizzeria import Ui_ventana_pizza

#Generamos una clase para la ventana de la aplicación
class AplicacionPizzeria(QDialog):
    #Definimos una función para la ventana
    def __init__(self):
        #Y heredará
        super().__init__()

        self.ui_ventana = Ui_ventana_pizza()
        self.ui_ventana.setupUi(self)
        
        #Cuando se actúe sobre uno de los checks se llamará a la función precio_pizza
        self.ui_ventana.chk_extra_queso.stateChanged.connect(self.precio_pizza)
        self.ui_ventana.chk_extra_pepperoni.stateChanged.connect(self.precio_pizza)
        self.ui_ventana.chk_extra_champi.stateChanged.connect(self.precio_pizza)
        self.ui_ventana.chk_extra_barbacoa.stateChanged.connect(self.precio_pizza)
        
        self.show()
    #end __init__
    
    def precio_pizza(self):        
        #En esta función sumaremos el precio de los ingredientes a la base
        
        #Declaramos una variable que almacenará el precio
        self.precio = 15.0
        
        #Los siguientes if sumarán a precio en función de cuántos haya marcados
        if self.ui_ventana.chk_extra_queso.isChecked():
            self.precio += 2.5
            
        if self.ui_ventana.chk_extra_pepperoni.isChecked():
            self.precio += 2.5
            
        if self.ui_ventana.chk_extra_champi.isChecked():
            self.precio += 2.5
            
        if self.ui_ventana.chk_extra_barbacoa.isChecked():
            self.precio += 2.5

        
        #Mostramos el precio de la pizza    
        self.ui_ventana.lbl_mostrar_precio.setText("Precio de la pizza: {} €.".format(self.precio))

    #end_precio_pizza
#end AplicacionPizzeria