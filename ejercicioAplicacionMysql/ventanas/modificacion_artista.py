# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificacion_artista.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ventana_Modificacion_Artista(object):
    def setupUi(self, Ventana_Modificacion_Artista):
        Ventana_Modificacion_Artista.setObjectName("Ventana_Modificacion_Artista")
        Ventana_Modificacion_Artista.resize(333, 256)
        Ventana_Modificacion_Artista.setStyleSheet("background-image: url(\'images/ini_background.jpg\');background-repeat: no-repeat; background-position: center;")
        self.lbl_mod_nacionalidad = QtWidgets.QLabel(Ventana_Modificacion_Artista)
        self.lbl_mod_nacionalidad.setGeometry(QtCore.QRect(120, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_mod_nacionalidad.setFont(font)
        self.lbl_mod_nacionalidad.setStyleSheet("background: rgb(0,0,0,0.8);color:white;border: 2px solid black;border-radius:5px;text-decoration:center")
        self.lbl_mod_nacionalidad.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mod_nacionalidad.setObjectName("lbl_mod_nacionalidad")
        self.txt_mod_artista = QtWidgets.QLineEdit(Ventana_Modificacion_Artista)
        self.txt_mod_artista.setGeometry(QtCore.QRect(70, 60, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_mod_artista.setFont(font)
        self.txt_mod_artista.setStyleSheet("background: rgb(125,125,125, 0.8);color:white;border: 2px solid black;border-radius:5px;color:black;")
        self.txt_mod_artista.setObjectName("txt_mod_artista")
        self.txt_mod_nacionalidad = QtWidgets.QLineEdit(Ventana_Modificacion_Artista)
        self.txt_mod_nacionalidad.setGeometry(QtCore.QRect(70, 150, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_mod_nacionalidad.setFont(font)
        self.txt_mod_nacionalidad.setStyleSheet("background: rgb(125,125,125, 0.8);color:white;border: 2px solid black;border-radius:5px;color:black;")
        self.txt_mod_nacionalidad.setObjectName("txt_mod_nacionalidad")
        self.btn_mod_aceptar = QtWidgets.QPushButton(Ventana_Modificacion_Artista)
        self.btn_mod_aceptar.setGeometry(QtCore.QRect(40, 200, 91, 31))
        self.btn_mod_aceptar.setObjectName("btn_mod_aceptar")
        self.btn_mod_aceptar.setStyleSheet("border: 2px solid black;"
                                            "border-radius:5px;"
                                            "background: rgb(255,255,255);"
                                            "color:black;"
                                            "font: 13px")
        self.btn_mod_cancelar = QtWidgets.QPushButton(Ventana_Modificacion_Artista)
        self.btn_mod_cancelar.setGeometry(QtCore.QRect(200, 200, 91, 31))
        self.btn_mod_cancelar.setObjectName("btn_mod_cancelar")
        self.btn_mod_cancelar.setStyleSheet("border: 2px solid black;"
                                "border-radius:5px;"
                                "background: rgb(255,255,255);"
                                "color:black;"
                                "font: 13px")
        self.lbl_mod_artista = QtWidgets.QLabel(Ventana_Modificacion_Artista)
        self.lbl_mod_artista.setGeometry(QtCore.QRect(120, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_mod_artista.setFont(font)
        self.lbl_mod_artista.setStyleSheet("background: rgb(0,0,0, 0.8);color:white;border: 2px solid black;border-radius:5px;")
        self.lbl_mod_artista.setObjectName("lbl_mod_artista")
        self.lbl_mod_artista.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(Ventana_Modificacion_Artista)
        QtCore.QMetaObject.connectSlotsByName(Ventana_Modificacion_Artista)

    def retranslateUi(self, Ventana_Modificacion_Artista):
        _translate = QtCore.QCoreApplication.translate
        Ventana_Modificacion_Artista.setWindowTitle(_translate("Ventana_Modificacion_Artista", "Modificación Artista"))
        self.lbl_mod_nacionalidad.setText(_translate("Ventana_Modificacion_Artista", "Nacionalidad"))
        self.btn_mod_aceptar.setText(_translate("Ventana_Modificacion_Artista", "Aceptar"))
        self.btn_mod_cancelar.setText(_translate("Ventana_Modificacion_Artista", "Cancelar"))
        self.lbl_mod_artista.setText(_translate("Ventana_Modificacion_Artista", "Artista"))
