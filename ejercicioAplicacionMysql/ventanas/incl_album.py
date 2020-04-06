'''
Created on 2 abr. 2020

@author: Sidney

Inclusión de discos en la bd

'''

from PyQt5 import QtCore, QtGui, QtWidgets
from bd.operaciones import Listar_Generos, Listar_Bandas


class Ventana_Incluir_Disco(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(647, 415)
        MainWindow.setStyleSheet("")
        self.listado_generos = Listar_Generos()
        self.listado_bandas = Listar_Bandas()
        self.principal_widget = QtWidgets.QWidget(MainWindow)
        self.principal_widget.setObjectName("principal_widget")
        self.gph_background = QtWidgets.QGraphicsView(self.principal_widget)
        self.gph_background.setGeometry(QtCore.QRect(-10, -20, 671, 431))
        self.gph_background.setStyleSheet("background-image: url(\'images/ini_background.jpg\');background-repeat: no-repeat; background-position: center;")
        self.gph_background.setObjectName("gph_background")
        self.lbl_disco_nom_banda = QtWidgets.QLabel(self.principal_widget)
        self.lbl_disco_nom_banda.setGeometry(QtCore.QRect(40, 50, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lbl_disco_nom_banda.setFont(font)
        self.lbl_disco_nom_banda.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                               "color:white;"
                                                "border: 2px solid black;\n"
                                                "border-radius:5px;")
        self.lbl_disco_nom_banda.setObjectName("lbl_disco_nom_banda")
        self.lbl_disco_nom_album = QtWidgets.QLabel(self.principal_widget)
        self.lbl_disco_nom_album.setGeometry(QtCore.QRect(40, 100, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lbl_disco_nom_album.setFont(font)
        self.lbl_disco_nom_album.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                               "color:white;"
                                                "border: 2px solid black;\n"
                                                "border-radius:5px;")
        self.lbl_disco_nom_album.setObjectName("lbl_disco_nom_album")
        self.txt_disco_nom_album = QtWidgets.QLineEdit(self.principal_widget)
        self.txt_disco_nom_album.setGeometry(QtCore.QRect(270, 100, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.txt_disco_nom_album.setFont(font)
        self.txt_disco_nom_album.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                               "color:white;"
                                                "border: 2px solid black;\n"
                                                "border-radius:5px;\n")
        self.txt_disco_nom_album.setObjectName("txt_disco_nom_album")
        self.btn_incluir_disco = QtWidgets.QPushButton(self.principal_widget)
        self.btn_incluir_disco.setGeometry(QtCore.QRect(520, 310, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_incluir_disco.setFont(font)
        self.btn_incluir_disco.setStyleSheet("border: 2px solid black;\n"
                                            "border-radius:5px;\n"
                                            "background: rgb(255,255,255, 0.8);"
                                            "color:black;")
        self.btn_incluir_disco.setObjectName("btn_incluir_disco")
        self.lbl_disco_num_pistas = QtWidgets.QLabel(self.principal_widget)
        self.lbl_disco_num_pistas.setGeometry(QtCore.QRect(40, 200, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lbl_disco_num_pistas.setFont(font)
        self.lbl_disco_num_pistas.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                                "color:white;"
                                                "border: 2px solid black;\n"
                                                "border-radius:5px;")
        self.lbl_disco_num_pistas.setObjectName("lbl_disco_num_pistas")
        self.txt_disco_num_pistas = QtWidgets.QLineEdit(self.principal_widget)
        self.txt_disco_num_pistas.setGeometry(QtCore.QRect(500, 200, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.txt_disco_num_pistas.setFont(font)
        self.txt_disco_num_pistas.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                                "color:white;"
                                                "border: 2px solid black;\n"
                                                "border-radius:5px;\n")
        self.txt_disco_num_pistas.setObjectName("txt_disco_num_pistas")
        self.lbl_disco_anho_publicacion = QtWidgets.QLabel(self.principal_widget)
        self.lbl_disco_anho_publicacion.setGeometry(QtCore.QRect(40, 250, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lbl_disco_anho_publicacion.setFont(font)
        self.lbl_disco_anho_publicacion.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                                      "color:white;"
                                                    "border: 2px solid black;\n"
                                                    "border-radius:5px;")
        self.lbl_disco_anho_publicacion.setObjectName("lbl_disco_anho_publicacion")
        self.date_disco_anho_publicacion = QtWidgets.QDateEdit(self.principal_widget)
        self.date_disco_anho_publicacion.setGeometry(QtCore.QRect(500, 250, 110, 22))
        self.date_disco_anho_publicacion.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                                      "color:white;"
                                                      "border: 2px solid black;\n"
                                                      "border-radius:5px;")
        self.date_disco_anho_publicacion.setObjectName("date_disco_anho_publicacion")
        self.combo_disco_nom_banda = QtWidgets.QComboBox(self.principal_widget)
        self.combo_disco_nom_banda.setGeometry(QtCore.QRect(400, 50, 211, 22))
        self.combo_disco_nom_banda.setStyleSheet("background-color:black;color:white;border: 2px solid black;border-radius:5px;")
        self.combo_disco_nom_banda.setObjectName("combo_disco_nom_banda")
        i = 0
        while i <= (len(self.listado_bandas)-1):
            self.combo_disco_nom_banda.addItem("")
            i += 1
        #end while
        self.lbl_disco_genero = QtWidgets.QLabel(self.principal_widget)
        self.lbl_disco_genero.setGeometry(QtCore.QRect(40, 150, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lbl_disco_genero.setFont(font)
        self.lbl_disco_genero.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                            "color:white;"
                                            "border: 2px solid black;\n"
                                            "border-radius:5px;")
        self.lbl_disco_genero.setObjectName("lbl_disco_genero")
        self.combo_disco_genero = QtWidgets.QComboBox(self.principal_widget)
        self.combo_disco_genero.setGeometry(QtCore.QRect(400, 150, 211, 22))
        self.combo_disco_genero.setStyleSheet("background-color:black;color:white;border: 2px solid black;border-radius:5px;")
        self.combo_disco_genero.setObjectName("combo_disco_genero")
        i = 0
        while i <= (len(self.listado_generos)-1):
            self.combo_disco_genero.addItem("")
            i += 1
        #end while
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
        self.lbl_disco_nom_banda.setText(_translate("MainWindow", "Artista/Banda"))
        self.lbl_disco_nom_album.setText(_translate("MainWindow", "Nombre del álbum"))
        self.btn_incluir_disco.setText(_translate("MainWindow", "Incluir"))
        self.lbl_disco_num_pistas.setText(_translate("MainWindow", "Número de pistas"))
        self.lbl_disco_anho_publicacion.setText(_translate("MainWindow", "Año de publicación"))
        indice = 0
        for l in self.listado_bandas:        
            self.combo_disco_nom_banda.setItemText(indice, _translate("MainWindow", l[0]))
            indice += 1
        #end for
        
        self.lbl_disco_genero.setText(_translate("MainWindow", "Género musical"))
        #Creamos un bucle para generar los items según haya en la bd
        indice = 0
        for l in self.listado_generos:        
            self.combo_disco_genero.setItemText(indice, _translate("MainWindow", l[0]))
            indice += 1
        #end for        
        
        self.menuDirectorio_musical.setTitle(_translate("MainWindow", "Directorio musical"))
        self.menuListados.setTitle(_translate("MainWindow", "Listados"))
        self.actionIncluir_artista_banda.setText(_translate("MainWindow", "Incluir artista/banda"))
        self.actionIncluir_disco.setText(_translate("MainWindow", "Incluir disco"))
        self.actionIncluir_genero.setText(_translate("MainWindow", "Incluir género"))
        self.actionListar_artistas_bandas.setText(_translate("MainWindow", "Listar artistas/bandas"))
        self.actionListar_discos.setText(_translate("MainWindow", "Listar discos"))
        self.actionListar_generos.setText(_translate("MainWindow", "Listar géneros"))
    #end retranslateUi
#end Ventana_Incluir_Disco