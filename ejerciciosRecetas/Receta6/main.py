'''
Created on 31 mar. 2020

@author: Sidney

'''
import sys
from PyQt5.QtWidgets import QApplication
from Receta6.aplicacion.aplicacion_saludo import AplicacionSaludo


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ui_ventana = AplicacionSaludo() 
    
   
    ui_ventana.show()
    sys.exit(app.exec_()) 
    
    