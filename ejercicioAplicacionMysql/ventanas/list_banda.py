'''
Created on 2 abr. 2020

@author: Sidney

Listado de bandas de la bd

'''

from PyQt5 import QtCore, QtWidgets
from bd.operaciones import Listar_Bandas


class Ventana_Listar_Banda(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(647, 415)
        MainWindow.setStyleSheet("QHeaderView::section{background-color:black;}")
        #Almacenamos el listado de bandas en una tupla
        self.listado_bandas = Listar_Bandas()
        self.principal_widget = QtWidgets.QWidget(MainWindow)
        self.principal_widget.setObjectName("principal_widget")
        self.gph_background = QtWidgets.QGraphicsView(self.principal_widget)
        self.gph_background.setGeometry(QtCore.QRect(-10, -20, 671, 431))
        self.gph_background.setStyleSheet("background-image: url(\'images/ini_background.jpg\');background-repeat: no-repeat; background-position: center;")
        self.gph_background.setObjectName("gph_background")
        self.tbl_listado_artistas = QtWidgets.QTableWidget(self.principal_widget)
        self.tbl_listado_artistas.setGeometry(QtCore.QRect(10, 20, 481, 341))
        self.tbl_listado_artistas.setObjectName("tbl_listado_artistas")
        self.tbl_listado_artistas.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                                "color:white;"
                                                "border: 2px solid black;\n"
                                                "border-radius:5px;")
        self.tbl_listado_artistas.setColumnCount(2)
        self.tbl_listado_artistas.setColumnWidth(0,250)
        self.tbl_listado_artistas.setColumnWidth(1,202)
        self.tbl_listado_artistas.setRowCount(len(self.listado_bandas))
        #Generamos tantas cabeceras para las filas como resultados tengamos.
        for i in range(0,len(self.listado_bandas)):
            item = QtWidgets.QTableWidgetItem()
            self.tbl_listado_artistas.setVerticalHeaderItem(i, item)
        #end for
        item = QtWidgets.QTableWidgetItem()
        self.tbl_listado_artistas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_listado_artistas.setHorizontalHeaderItem(1, item)
        #Creamos dos bucles para crear las celdas en la tabla
        #El primer bucle genera la fila
        for i in range(0,len(self.listado_bandas)):
            #El segundo bucle se encarga de las columnas
            for j in range(2):
                item = QtWidgets.QTableWidgetItem()
                self.tbl_listado_artistas.setItem(i, j, item)
            #end for
        #end for
        self.btn_modificar_banda = QtWidgets.QPushButton(self.principal_widget)
        self.btn_modificar_banda.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.btn_eliminar_banda = QtWidgets.QPushButton(self.principal_widget)
        self.btn_eliminar_banda.setGeometry(QtCore.QRect(0, 0, 0, 0))
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
        item = self.tbl_listado_artistas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Artista"))
        item = self.tbl_listado_artistas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nacionalidad"))
        __sortingEnabled = self.tbl_listado_artistas.isSortingEnabled()
        self.tbl_listado_artistas.setSortingEnabled(False)
        #Generamos las líneas necesarias en función de la longitud del listado
        i = 0
        for banda in self.listado_bandas:
            item = self.tbl_listado_artistas.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", ""))
            for j in range(0,2):
                item = self.tbl_listado_artistas.item(i, j)
                item.setText(_translate("MainWindow", banda[j]))
            #end for   
            i += 1
        #end for
        self.tbl_listado_artistas.setSortingEnabled(__sortingEnabled)
        self.actionIncluir_artista_banda.setText(_translate("MainWindow", "Incluir artista/banda"))
        self.actionIncluir_disco.setText(_translate("MainWindow", "Incluir disco"))
        self.actionIncluir_genero.setText(_translate("MainWindow", "Incluir género"))
        self.actionListar_artistas_bandas.setText(_translate("MainWindow", "Listar artistas/bandas"))
        self.actionListar_discos.setText(_translate("MainWindow", "Listar discos"))
        self.actionListar_generos.setText(_translate("MainWindow", "Listar géneros"))
    #end restranslateUi
    
    def modificar_eliminar(self):
        _translate = QtCore.QCoreApplication.translate
        self.btn_modificar_banda.setGeometry(QtCore.QRect(520, 290, 101, 31))
        self.btn_modificar_banda.setObjectName("btn_modificar_banda")
        self.btn_modificar_banda.setStyleSheet("border: 2px solid black;"
                                                "border-radius:5px;"
                                                "background: rgb(255,255,255);"
                                                "color:black;"
                                                "font: 13px")            
        self.btn_eliminar_banda.setGeometry(QtCore.QRect(520, 330, 101, 31))
        self.btn_eliminar_banda.setObjectName("btn_eliminar_banda")
        self.btn_eliminar_banda.setStyleSheet("border: 2px solid black;"
                                            "border-radius:5px;"
                                            "background: rgb(255,255,255);"
                                            "color:black;"
                                            "font: 13px")
        self.btn_modificar_banda.setText(_translate("MainWindow", "Modificar"))
        self.btn_eliminar_banda.setText(_translate("MainWindow", "Eliminar"))
    #end modificar_eliminar
#end Ventana_Listar_Banda