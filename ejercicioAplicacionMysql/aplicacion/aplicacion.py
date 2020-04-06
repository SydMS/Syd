'''
Created on 2 abr. 2020

@author: Sidney

Funcionalidades principales de la aplicación

'''

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ventanas.principal import Ventana_Bienvenida
from ventanas.incl_banda import Ventana_Incluir_Banda
from bd.operaciones import Insertar_Banda, Insertar_Genero,\
    Insertar_Album, Obtener_ID_Banda, Obtener_ID_Genero
from modelo.clases import Artista_Banda, Genero, Album
from ventanas.list_banda import Ventana_Listar_Banda
from ventanas.incl_genero import Ventana_Incluir_Genero
from ventanas.list_genero import Ventana_Listar_Generos
from ventanas.incl_album import Ventana_Incluir_Disco
from _datetime import datetime
from ventanas.list_album import Ventana_Listar_Discos


#Creamos una clase para la ventana principal
class VentanaPrincipalAplicación(QMainWindow):
    #Generamos su constructor
    def __init__(self):
        #Hacemos que herede del constructor padre
        super().__init__()
        #Preparamos un objeto con los atributos de la ventana
        self.ui_bienvenida = Ventana_Bienvenida()
        self.ui_bienvenida.setupUi(self)
        
        #Asignamos la función a cada uno de los botones del menú
        self.ui_bienvenida.actionIncluir_artista_banda.triggered.connect(self.incluir_banda)
        self.ui_bienvenida.actionIncluir_genero.triggered.connect(self.incluir_genero)
        self.ui_bienvenida.actionIncluir_disco.triggered.connect(self.incluir_disco)
        self.ui_bienvenida.actionListar_generos.triggered.connect(self.listar_generos)
        self.ui_bienvenida.actionListar_artistas_bandas.triggered.connect(self.listar_banda)
        self.ui_bienvenida.actionListar_discos.triggered.connect(self.listar_discos)
        
        
        #Mostramos la aplicación
        self.show()
    #end __init__
        
    def incluir_banda(self):
        #Se genera ui_incl_banda que contendrá la ventana para incluir bandas
        self.ui_incl_banda = Ventana_Incluir_Banda()
        self.ui_incl_banda.setupUi(self) 
        #Funciones para los botones del menú
        self.ui_incl_banda.actionIncluir_artista_banda.triggered.connect(self.incluir_banda)
        self.ui_incl_banda.actionIncluir_genero.triggered.connect(self.incluir_genero)
        self.ui_incl_banda.actionIncluir_disco.triggered.connect(self.incluir_disco)
        self.ui_incl_banda.actionListar_generos.triggered.connect(self.listar_generos)
        self.ui_incl_banda.actionListar_artistas_bandas.triggered.connect(self.listar_banda)
        self.ui_incl_banda.actionListar_discos.triggered.connect(self.listar_discos)
        
        #Mostramos la ventana       
        self.show()
        
        #Cuando se clicke en el botón se llama a la función para guardar en la bd
        self.ui_incl_banda.btn_incluir_banda.clicked.connect(self.click_incluir_banda)
    #end incluir_banda
        
    def click_incluir_banda(self):
        #Creamos una variable que contendrá los atributos de la clase Artista_Banda
        banda = Artista_Banda()
        
        #Cargamos en la variable los valores que haya introducido el usuario
        banda.nombre = self.ui_incl_banda.txt_nom_band.text()        
        banda.pais = self.ui_incl_banda.txt_nom_pais.text()
        
        #Si los campos no están vacíos, se ejecuta la función que llama a la bd
        if banda.nombre != "" and banda.pais != "":
            Insertar_Banda(banda)
        #end if
        
        #Reseteamos los cambios de texto
        self.ui_incl_banda.txt_nom_band.setText("")
        self.ui_incl_banda.txt_nom_pais.setText("")
        #Mostramos al usuario que se ha realizado el registro
        QMessageBox.about(self, "Información", "Registro realizado.")
    #end click_incluir_banda
    
    def listar_banda(self):
        #Se genera ui_list_banda que contendrá la ventana para listar las bandas
        self.ui_list_banda = Ventana_Listar_Banda()
        self.ui_list_banda.setupUi(self)
        #Funciones para los botones del menú
        self.ui_list_banda.actionIncluir_artista_banda.triggered.connect(self.incluir_banda)
        self.ui_list_banda.actionIncluir_genero.triggered.connect(self.incluir_genero)
        self.ui_list_banda.actionIncluir_disco.triggered.connect(self.incluir_disco)
        self.ui_list_banda.actionListar_generos.triggered.connect(self.listar_generos)
        self.ui_list_banda.actionListar_artistas_bandas.triggered.connect(self.listar_banda)
        self.ui_list_banda.actionListar_discos.triggered.connect(self.listar_discos)
               
        self.show()
    #end listar_banda
        
    def incluir_genero(self):
        #Se genera ui_incl_banda que contendrá la ventana para incluir generos
        self.ui_incl_genero = Ventana_Incluir_Genero()
        self.ui_incl_genero.setupUi(self) 
        #Funciones para los botones del menú
        self.ui_incl_genero.actionIncluir_artista_banda.triggered.connect(self.incluir_banda)
        self.ui_incl_genero.actionIncluir_genero.triggered.connect(self.incluir_genero)
        self.ui_incl_genero.actionIncluir_disco.triggered.connect(self.incluir_disco)
        self.ui_incl_genero.actionListar_generos.triggered.connect(self.listar_generos)
        self.ui_incl_genero.actionListar_artistas_bandas.triggered.connect(self.listar_banda)
        self.ui_incl_genero.actionListar_discos.triggered.connect(self.listar_discos)
        
        #Mostramos la ventana       
        self.show()
        
        #Cuando se clicke en el botón se llama a la función para guardar en la bd
        self.ui_incl_genero.btn_incluir_genero.clicked.connect(self.click_incluir_genero)  
    #end incluir_genero  
        
    def click_incluir_genero(self):
        #Creamos una variable que contendrá los atributos de la clase Genero
        genero_musical = Genero()
        
        #Cargamos en la variable los valores que haya introducido el usuario
        genero_musical.nombre = self.ui_incl_genero.txt_nom_genero.text()        
        
        #Si los campos no están vacíos, se ejecuta la función que llama a la bd
        if genero_musical.nombre != "":
            Insertar_Genero(genero_musical)
        
        #Reseteamos los cambios de texto
        self.ui_incl_genero.txt_nom_genero.setText("")
        #Mostramos al usuario que se ha realizado el registro
        QMessageBox.about(self, "Información", "Registro realizado.")
    #end click_incluir_genero
        
    def listar_generos(self):
        #Se genera ui_list_banda que contendrá la ventana para incluir bandas
        self.ui_list_genero = Ventana_Listar_Generos()
        self.ui_list_genero.setupUi(self)
        #Funciones para los botones del menú
        self.ui_list_genero.actionIncluir_artista_banda.triggered.connect(self.incluir_banda)
        self.ui_list_genero.actionIncluir_genero.triggered.connect(self.incluir_genero)
        self.ui_list_genero.actionIncluir_disco.triggered.connect(self.incluir_disco)
        self.ui_list_genero.actionListar_generos.triggered.connect(self.listar_generos)
        self.ui_list_genero.actionListar_artistas_bandas.triggered.connect(self.listar_banda)
        self.ui_list_genero.actionListar_discos.triggered.connect(self.listar_discos)

        #Mostramos la ventana       
        self.show()
    #end listar_generos
        
    def incluir_disco(self):
        #Se genera ui_incl_disco que contendrá la ventana para incluir los discos
        self.ui_incl_disco = Ventana_Incluir_Disco()
        self.ui_incl_disco.setupUi(self) 
        #Funciones para los botones del menú
        self.ui_incl_disco.actionIncluir_artista_banda.triggered.connect(self.incluir_banda)
        self.ui_incl_disco.actionIncluir_genero.triggered.connect(self.incluir_genero)
        self.ui_incl_disco.actionIncluir_disco.triggered.connect(self.incluir_disco)
        self.ui_incl_disco.actionListar_generos.triggered.connect(self.listar_generos)
        self.ui_incl_disco.actionListar_artistas_bandas.triggered.connect(self.listar_banda)
        self.ui_incl_disco.actionListar_discos.triggered.connect(self.listar_discos)
        
        #Mostramos la ventana       
        self.show()
        
        #Cuando se clickee en el botón se llama a la función para guardar en la bd
        self.ui_incl_disco.btn_incluir_disco.clicked.connect(self.click_incluir_disco)
    #end incluir_disco
        
    def click_incluir_disco(self):
        #Creamos una variable que contendrá los atributos de la clase Album
        disco = Album()
        
        #Cargamos en la variable los valores que haya introducido el usuario
        disco.banda = self.ui_incl_disco.combo_disco_nom_banda.currentText()
        #Actualizamos el valor con el número de ID en lugar del nombre
        disco.banda = Obtener_ID_Banda(disco.banda)
        disco.nombre_disco = self.ui_incl_disco.txt_disco_nom_album.text()
        disco.genero = self.ui_incl_disco.combo_disco_genero.currentText()
        #Actualizamos el valor con el número de ID en lugar del género
        disco.genero = Obtener_ID_Genero(disco.genero)
        disco.num_pistas = self.ui_incl_disco.txt_disco_num_pistas.text()
        disco.year = self.ui_incl_disco.date_disco_anho_publicacion.text()
        #Formateamos la fecha para que coincida con la bbdd
        disco.year = datetime.strptime(disco.year,'%d/%m/%Y')
        disco.year = datetime.strftime(disco.year,'%Y-%m-%d')  
        
        #Si los campos no están vacíos, se ejecuta la función que llama a la bd
        if disco.nombre_disco != "" and disco.banda != "" and disco.genero != "" and disco.num_pistas != "" and disco.year != "":
            Insertar_Album(disco)
        #end if
        
        #Reseteamos los cambios de texto
        self.ui_incl_disco.combo_disco_nom_banda.setCurrentText("Agnes Obel")
        self.ui_incl_disco.txt_disco_nom_album.setText("")
        self.ui_incl_disco.combo_disco_genero.setCurrentText("Blues")
        self.ui_incl_disco.txt_disco_num_pistas.setText("")
        #Mostramos al usuario que se ha realizado el registro
        QMessageBox.about(self, "Información", "Registro realizado.")
    #end click_incluir_disco
        
    def listar_discos(self):
        #Se genera ui_list_banda que contendrá la ventana para incluir bandas
        self.ui_list_discos = Ventana_Listar_Discos()
        self.ui_list_discos.setupUi(self)
        #Funciones para los botones del menú
        self.ui_list_discos.actionIncluir_artista_banda.triggered.connect(self.incluir_banda)
        self.ui_list_discos.actionIncluir_genero.triggered.connect(self.incluir_genero)
        self.ui_list_discos.actionIncluir_disco.triggered.connect(self.incluir_disco)
        self.ui_list_discos.actionListar_generos.triggered.connect(self.listar_generos)
        self.ui_list_discos.actionListar_artistas_bandas.triggered.connect(self.listar_banda)
        self.ui_list_discos.actionListar_discos.triggered.connect(self.listar_discos)

        #Mostramos la ventana       
        self.show()
        #Declaramos una variable para ayudar a cargar la función por 1ª vez
        inicio = True
        #En caso de ser la primera vez
        if inicio == True:
            self.ui_list_discos.mostrar_discos()
            #Cambiamos el valor de la variable
            inicio = False
        #end if
        
        if inicio == False:
            #A partir de la 2ª selección se ejecutará esta línea
            self.ui_list_discos.combo_list_banda_album.currentTextChanged.connect(self.ui_list_discos.mostrar_discos)
        #end if
        
    #end listar_discos
    
#end VentanaPrincipalAplicación