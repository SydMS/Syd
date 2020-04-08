'''
Created on 2 abr. 2020

@author: Sidney

Listado de géneros músicales de la bd

'''

from PyQt5 import QtCore, QtWidgets
from bd.operaciones import Listar_Generos


class Ventana_Listar_Generos(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(647, 415)
        MainWindow.setStyleSheet("")
        self.listado_generos = Listar_Generos()
        self.principal_widget = QtWidgets.QWidget(MainWindow)
        self.principal_widget.setObjectName("principal_widget")
        self.gph_background = QtWidgets.QGraphicsView(self.principal_widget)
        self.gph_background.setGeometry(QtCore.QRect(-10, -20, 671, 431))
        self.gph_background.setStyleSheet("background-image: url(\'images/ini_background.jpg\');background-repeat: no-repeat; background-position: center;")
        self.gph_background.setObjectName("gph_background")
        self.lst_listar_genero = QtWidgets.QListWidget(self.principal_widget)
        self.lst_listar_genero.setGeometry(QtCore.QRect(40, 20, 551, 331))
        self.lst_listar_genero.setObjectName("lst_listar_genero")
        self.lst_listar_genero.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                             "color:white;")
        #Creamos un bucle para generar los items según haya en la bd
        i = 0
        while i <= (len(self.listado_generos)-1):
            item = QtWidgets.QListWidgetItem()
            self.lst_listar_genero.addItem(item)
            i += 1
        #end while
        MainWindow.setCentralWidget(self.principal_widget)
        self.actionIncluir_artista_banda = QtWidgets.QAction(MainWindow)
        self.actionIncluir_artista_banda.setObjectName("actionIncluir_artista_banda")
        self.actionIncluir_disco = QtWidgets.QAction(MainWindow)
        self.actionIncluir_disco.setObjectName("actionIncluir_disco")
        self.actionIncluir_genero = QtWidgets.QAction(MainWindow)
        self.actionIncluir_genero.setObjectName("actionIncluir_genero")
        self.actionListar_artistas_bandas = QtWidgets.QAction(MainWindow)
        self.actionListar_artistas_bandas.setObjectName("actionListar_artistas_bandas")
        self.actionListar_discos = QtWidgets.QAction(MainWindow)
        self.actionListar_discos.setObjectName("actionListar_discos")
        self.actionListar_generos = QtWidgets.QAction(MainWindow)
        self.actionListar_generos.setObjectName("actionListar_generos")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #end setupUi
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Directorio musical"))
        __sortingEnabled = self.lst_listar_genero.isSortingEnabled()
        self.lst_listar_genero.setSortingEnabled(False)
        
        indice = 0
        #Creamos un bucle para generar los items según haya en la bd
        for l in self.listado_generos:            
            item = self.lst_listar_genero.item(indice)
            item.setText(_translate("MainWindow", l[0]))
            indice += 1
        #end for
        self.lst_listar_genero.setSortingEnabled(__sortingEnabled)
        self.actionIncluir_artista_banda.setText(_translate("MainWindow", "Incluir artista/banda"))
        self.actionIncluir_disco.setText(_translate("MainWindow", "Incluir disco"))
        self.actionIncluir_genero.setText(_translate("MainWindow", "Incluir género"))
        self.actionListar_artistas_bandas.setText(_translate("MainWindow", "Listar artistas/bandas"))
        self.actionListar_discos.setText(_translate("MainWindow", "Listar discos"))
        self.actionListar_generos.setText(_translate("MainWindow", "Listar géneros"))
    #end retranslateUi
#end Ventana_Listar_Generos