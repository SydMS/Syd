'''
Created on 2 abr. 2020

@author: Sidney

Listado de discos de la bd

'''

from PyQt5 import QtCore, QtWidgets
from bd.operaciones import Listar_Bandas, Obtener_ID_Banda, Listar_Discos
from _datetime import datetime


class Ventana_Listar_Discos(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(647, 415)
        MainWindow.setStyleSheet("QHeaderView::section{background-color:black;}")
        #Creamos listado_bandas para recoger la tupla con todas las bandas de la bd
        self.listado_bandas = Listar_Bandas()
        self.principal_widget = QtWidgets.QWidget(MainWindow)
        self.principal_widget.setObjectName("principal_widget")
        self.gph_background = QtWidgets.QGraphicsView(self.principal_widget)
        self.gph_background.setGeometry(QtCore.QRect(-10, -20, 671, 431))
        self.gph_background.setStyleSheet("background-image: url(\'images/ini_background.jpg\');background-repeat: no-repeat; background-position: center;")
        self.gph_background.setObjectName("gph_background")
        self.combo_list_banda_album = QtWidgets.QComboBox(self.principal_widget)
        self.combo_list_banda_album.setGeometry(QtCore.QRect(30, 20, 151, 22))
        self.combo_list_banda_album.setObjectName("combo_list_banda_album")
        self.combo_list_banda_album.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                                  "color:white;"
                                                  "border: 2px solid black;\n"
                                                  "border-radius:5px;")
        i = 0
        #Creamos tantos items como elementos haya en listado_bandas
        while i <= (len(self.listado_bandas)-1):
            self.combo_list_banda_album.addItem("")
            i += 1
        #end while
        self.tbl_listado_album = QtWidgets.QTableWidget(self.principal_widget)
        self.tbl_listado_album.setGeometry(QtCore.QRect(190, 20, 431, 341))
        self.tbl_listado_album.setObjectName("tbl_listado_album")
        self.tbl_listado_album.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                              "color:white;"
                                              "border: 2px solid black;\n"
                                              "border-radius:5px;")
        self.tbl_listado_album.setColumnCount(4)
        self.tbl_listado_album.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_listado_album.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_listado_album.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_listado_album.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_listado_album.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_listado_album.setVerticalHeaderItem(0, item)
        MainWindow.setCentralWidget(self.principal_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 21))
        self.menubar.setObjectName("menubar")
        self.menuDirectorio_musical = QtWidgets.QMenu(self.menubar)
        self.menuDirectorio_musical.setObjectName("menuDirectorio_musical")
        self.menuListados = QtWidgets.QMenu(self.menubar)
        self.menuListados.setObjectName("menuListados")
        MainWindow.setMenuBar(self.menubar)
        self.barra_estado = QtWidgets.QStatusBar(MainWindow)
        self.barra_estado.setObjectName("barra_estado")
        MainWindow.setStatusBar(self.barra_estado)
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
        self.menuDirectorio_musical.addAction(self.actionIncluir_artista_banda)
        self.menuDirectorio_musical.addAction(self.actionIncluir_disco)
        self.menuDirectorio_musical.addAction(self.actionIncluir_genero)
        self.menuListados.addAction(self.actionListar_artistas_bandas)
        self.menuListados.addAction(self.actionListar_discos)
        self.menuListados.addAction(self.actionListar_generos)
        self.menubar.addAction(self.menuDirectorio_musical.menuAction())
        self.menubar.addAction(self.menuListados.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #end setupUi
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Directorio musical"))
        indice = 0
        #Generamos el combo con los nombre de las bandas
        for l in self.listado_bandas:        
            self.combo_list_banda_album.setItemText(indice, _translate("MainWindow", l[0]))
            indice += 1
        #end for
        
        item = self.tbl_listado_album.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", ""))
        item = self.tbl_listado_album.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Álbum"))
        item = self.tbl_listado_album.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Num. Pistas"))
        item = self.tbl_listado_album.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Año"))
        item = self.tbl_listado_album.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Género"))
        __sortingEnabled = self.tbl_listado_album.isSortingEnabled()
        self.tbl_listado_album.setSortingEnabled(False)
        self.tbl_listado_album.setSortingEnabled(__sortingEnabled)
        self.menuDirectorio_musical.setTitle(_translate("MainWindow", "Directorio musical"))
        self.menuListados.setTitle(_translate("MainWindow", "Listados"))
        self.actionIncluir_artista_banda.setText(_translate("MainWindow", "Incluir artista/banda"))
        self.actionIncluir_disco.setText(_translate("MainWindow", "Incluir disco"))
        self.actionIncluir_genero.setText(_translate("MainWindow", "Incluir género"))
        self.actionListar_artistas_bandas.setText(_translate("MainWindow", "Listar artistas/bandas"))
        self.actionListar_discos.setText(_translate("MainWindow", "Listar discos"))
        self.actionListar_generos.setText(_translate("MainWindow", "Listar géneros"))
    #end retranslateUi  
    def mostrar_discos(self):
        _translate = QtCore.QCoreApplication.translate
        #Cargamos en la variable nom_banda la selección del usuario
        nom_banda = self.combo_list_banda_album.currentText()
        #Obtenemos, a través de una consulta, el ID de la banda
        id_banda = Obtener_ID_Banda(nom_banda)
        #discos será una tupla que contendrá el listado completo de discos
        #con ID id_banda
        discos = Listar_Discos(id_banda)
        #Generamos tantas filas discos tenga el grupo
        self.tbl_listado_album.setRowCount(len(discos))
        #Declaramos las variables i y j que será las posiciones de las celdas        
        i = 0
        j = 0
        #En este primer bucle separamos cada disco del grupo
        for tupla in discos:
            #Creamos una cabecera para la fila por cada disco
            item = QtWidgets.QTableWidgetItem()
            self.tbl_listado_album.setVerticalHeaderItem(i, item)
            #Creamos una lista...
            lista_valor = []
            #...que contendrá los valores de la tupla para poder manipularlos
            lista_valor = list(tupla)            
            #El índice 1 es un integer, así que lo transformamos en string
            lista_valor[1] = str(lista_valor[1])
            #El índice 2 es una fecha, se transforma a string y le damos formato
            lista_valor[2] = datetime.strftime(lista_valor[2],'%d/%m/%Y')
            #En este segundo bucle se tratará cada elemento de la lista
            for valor in lista_valor:
                #Creamos un Item por cada elemento siendo i la fila, j la columna
                #y valor elemento que se mostrará
                item = QtWidgets.QTableWidgetItem()
                self.tbl_listado_album.setItem(i, j, item)
                item = self.tbl_listado_album.item(i, j)
                item.setText(_translate("MainWindow", valor))
                j += 1
            #Aumentamos la fila y reseteamos la columna
            i += 1
            j = 0
            #end for
        #end for
    #end mostrar_discos
#end Ventana_Listar_Discos