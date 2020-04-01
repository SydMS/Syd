'''
Created on 31 mar. 2020

@author: Sidney

'''

import sys
from PyQt5.QtWidgets import QApplication
from Receta7.aplicacion.aplicacion_vuelo import AplicacionVuelos


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    MainWindow = AplicacionVuelos()
    
    MainWindow.show()
    
    sys.exit(app.exec_())
    
    