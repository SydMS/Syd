'''
Módulo para la interfaz gráfica y la resolución

En construcción...
'''

from tkinter import Text, Button, END

class Interfaz:
    #Definimos un constructor para la ventana principal
    def __init__(self,ventana):
        #Asignamos el parámetro al self
        self.ventana = ventana
        #Título que aparecerá en la ventana
        self.ventana.title("Calculadora")
        
        #Definimos el visor de la calculadora, que estará deshabilitado
        #para que nos e pueda escribir
        self.visor = Text(ventana, state="disabled", width=40, height=3, background="blue", foreground="white",font=("Arial",15))
        
        #Usamos grid para situarlo en la ventana y le damos un pad
        self.visor.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
        
        #la operacion que tiene que desarrollar la calculadora
        self.operacion = ""
        
        #Generamos los botones usando el módulo boton
        boton1 = self.boton(7)
        boton2 = self.boton(8)
        boton3 = self.boton(9)
        boton4 = self.boton("/")
        boton5 = self.boton(4)
        boton6 = self.boton(5)
        boton7 = self.boton(6)
        boton8 = self.boton("x")
        boton9 = self.boton(3)
        boton10 = self.boton(2)
        boton11 = self.boton(1)
        boton12 = self.boton("-")
        boton13 = self.boton(",")
        boton14 = self.boton(0)
        boton15 = self.boton("Del",escribir=False)
        boton16 = self.boton("+")
        boton17 = self.boton("=",escribir=False,size=18)
        
        
        #Almacenamos todos los botones en una tupla
        botones = (boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,
                   boton10,boton11,boton12,boton13,boton14,boton15,boton16,boton17)
        
        #Definimos una variable índice para el bucle
        indice = 0
        #Este bucle generará el grid para cada boton, excepto el =
        for fila in range(1,5):
            for columna in range(4):
                botones[indice].grid(row=fila,column=columna,padx=2,pady=2,ipady=3)
                indice += 1
        
        #Tratamos el botón = de forma específica para darle otra configuración                
        botones[16].grid(row=5,column=0,columnspan=4,pady=2,ipady=10,ipadx=50)
        
        #Asociamos el teclado para poder usarlo
        ventana.bind("1",self.key1)
        ventana.bind("2",self.key2)
        ventana.bind("3",self.key3)
        ventana.bind("4",self.key4)
        ventana.bind("5",self.key5)
        ventana.bind("6",self.key6)
        ventana.bind("7",self.key7)
        ventana.bind("8",self.key8)
        ventana.bind("9",self.key9)
        ventana.bind("0",self.key0)
        ventana.bind(".",self.keyComa)
        ventana.bind("/",self.keyDiv)
        ventana.bind("*",self.keyMulti)
        ventana.bind("-",self.keyRest)
        ventana.bind("+",self.keySum)
        ventana.bind("<Return>",self.keyEnter)
        ventana.bind("<BackSpace>",self.keyDel)
         
    #Definimos los métodos para esas teclas (Pendiente mejorar)
    def key1(self,_event=None):
            self.clickar(1, escribir=True)
             
    def key2(self,_event=None):
            self.clickar(2, escribir=True)
             
    def key3(self,_event=None):
            self.clickar(3, escribir=True)        
     
    def key4(self,_event=None):
            self.clickar(4, escribir=True)
     
    def key5(self,_event=None):
        self.clickar(5, escribir=True)        
     
    def key6(self,_event=None):
            self.clickar(6, escribir=True)
         
    def key7(self,_event=None):
        self.clickar(7, escribir=True)
         
    def key8(self,_event=None):
        self.clickar(8, escribir=True)
     
    def key9(self,_event=None):
        self.clickar(9, escribir=True)
     
    def key0(self,_event=None):
        self.clickar(0, escribir=True)
     
    def keyComa(self,_event=None):
        self.clickar(",", escribir=True)
     
    def keyDiv(self,_event=None):
            self.clickar("/", escribir=True)
      
    def keyMulti(self,_event=None):
            self.clickar("*", escribir=True)
     
    def keyRest(self,_event=None):
            self.clickar("-", escribir=True)
     
    def keySum(self,_event=None):
            self.clickar("+", escribir=True)
 
    def keyEnter(self,_event=None):
            self.clickar("=", escribir=False)
                          
    def keyDel(self,_event=None):
            self.clickar("Del",escribir=False)
            
    #Fin de los métodos para el teclado
     
    #Definimos un módulo para generar los diferentes botones
    def boton(self,valor,escribir=True,ancho=9,alto=1,size=12):
        #Devolverá todo el código del botón
        return Button(self.ventana,
                      text=valor,
                      width=ancho,
                      height=alto,
                      font=("Arial",size),
                      background="lightBlue",
                      command=lambda:self.clickar(valor,escribir))
        
    #Definimos lo que pasará cada vez que se haga click en un botón
    def clickar(self,texto,escribir):
            #Si escribir es False
            if not escribir:
                #Si se ha pulsado resolver y hay algo que resolver
                if texto=="=" and self.operacion!="":
                    #Cambiamos la coma por el punto para que se pueda resolver
                    self.operacion=self.operacion.replace("x","*")
                    self.operacion=self.operacion.replace(",",".")
                    resultado=str(eval(self.operacion))
                    #Cambiamos el punto por la coma para mostrarlo
                    resultado=resultado.replace(".",",")
                    self.operacion=""
                    self.limpiar()
                    self.mostrar(resultado)
                elif texto=="Del":
                    self.operacion=""
                    self.limpiar()
            #Si escribir es True
            else:
                #Acumulamos lo que se está tecleando
                self.operacion+=str(texto)
                #Lo mostramos
                self.mostrar(texto)
    
    #Este método limpia la pantalla, primero se habilita, se borra y se vuelve
    #a deshabilitar
    def limpiar(self):
        self.visor.configure(state="normal")
        self.visor.delete("0.0", END)
        self.visor.configure(state="disabled")
        
    #Con este método mostramos en el visor lo que hayamos pulsado. Igual que con
    #limpiar: habilitamos, mostramos y deshabilitamos de nuevo el visor
    def mostrar(self, valor):
        self.visor.configure(state="normal")
        self.visor.insert(END, valor)
        self.visor.configure(state="disabled")    
        
