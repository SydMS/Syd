'''
Created on 2 abr. 2020

@author: Sidney

Ejercicio Aplicación con Mysql
'''

import sys
from PyQt5.QtWidgets import QApplication
from aplicacion.aplicacion import VentanaPrincipalAplicación

#Comprobamos que se está ejecutando desde el main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_win = VentanaPrincipalAplicación()
    
    ui_win.show()
    sys.exit(app.exec_())
#end if