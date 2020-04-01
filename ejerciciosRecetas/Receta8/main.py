'''
Created on 1 abr. 2020

@author: Sidney

https://www.youtube.com/watch?v=JTR8BDa2Vb4

'''

import sys
from PyQt5.QtWidgets import QApplication
from Receta8.aplicacion.aplicacion_venta import VentanaCamisas

if __name__ == "__main__":
        
    app = QApplication(sys.argv)
    MainWindow = VentanaCamisas()
    
    MainWindow.show()
    sys.exit(app.exec_())
    