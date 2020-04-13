'''
Created on 2 abr. 2020

@author: Sidney

Funcionalidades principales de la aplicación

'''

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from ventanas.principal import Ventana_Bienvenida
from ventanas.incl_banda import Ventana_Incluir_Banda
from bd.operaciones import Insertar_Banda, Insertar_Genero,\
    Insertar_Album, Obtener_ID_Banda, Obtener_ID_Genero, Modificar_Banda,\
    Eliminar_Banda, Obtener_ID_Album, Modificar_Album, Eliminar_Disco
from modelo.clases import Artista_Banda, Genero, Album
from ventanas.list_banda import Ventana_Listar_Banda
from ventanas.incl_genero import Ventana_Incluir_Genero
from ventanas.list_genero import Ventana_Listar_Generos
from ventanas.incl_album import Ventana_Incluir_Disco
from _datetime import datetime
from ventanas.list_album import Ventana_Listar_Discos
from ventanas.modificacion_artista import Ventana_Modificacion_Artista
from functools import partial
from ventanas.modificacion_disco import Ventana_Modificacion_Disco


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
        
        #Mostramos al usuario que se ha realizado el registro
        QMessageBox.about(self, "Información", "Registro realizado.")
    #end click_incluir_banda
        
        #Reseteamos la ventana
        self.incluir_banda()
    
    def listar_banda(self):
        #Se genera ui_list_banda que contendrá la ventana para listar las bandas
        self.ui_list_banda = Ventana_Listar_Banda()
        self.ui_list_banda.setupUi(self)
        
        self.ui_list_banda.tbl_listado_artistas.clicked.connect(self.ui_list_banda.modificar_eliminar)        
        self.ui_list_banda.btn_modificar_banda.clicked.connect(self.ventana_modificacion_banda)
        self.ui_list_banda.btn_eliminar_banda.clicked.connect(self.eliminar_banda)
        
        #Mostramos la ventana
        self.show()
    #end listar_banda
    
    def ventana_modificacion_banda(self):
        #Creamos una ventana secundaria para realizar la modificación/eliminación
        self.ventana = QDialog()
        self.ui_mod = Ventana_Modificacion_Artista()
        self.ui_mod.setupUi(self.ventana)
        #Creamos un elemento para los valores de esta clase
        antigua_banda = Artista_Banda()
        #Recogemos la columna que ha seleccionado el usuario
        columna_seleccionada = self.ui_list_banda.tbl_listado_artistas.currentColumn()
        #Mostraremos al usuario los datos ordenados independientemente de su selección
        if columna_seleccionada == 0:
            antigua_banda.nombre =  self.ui_list_banda.tbl_listado_artistas.currentItem().text()
            self.ui_mod.txt_mod_artista.setText(antigua_banda.nombre)
            row = self.ui_list_banda.tbl_listado_artistas.currentRow()
            antigua_banda.pais = self.ui_list_banda.tbl_listado_artistas.item(row, 1).text()
            self.ui_mod.txt_mod_nacionalidad.setText(antigua_banda.pais)
        elif columna_seleccionada == 1:
            row = self.ui_list_banda.tbl_listado_artistas.currentRow()
            antigua_banda.nombre = self.ui_list_banda.tbl_listado_artistas.item(row, 0).text()
            self.ui_mod.txt_mod_artista.setText(antigua_banda.nombre)
            antigua_banda.pais = self.ui_list_banda.tbl_listado_artistas.currentItem().text()
            self.ui_mod.txt_mod_nacionalidad.setText(antigua_banda.pais)
        #end if
        
        self.ventana.show()
        #Acciones para los botones de modificar y eliminar
        self.ui_mod.btn_mod_aceptar.clicked.connect(partial(self.modificar_banda,antigua_banda))
        self.ui_mod.btn_mod_cancelar.clicked.connect(lambda:self.ventana.close())
        
    #end ventana_modificacion
    
    def modificar_banda(self,antigua_banda):
        #Este método tiene como parámetro el elemento que se quiere modificar
        #Creamos una elemento de la clase Artista_Banda
        nueva_banda = Artista_Banda()
        #Cargamos los valores introducidos por el usuario
        nueva_banda.nombre = self.ui_mod.txt_mod_artista.text()
        nueva_banda.pais = self.ui_mod.txt_mod_nacionalidad.text()
        #Obtenemos el id de la banda a modificar
        id_banda = Obtener_ID_Banda(antigua_banda.nombre)
        
        #Lanzamos la modificación de los datos
        Modificar_Banda(nueva_banda,id_banda)
        
        #Cerramos la ventana secundaria y actualizamos la lista
        self.ventana.close()
        self.listar_banda()
        
    
    #end modificar_artista
    
    def eliminar_banda(self):
        #Confirmamos la eliminación de la banda y sus discos
        respuesta = QMessageBox.question(self, 'Eliminar artista', "¿Quiere eliminar este artista y todos sus discos?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if respuesta == QMessageBox.No:
            return
        elif respuesta == QMessageBox.Yes:
            columna_seleccionada = self.ui_list_banda.tbl_listado_artistas.currentColumn()
            if columna_seleccionada == 0:
                #Si el usuario seleccionó la 1º columna obtenemos el ID de la banda
                nombre_banda =  self.ui_list_banda.tbl_listado_artistas.currentItem().text()
                id_banda = Obtener_ID_Banda(nombre_banda)
            elif columna_seleccionada == 1:
                #Si el usuario ha seleccionado la 2º columna, recogemos el valor de la primera para el ID
                row = self.ui_list_banda.tbl_listado_artistas.currentRow()
                nombre_banda = self.ui_list_banda.tbl_listado_artistas.item(row, 0).text()
                id_banda = Obtener_ID_Banda(nombre_banda)
            #end if
        #end if
            
            Eliminar_Banda(id_banda)
        #Actualizamos la lista
        self.listar_banda()
    #end eliminar_banda
            
    def incluir_genero(self):
        #Se genera ui_incl_banda que contendrá la ventana para incluir generos
        self.ui_incl_genero = Ventana_Incluir_Genero()
        self.ui_incl_genero.setupUi(self) 
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
        
        #Mostramos al usuario que se ha realizado el registro
        QMessageBox.about(self, "Información", "Registro realizado.")
        
        #Reseteamos la ventana
        self.incluir_genero()
    #end click_incluir_genero
        
    def listar_generos(self):
        #Se genera ui_list_banda que contendrá la ventana para incluir bandas
        self.ui_list_genero = Ventana_Listar_Generos()
        self.ui_list_genero.setupUi(self)

        #Mostramos la ventana       
        self.show()
    #end listar_generos
        
    def incluir_disco(self):
        #Se genera ui_incl_disco que contendrá la ventana para incluir los discos
        self.ui_incl_disco = Ventana_Incluir_Disco()
        self.ui_incl_disco.setupUi(self) 
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
        #Damos formato a la fecha
        disco.year = datetime.strptime(disco.year,'%d/%m/%Y')
        disco.year = datetime.strftime(disco.year,'%Y-%m-%d')  
        
        #Si los campos no están vacíos, se ejecuta la función que llama a la bd
        if disco.nombre_disco != "" and disco.banda != "" and disco.genero != "" and disco.num_pistas != "" and disco.year != "":
            Insertar_Album(disco)
        #end if
        
        QMessageBox.about(self, "Información", "Registro realizado.")
        #Reseteamos la ventana
        self.incluir_disco()
    #end click_incluir_disco

        
    def listar_discos(self, banda = 0):
        #Este método podrá recibir la banda que hay que mostrar primero
        
        #Se genera ui_list_banda que contendrá la ventana para incluir bandas
        self.ui_list_discos = Ventana_Listar_Discos()
        self.ui_list_discos.setupUi(self)
        
        #Mostramos la ventana       
        self.show()
        #Declaramos una variable para ayudar a cargar la función por 1ª vez
        inicio = True
        #En caso de ser la primera vez
        if inicio == True:
            if banda == 0:
                #En caso de no haber recibido ninguna banda para mostrar
                self.ui_list_discos.mostrar_discos(banda)
            else:
                #Si la recibió
                self.ui_list_discos.mostrar_discos(banda)
                self.ui_list_discos.combo_list_banda_album.setCurrentText(banda)
            
            #Cambiamos el valor de la variable
            inicio = False
        #end if
        
        if inicio == False:
            #A partir de la 2ª selección se ejecutará esta línea
            if banda == 0:
                #Si no se ha recibido ninguna banda en particular para mostrar
                #ejecutamos los valores por defecto
                self.ui_list_discos.combo_list_banda_album.currentTextChanged.connect(self.ui_list_discos.mostrar_discos)
                #Al cambiar la selección del combo, ocultamos los botones de mod/eli
                self.ui_list_discos.combo_list_banda_album.currentTextChanged.connect(partial(self.ui_list_discos.modificar_eliminar_disco,False))
                #Al clickar sobre la tabla, mostramos los botones mod/eli
                self.ui_list_discos.tbl_listado_album.clicked.connect(partial(self.ui_list_discos.modificar_eliminar_disco,True))
                self.ui_list_discos.btn_modificar_disco.clicked.connect(self.modificacion_discos)
                self.ui_list_discos.btn_eliminar_disco.clicked.connect(self.eliminar_disco)
            else:
                #Si se recibió, situaremos el combo en dicha banda
                self.ui_list_discos.combo_list_banda_album.setCurrentText(banda)
                self.ui_list_discos.combo_list_banda_album.currentTextChanged.connect(self.ui_list_discos.mostrar_discos)
                self.ui_list_discos.combo_list_banda_album.currentTextChanged.connect(partial(self.ui_list_discos.modificar_eliminar_disco,False))
                self.ui_list_discos.tbl_listado_album.clicked.connect(partial(self.ui_list_discos.modificar_eliminar_disco,True))
                self.ui_list_discos.btn_modificar_disco.clicked.connect(self.modificacion_discos)
                self.ui_list_discos.btn_eliminar_disco.clicked.connect(self.eliminar_disco)
        #end if
    #end listar_discos
    
    
    def modificacion_discos(self):
        #Abrimos una ventana secundaria para las modificaciones
        self.ventana = QDialog()
        self.ui_mod_disco = Ventana_Modificacion_Disco()
        #Recogemos la columna que ha seleccionado el usuario
        columna_seleccionada = self.ui_list_discos.tbl_listado_album.currentColumn()
        #Pasamos la columna a setupUi para mostrar la ventana adecuada
        self.ui_mod_disco.setupUi(self.ventana,columna_seleccionada)
        
        #Según la columna que haya seleccionado se mostrarán los textos adecuados
        #Además se carga en la ventana secundaria el valor que se quiere modificar
        if columna_seleccionada == 0:
            self.ui_mod_disco.lbl_mod_disco.setText("Nombre disco")
            antiguo_nombre = self.ui_list_discos.tbl_listado_album.currentItem().text()
            self.ui_mod_disco.txt_mod_nom_disco.setText(antiguo_nombre)
        elif columna_seleccionada == 1:
            self.ui_mod_disco.lbl_mod_disco.setText("Número de pistas")
            antiguo_num_pistas = self.ui_list_discos.tbl_listado_album.currentItem().text()
            self.ui_mod_disco.txt_mod_num_pistas.setText(antiguo_num_pistas)
        elif columna_seleccionada == 2:
            antiguo_anho = self.ui_list_discos.tbl_listado_album.currentItem().text()
            antiguo_anho = datetime.strptime(antiguo_anho,'%d/%m/%Y')
            self.ui_mod_disco.date_mod_disco_anho.setDate(antiguo_anho)
            self.ui_mod_disco.lbl_mod_disco.setText("Fecha de lanzamiento")
        elif columna_seleccionada == 3:
            self.ui_mod_disco.lbl_mod_disco.setText("Género musical")
            genero = self.ui_list_discos.tbl_listado_album.currentItem().text()
            self.ui_mod_disco.combo_mod_genero_disco.setCurrentText(genero)
        
        self.ventana.show()
        
        self.ui_mod_disco.btn_mod_aceptar.clicked.connect(partial(self.click_modificar_disco,columna_seleccionada))
    
        self.ui_mod_disco.btn_mod_cancelar.clicked.connect(lambda:self.ventana.close())
    #end modificacion_disco
        
    def click_modificar_disco(self,columna_seleccionada):
        #Variable con los atributos de la clase Album
        disco = Album()
        #Recogemos la fila que ha seleccionado el usuario
        fila = self.ui_list_discos.tbl_listado_album.currentRow()
        
        #Guardamos el nombre de la banda seleccionada para después actualizar la ventana
        banda = self.ui_list_discos.combo_list_banda_album.currentText()
        
        #Dependiendo de la columna seleccionada por el usuario, guardamos los
        #datos dentro de la variable
        if columna_seleccionada == 0:                
            disco.nombre_disco = self.ui_mod_disco.txt_mod_nom_disco.text()
            disco.num_pistas = self.ui_list_discos.tbl_listado_album.item(fila, 1).text()
            disco.year = self.ui_list_discos.tbl_listado_album.item(fila, 2).text()
            disco.genero = self.ui_list_discos.tbl_listado_album.item(fila, 3).text()
        elif columna_seleccionada == 1:
            disco.nombre_disco = self.ui_list_discos.tbl_listado_album.item(fila, 0).text()
            disco.num_pistas = self.ui_mod_disco.txt_mod_num_pistas.text()
            disco.year = self.ui_list_discos.tbl_listado_album.item(fila, 2).text()
            disco.genero = self.ui_list_discos.tbl_listado_album.item(fila, 3).text()
        elif columna_seleccionada == 2:
            disco.nombre_disco = self.ui_list_discos.tbl_listado_album.item(fila, 0).text()
            disco.num_pistas = self.ui_list_discos.tbl_listado_album.item(fila, 1).text()
            disco.year = self.ui_mod_disco.date_mod_disco_anho.text()
            disco.genero = self.ui_list_discos.tbl_listado_album.item(fila, 3).text()
        elif columna_seleccionada == 3:
            disco.nombre_disco = self.ui_list_discos.tbl_listado_album.item(fila, 0).text()
            disco.num_pistas = self.ui_list_discos.tbl_listado_album.item(fila, 1).text()
            disco.year = self.ui_list_discos.tbl_listado_album.item(fila,2).text()
            disco.genero = self.ui_mod_disco.combo_mod_genero_disco.currentText()
        
        #Guardamos también el nombre de la banda y obtenemos su ID
        disco.banda = self.ui_list_discos.combo_list_banda_album.currentText()
        disco.banda = Obtener_ID_Banda(disco.banda)
        #Modificamos el formato de la fecha para adecuarlo a la bd
        disco.year = datetime.strptime(disco.year,'%d/%m/%Y')
        disco.year = datetime.strftime(disco.year,'%Y-%m-%d') 
        #Obtenemos el ID del género
        disco.genero = Obtener_ID_Genero(disco.genero)
        
        #Guardamos el nombre anterior del disco porque lo necesitamos para la modificación
        anterior_nombre_disco = self.ui_list_discos.tbl_listado_album.item(fila,0).text()
        
        id_disco = Obtener_ID_Album(disco.banda,anterior_nombre_disco)
        
        #Lanzamos la modificación con los nuevos datos
        Modificar_Album(disco,id_disco)
        #Mostramos al usuario un mensaje confirmando que se ha realizado
        QMessageBox.about(self, "Información", "Registro modificado.")
        #Cerramos la ventana secundaria
        self.ventana.close()
        #Actualizamos el ventana con la misma banda
        self.listar_discos(banda)       
        
    #end click_modificar_disco
    
    
    def eliminar_disco(self):
        #Almacenamos la banda de la que se quiere eliminar el disco
        banda = self.ui_list_discos.combo_list_banda_album.currentText()
        #Pedimos confirmación al usuario y marcamos por defecto el No
        respuesta = QMessageBox.question(self, 'Eliminar disco', "¿Está seguro de que quiere eliminar este disco?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if respuesta == QMessageBox.No:
            return
        elif respuesta == QMessageBox.Yes:
            #Recogemos el valor nombre_disco correspondiente a la fila seleccionada
            fila_seleccionada = self.ui_list_discos.tbl_listado_album.currentRow()
            if fila_seleccionada == 0:
                nombre_disco =  self.ui_list_discos.tbl_listado_album.currentItem().text()
            else:
                nombre_disco = self.ui_list_discos.tbl_listado_album.item(fila_seleccionada, 0).text()
            #end if
        #end if
        
            #Guardamos el nombre de la banda y consultamos su ID
            nombre_banda = self.ui_list_discos.combo_list_banda_album.currentText()
            id_banda = Obtener_ID_Banda(nombre_banda)
            #Obtenemos el ID del album que se quiere eliminar y lanzamos la sentencia
            id_album = Obtener_ID_Album(id_banda, nombre_disco)
            Eliminar_Disco(id_album)
        #Actualizamos la ventana con la misma banda
        self.listar_discos(banda)
    #end eliminar_disco
    
#end VentanaPrincipalAplicación