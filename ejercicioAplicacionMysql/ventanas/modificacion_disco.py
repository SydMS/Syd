# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificacion_disco.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from bd.operaciones import Listar_Generos
from PyQt5.Qt import Qt


class Ventana_Modificacion_Disco(object):
    def setupUi(self, Ventana_Modificacion_Disco,columna_seleccionada):
        Ventana_Modificacion_Disco.setObjectName("Ventana_Modificacion_Disco")
        Ventana_Modificacion_Disco.resize(333, 256)
        Ventana_Modificacion_Disco.setStyleSheet("background-image: url(\'images/ini_background.jpg\');background-repeat: no-repeat; background-position: center;")
        #Creamos una variable que almacena los géneros que tenemos en la bd
        self.listado_generos = Listar_Generos()
        #Según la elección del usuario mostraremos unos campos u otros
        if columna_seleccionada == 0:
            self.txt_mod_nom_disco = QtWidgets.QLineEdit(Ventana_Modificacion_Disco)
            self.txt_mod_nom_disco.setGeometry(QtCore.QRect(60, 100, 201, 21))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.txt_mod_nom_disco.setAlignment(Qt.AlignCenter)
            self.txt_mod_nom_disco.setFont(font)
            self.txt_mod_nom_disco.setStyleSheet("background: rgb(0,0,0, 0.8);color:white;border: 2px solid black;border-radius:5px;")
            self.txt_mod_nom_disco.setObjectName("txt_mod_nom_disco")
        elif columna_seleccionada == 1:
            self.txt_mod_num_pistas = QtWidgets.QLineEdit(Ventana_Modificacion_Disco)
            self.txt_mod_num_pistas.setGeometry(QtCore.QRect(135, 100, 50, 21))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.txt_mod_num_pistas.setFont(font)
            self.txt_mod_num_pistas.setAlignment(Qt.AlignCenter)
            self.txt_mod_num_pistas.setStyleSheet("background: rgb(0,0,0, 0.8);color:white;border: 2px solid black;border-radius:5px;")
            self.txt_mod_num_pistas.setObjectName("txt_mod_num_pistas")
        elif columna_seleccionada == 2:
            self.date_mod_disco_anho = QtWidgets.QDateEdit(Ventana_Modificacion_Disco)
            self.date_mod_disco_anho.setGeometry(QtCore.QRect(110, 80, 110, 22))
            self.date_mod_disco_anho.setStyleSheet("border: 2px solid black;border-radius:5px;")
            self.date_mod_disco_anho.setObjectName("date_mod_disco_anho")
        elif columna_seleccionada == 3:
            self.combo_mod_genero_disco = QtWidgets.QComboBox(Ventana_Modificacion_Disco)
            self.combo_mod_genero_disco.setGeometry(QtCore.QRect(100, 80, 140, 22))
            self.combo_mod_genero_disco.setMaxVisibleItems(7)
            self.combo_mod_genero_disco.setStyleSheet("background: rgb(0,0,0, 0.8);color:white;border: 2px solid black;border-radius:5px;")
            self.combo_mod_genero_disco.setObjectName("combo_mod_genero_disco")
            i = 0
            #Este bucle creará tanto items en el combo como géneros tengamos
            while i <= (len(self.listado_generos)-1):
                self.combo_mod_genero_disco.addItem("")
                i += 1
            #end while
        self.btn_mod_aceptar = QtWidgets.QPushButton(Ventana_Modificacion_Disco)
        self.btn_mod_aceptar.setGeometry(QtCore.QRect(40, 200, 91, 31))
        self.btn_mod_aceptar.setObjectName("btn_mod_aceptar")
        self.btn_mod_aceptar.setStyleSheet("border: 2px solid black;\n"
                                            "border-radius:5px;"
                                            "background: rgb(255,255,255, 0.8);"
                                            "color:black;")
        self.btn_mod_cancelar = QtWidgets.QPushButton(Ventana_Modificacion_Disco)
        self.btn_mod_cancelar.setGeometry(QtCore.QRect(200, 200, 91, 31))
        self.btn_mod_cancelar.setObjectName("btn_mod_cancelar")
        self.btn_mod_cancelar.setStyleSheet("border: 2px solid black;"
                                            "border-radius:5px;"
                                            "background: rgb(255,255,255, 0.8);"
                                            "color:black;")
        self.lbl_mod_disco = QtWidgets.QLabel(Ventana_Modificacion_Disco)
        #Según la elección del usuario mostraremos una situación u otra para el lbl
        if columna_seleccionada == 0 or columna_seleccionada == 3:
            self.lbl_mod_disco.setGeometry(QtCore.QRect(110, 15, 121, 21))
        elif columna_seleccionada == 1 or columna_seleccionada == 2:
            self.lbl_mod_disco.setGeometry(QtCore.QRect(80, 15, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lbl_mod_disco.setAlignment(Qt.AlignCenter)
        self.lbl_mod_disco.setFont(font)
        self.lbl_mod_disco.setStyleSheet("background: rgb(0,0,0, 0.8);color:white;border: 2px solid black;border-radius:5px;")
        self.lbl_mod_disco.setObjectName("lbl_mod_disco")
        
        

        self.retranslateUi(Ventana_Modificacion_Disco,columna_seleccionada)
        QtCore.QMetaObject.connectSlotsByName(Ventana_Modificacion_Disco)

    def retranslateUi(self, Ventana_Modificacion_Disco,columna_seleccionada):
        _translate = QtCore.QCoreApplication.translate
        Ventana_Modificacion_Disco.setWindowTitle(_translate("Ventana_Modificacion_Disco", "Modificación de datos"))
        #En caso de que el usuario haya seleccionado los géneros, cargamos los items con sus valores
        if columna_seleccionada == 0 or columna_seleccionada == 1 or columna_seleccionada == 2:
            pass
        elif columna_seleccionada == 3:
            indice = 0
            #Creamos un bucle para generar los items según haya en la bd
            for l in self.listado_generos:        
                self.combo_mod_genero_disco.setItemText(indice, _translate("Ventana_Modificacion_Artista", l[0]))
                indice += 1
        #end for 
        self.btn_mod_aceptar.setText(_translate("Ventana_Modificacion_Artista", "Aceptar"))
        self.btn_mod_cancelar.setText(_translate("Ventana_Modificacion_Artista", "Cancelar"))
        self.lbl_mod_disco.setText(_translate("Ventana_Modificacion_Artista", ""))
