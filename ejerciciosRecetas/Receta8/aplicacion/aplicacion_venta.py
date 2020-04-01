'''
Created on 1 abr. 2020

@author: Sidney

'''

from PyQt5.QtWidgets import QDialog
from Receta8.ventanas.ventana_venta import Ui_dialog_venta_camisa

#Generamos una clase que contendrá los elementos de la venta
class VentanaCamisas(QDialog):
    #Definimos el constructor
    def __init__(self):
        #Hacemos que herede de QDialog
        super().__init__()
        #Definimos las variables que almacenarán lo seleccionado
        self.talla = ""
        self.pago = ""
        
        self.ui_venta = Ui_dialog_venta_camisa()
        self.ui_venta.setupUi(self)
        
        #En caso de que cambie el estado de estos botones se ejecutará 
        #su correspondiente función para almacenar el valor en la variable
        self.ui_venta.rbn_talla_S.toggled.connect(self.mostrar_talla)
        self.ui_venta.rbn_talla_M.toggled.connect(self.mostrar_talla)
        self.ui_venta.rbn_talla_L.toggled.connect(self.mostrar_talla)
        self.ui_venta.rbn_talla_XL.toggled.connect(self.mostrar_talla)
        
        self.ui_venta.rbn_pago_tarjeta.toggled.connect(self.mostrar_pago)
        self.ui_venta.rbn_pago_reembolso.toggled.connect(self.mostrar_pago)
        self.ui_venta.rbn_pago_paypal.toggled.connect(self.mostrar_pago)
        
                   
        self.show()
    #end __init__
    
        
    def mostrar_talla(self):
        #Dependiendo del botón seleccionado se guardará su valor en la variable
        if self.ui_venta.rbn_talla_S.isChecked():
            self.talla = "S"
        elif self.ui_venta.rbn_talla_M.isChecked():
            self.talla = "M"
        elif self.ui_venta.rbn_talla_L.isChecked():
            self.talla = "L"
        elif self.ui_venta.rbn_talla_XL.isChecked():
            self.talla = "XL"
        
        #Devolvemos el valor almacenado a la función que lo mostrará en pantalla
        return self.mostrar_venta(self.talla,self.pago)
    #end mostrar_talla
    
    
    def mostrar_pago(self):
        if self.ui_venta.rbn_pago_tarjeta.isChecked():
            self.pago = "tarjeta de crédito/débito"
        elif self.ui_venta.rbn_pago_reembolso.isChecked():
            self.pago = "contrareembolso"
        elif self.ui_venta.rbn_pago_paypal.isChecked():
            self.pago = "PayPal"
            
        return self.mostrar_venta(self.talla,self.pago)
    #end mostrar_pago
    
    
    def mostrar_venta(self,talla,pago):
        #En caso de que ambas variables tengan un valor guardado diferente a ""
        if (self.talla != "") and (self.pago != ""):
            #Lo mostramos en pantalla
            self.ui_venta.lbl_resultado_venta.setText("Vas a comprar una camisa talla {}. (Pago {})".format(self.talla,self.pago))
        
    #end mostrar_venta

#end VentanaCamisas