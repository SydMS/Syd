'''
Created on 2 abr. 2020

@author: Sidney

Ventana Bienvenida

'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ventana_Bienvenida(object):
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
        self.lbl_bienvenida = QtWidgets.QLabel(self.principal_widget)
        self.lbl_bienvenida.setGeometry(QtCore.QRect(520, 320, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_bienvenida.setFont(font)
        self.lbl_bienvenida.setObjectName("lbl_bienvenida")
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
        self.lbl_bienvenida.setText(_translate("MainWindow", "Bienvenid@"))
        self.menuDirectorio_musical.setTitle(_translate("MainWindow", "Directorio musical"))
        self.menuListados.setTitle(_translate("MainWindow", "Listados"))
        self.actionIncluir_artista_banda.setText(_translate("MainWindow", "Incluir artista/banda"))
        self.actionIncluir_disco.setText(_translate("MainWindow", "Incluir disco"))
        self.actionIncluir_genero.setText(_translate("MainWindow", "Incluir género"))
        self.actionListar_artistas_bandas.setText(_translate("MainWindow", "Listar artistas/bandas"))
        self.actionListar_discos.setText(_translate("MainWindow", "Listar discos"))
        self.actionListar_generos.setText(_translate("MainWindow", "Listar géneros"))
    #end retranslateUi
#end Ventana_Bienvenida