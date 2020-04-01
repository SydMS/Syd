# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_pizzeria.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana_pizza(object):
    def setupUi(self, ventana_pizza):
        ventana_pizza.setObjectName("ventana_pizza")
        ventana_pizza.resize(400, 300)
        self.lbl_pizza_base = QtWidgets.QLabel(ventana_pizza)
        self.lbl_pizza_base.setGeometry(QtCore.QRect(30, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.lbl_pizza_base.setFont(font)
        self.lbl_pizza_base.setObjectName("lbl_pizza_base")
        self.lbl_seleccione_extras = QtWidgets.QLabel(ventana_pizza)
        self.lbl_seleccione_extras.setGeometry(QtCore.QRect(30, 60, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_seleccione_extras.setFont(font)
        self.lbl_seleccione_extras.setObjectName("lbl_seleccione_extras")
        self.verticalLayoutWidget = QtWidgets.QWidget(ventana_pizza)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 100, 251, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vlayout_extras = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vlayout_extras.setContentsMargins(0, 0, 0, 0)
        self.vlayout_extras.setObjectName("vlayout_extras")
        self.chk_extra_queso = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chk_extra_queso.setObjectName("chk_extra_queso")
        self.vlayout_extras.addWidget(self.chk_extra_queso)
        self.chk_extra_pepperoni = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chk_extra_pepperoni.setObjectName("chk_extra_pepperoni")
        self.vlayout_extras.addWidget(self.chk_extra_pepperoni)
        self.chk_extra_champi = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chk_extra_champi.setObjectName("chk_extra_champi")
        self.vlayout_extras.addWidget(self.chk_extra_champi)
        self.chk_extra_barbacoa = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chk_extra_barbacoa.setObjectName("chk_extra_barbacoa")
        self.vlayout_extras.addWidget(self.chk_extra_barbacoa)
        self.lbl_mostrar_precio = QtWidgets.QLabel(ventana_pizza)
        self.lbl_mostrar_precio.setGeometry(QtCore.QRect(20, 240, 351, 31))
        self.lbl_mostrar_precio.setText("")
        self.lbl_mostrar_precio.setObjectName("lbl_mostrar_precio")

        self.retranslateUi(ventana_pizza)
        QtCore.QMetaObject.connectSlotsByName(ventana_pizza)
    #end setUi
    
    def retranslateUi(self, ventana_pizza):
        _translate = QtCore.QCoreApplication.translate
        ventana_pizza.setWindowTitle(_translate("ventana_pizza", "Menú Pizzería"))
        self.lbl_pizza_base.setText(_translate("ventana_pizza", "Precio Pizza (Base 15 €)"))
        self.lbl_seleccione_extras.setText(_translate("ventana_pizza", "Seleccione los extras que quiere añadir:"))
        self.chk_extra_queso.setText(_translate("ventana_pizza", "Extra Queso"))
        self.chk_extra_pepperoni.setText(_translate("ventana_pizza", "Pepperoni"))
        self.chk_extra_champi.setText(_translate("ventana_pizza", "Champiñones"))
        self.chk_extra_barbacoa.setText(_translate("ventana_pizza", "Salsa barbacoa"))
    #end retranslateUi
#end Ui_ventana_pizza
