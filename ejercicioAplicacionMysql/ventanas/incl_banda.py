'''
Created on 2 abr. 2020

@author: Sidney

Inclusión de discos en la bd

'''


from PyQt5 import QtCore, QtGui, QtWidgets


class Ventana_Incluir_Banda():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(647, 415)
        MainWindow.setStyleSheet("")
        self.principal_widget = QtWidgets.QWidget(MainWindow)
        self.principal_widget.setObjectName("principal_widget")
        self.gph_background = QtWidgets.QGraphicsView(self.principal_widget)
        self.gph_background.setGeometry(QtCore.QRect(-10, -20, 671, 431))
        self.gph_background.setStyleSheet("background-image: url(\'images/ini_background.jpg\');background-repeat: no-repeat; background-position: center;")
        self.gph_background.setObjectName("gph_background")
        self.lbl_nom_band = QtWidgets.QLabel(self.principal_widget)
        self.lbl_nom_band.setGeometry(QtCore.QRect(40, 50, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lbl_nom_band.setFont(font)
        self.lbl_nom_band.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                        "color:white;"
                                        "border: 2px solid black;\n"
                                        "border-radius:5px;")
        self.lbl_nom_band.setObjectName("lbl_nom_band")
        self.txt_nom_band = QtWidgets.QLineEdit(self.principal_widget)
        self.txt_nom_band.setGeometry(QtCore.QRect(270, 50, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.txt_nom_band.setFont(font)
        self.txt_nom_band.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                        "color:white;"
                                        "border: 2px solid black;\n"
                                        "border-radius:5px;")
        self.txt_nom_band.setObjectName("txt_nom_band")
        self.lbl_nom_pais = QtWidgets.QLabel(self.principal_widget)
        self.lbl_nom_pais.setGeometry(QtCore.QRect(40, 110, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lbl_nom_pais.setFont(font)
        self.lbl_nom_pais.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                        "color:white;"
                                        "border: 2px solid black;\n"
                                        "border-radius:5px;")
        self.lbl_nom_pais.setObjectName("lbl_nom_pais")
        self.txt_nom_pais = QtWidgets.QLineEdit(self.principal_widget)
        self.txt_nom_pais.setGeometry(QtCore.QRect(270, 110, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.txt_nom_pais.setFont(font)
        self.txt_nom_pais.setStyleSheet("background: rgb(0,0,0, 0.8);"
                                        "color:white;"
                                        "border: 2px solid black;\n"
                                        "border-radius:5px;\n")
        self.txt_nom_pais.setObjectName("txt_nom_pais")
        self.btn_incluir_banda = QtWidgets.QPushButton(self.principal_widget)
        self.btn_incluir_banda.setGeometry(QtCore.QRect(520, 310, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_incluir_banda.setFont(font)
        self.btn_incluir_banda.setStyleSheet("border: 2px solid black;"
                                            "border-radius:5px;"
                                            "background: rgb(255,255,255);"
                                            "color:black;")
        self.btn_incluir_banda.setObjectName("btn_incluir_banda")
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
        self.lbl_nom_band.setText(_translate("MainWindow", "Nombre artista/banda"))
        self.lbl_nom_pais.setText(_translate("MainWindow", "País"))
        self.btn_incluir_banda.setText(_translate("MainWindow", "Incluir"))
        self.actionIncluir_artista_banda.setText(_translate("MainWindow", "Incluir artista/banda"))
        self.actionIncluir_disco.setText(_translate("MainWindow", "Incluir disco"))
        self.actionIncluir_genero.setText(_translate("MainWindow", "Incluir género"))
        self.actionListar_artistas_bandas.setText(_translate("MainWindow", "Listar artistas/bandas"))
        self.actionListar_discos.setText(_translate("MainWindow", "Listar discos"))
        self.actionListar_generos.setText(_translate("MainWindow", "Listar géneros"))
    #end retranslateUi
#end Ventana_Incluir_Banda