'''
Created on 2 abr. 2020

@author: Sidney

Ejercicio Aplicación con Mysql
'''

import sys
from PyQt5.QtWidgets import QApplication
from aplicacion.aplicacion import VentanaPrincipalAplicación
from PyQt5 import QtCore

#Comprobamos que se está ejecutando desde el main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    #Instalamos un traductor para que las ventanas estén, en este caso, en castellano.
    translator = QtCore.QTranslator(app)
    locale = QtCore.QLocale.system().name()
    path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    translator.load('qtbase_%s' % locale, path)
    app.installTranslator(translator)
    
    
    ui_win = VentanaPrincipalAplicación()
    
    ui_win.show()
    sys.exit(app.exec_())
#end if