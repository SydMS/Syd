# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_vuelo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana_vuelo(object):
    def setupUi(self, ventana_vuelo):
        ventana_vuelo.setObjectName("ventana_vuelo")
        ventana_vuelo.resize(400, 266)
        self.lbl_escoger = QtWidgets.QLabel(ventana_vuelo)
        self.lbl_escoger.setGeometry(QtCore.QRect(20, 20, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_escoger.setFont(font)
        self.lbl_escoger.setObjectName("lbl_escoger")
        self.rad_first = QtWidgets.QRadioButton(ventana_vuelo)
        self.rad_first.setGeometry(QtCore.QRect(20, 60, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rad_first.setFont(font)
        self.rad_first.setObjectName("rad_first")
        self.rad_business = QtWidgets.QRadioButton(ventana_vuelo)
        self.rad_business.setGeometry(QtCore.QRect(20, 100, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rad_business.setFont(font)
        self.rad_business.setObjectName("rad_business")
        self.rad_economic = QtWidgets.QRadioButton(ventana_vuelo)
        self.rad_economic.setGeometry(QtCore.QRect(20, 140, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rad_economic.setFont(font)
        self.rad_economic.setObjectName("rad_economic")
        self.lbl_motrar_seleccion = QtWidgets.QLabel(ventana_vuelo)
        self.lbl_motrar_seleccion.setGeometry(QtCore.QRect(50, 210, 301, 31))
        self.lbl_motrar_seleccion.setText("")
        self.lbl_motrar_seleccion.setObjectName("lbl_motrar_seleccion")

        self.retranslateUi(ventana_vuelo)
        QtCore.QMetaObject.connectSlotsByName(ventana_vuelo)
    #end setupUi
    
    def retranslateUi(self, ventana_vuelo):
        _translate = QtCore.QCoreApplication.translate
        ventana_vuelo.setWindowTitle(_translate("ventana_vuelo", "Vuelo"))
        self.lbl_escoger.setText(_translate("ventana_vuelo", "Escoja la clase de vuelo:"))
        self.rad_first.setText(_translate("ventana_vuelo", "Primera clase."))
        self.rad_business.setText(_translate("ventana_vuelo", "Clase Business."))
        self.rad_economic.setText(_translate("ventana_vuelo", "Clase Económica."))
    #end retranslateUi
#end Ui_ventana_vuelo