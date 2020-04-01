# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_venta.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_venta_camisa(object):
    def setupUi(self, dialog_venta_camisa):
        dialog_venta_camisa.setObjectName("dialog_venta_camisa")
        dialog_venta_camisa.resize(406, 475)
        self.lbl_talla_camisa = QtWidgets.QLabel(dialog_venta_camisa)
        self.lbl_talla_camisa.setGeometry(QtCore.QRect(30, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_talla_camisa.setFont(font)
        self.lbl_talla_camisa.setObjectName("lbl_talla_camisa")
        self.lbl_metodo_pago = QtWidgets.QLabel(dialog_venta_camisa)
        self.lbl_metodo_pago.setGeometry(QtCore.QRect(30, 230, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_metodo_pago.setFont(font)
        self.lbl_metodo_pago.setObjectName("lbl_metodo_pago")
        self.lbl_resultado_venta = QtWidgets.QLabel(dialog_venta_camisa)
        self.lbl_resultado_venta.setGeometry(QtCore.QRect(30, 420, 331, 41))
        self.lbl_resultado_venta.setText("")
        self.lbl_resultado_venta.setObjectName("lbl_resultado_venta")
        self.verticalLayoutWidget = QtWidgets.QWidget(dialog_venta_camisa)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 301, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vlayout_talla = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vlayout_talla.setContentsMargins(0, 0, 0, 0)
        self.vlayout_talla.setObjectName("vlayout_talla")
        self.rbn_talla_S = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbn_talla_S.setFont(font)
        self.rbn_talla_S.setObjectName("rbn_talla_S")
        self.vlayout_talla.addWidget(self.rbn_talla_S)
        self.rbn_talla_M = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbn_talla_M.setFont(font)
        self.rbn_talla_M.setObjectName("rbn_talla_M")
        self.vlayout_talla.addWidget(self.rbn_talla_M)
        self.rbn_talla_L = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbn_talla_L.setFont(font)
        self.rbn_talla_L.setObjectName("rbn_talla_L")
        self.vlayout_talla.addWidget(self.rbn_talla_L)
        self.rbn_talla_XL = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbn_talla_XL.setFont(font)
        self.rbn_talla_XL.setObjectName("rbn_talla_XL")
        self.vlayout_talla.addWidget(self.rbn_talla_XL)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(dialog_venta_camisa)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 260, 301, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.vlayout_pago = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vlayout_pago.setContentsMargins(0, 0, 0, 0)
        self.vlayout_pago.setObjectName("vlayout_pago")
        self.rbn_pago_tarjeta = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbn_pago_tarjeta.setFont(font)
        self.rbn_pago_tarjeta.setObjectName("rbn_pago_tarjeta")
        self.vlayout_pago.addWidget(self.rbn_pago_tarjeta)
        self.rbn_pago_reembolso = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbn_pago_reembolso.setFont(font)
        self.rbn_pago_reembolso.setObjectName("rbn_pago_reembolso")
        self.vlayout_pago.addWidget(self.rbn_pago_reembolso)
        self.rbn_pago_paypal = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbn_pago_paypal.setFont(font)
        self.rbn_pago_paypal.setObjectName("rbn_pago_paypal")
        self.vlayout_pago.addWidget(self.rbn_pago_paypal)

        self.retranslateUi(dialog_venta_camisa)
        QtCore.QMetaObject.connectSlotsByName(dialog_venta_camisa)
    #end setupUi

    def retranslateUi(self, dialog_venta_camisa):
        _translate = QtCore.QCoreApplication.translate
        dialog_venta_camisa.setWindowTitle(_translate("dialog_venta_camisa", "Venta de camisas"))
        self.lbl_talla_camisa.setText(_translate("dialog_venta_camisa", "Seleccione la talla de su camisa:"))
        self.lbl_metodo_pago.setText(_translate("dialog_venta_camisa", "Seleccione su método de pago:"))
        self.rbn_talla_S.setText(_translate("dialog_venta_camisa", "Talla S"))
        self.rbn_talla_M.setText(_translate("dialog_venta_camisa", "Talla M"))
        self.rbn_talla_L.setText(_translate("dialog_venta_camisa", "Talla L"))
        self.rbn_talla_XL.setText(_translate("dialog_venta_camisa", "Talla XL"))
        self.rbn_pago_tarjeta.setText(_translate("dialog_venta_camisa", "Tarjeta de crédito/débito"))
        self.rbn_pago_reembolso.setText(_translate("dialog_venta_camisa", "Pago contrareembolso"))
        self.rbn_pago_paypal.setText(_translate("dialog_venta_camisa", "PayPal"))
    #end retranslateUi
#end Ui_dialog_venta_camisa