'''
Created on 1 abr. 2020

@author: Sidney

https://www.youtube.com/watch?v=tlOCmdnI0Ao

'''

import sys
from PyQt5.QtWidgets import QApplication
from Receta9.aplicacion.aplicacion_pizzeria import AplicacionPizzeria


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_MainWindow = AplicacionPizzeria()
    
    ui_MainWindow.show()
    sys.exit(app.exec_())