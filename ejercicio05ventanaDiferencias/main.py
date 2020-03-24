'''
Created on 17 mar. 2020

@author: Sidney Martín Siles

Ejercicio Diferencias
'''

#Ejemplo de un juego basado en un aplicación de ventanas con python Tkinter.
#Para mostrar un ejemplo sobre eventos y diferentes componentes visuales.

from tkinter import *
from tkinter import messagebox
import time
import os



#Declaro variables
listArchivo = None
listaCampos = []
x = 0 # Registrará el valor x
y = 0 # Registrará el valor y
num_dif = 0 # Registrará el número de aciertos
dif_list = [] #Validará si el acierto ya existe
t_respuesta = 0.0
nombreUsuario = None

#Abro el archivo
if os.path.isfile("log.txt"):
    #Genero la ventana para el listado
    listado = Tk()
    
    listado.title('Listado de participantes')
    
    archivo = open("log.txt","r")
    listArchivo = archivo.read().split(";")
    
    #Extraigo cada una de las partidas
    for l in listArchivo:
        listaCampos += l.split(",")
    #end for
    
    #Elimino el último valor, ya que se carga con un último elmento vacío
    listaCampos.pop()
    
    #Separo el usuario del tiempo
    num=0
    for i in listaCampos:
        if num%2:
            ind = listaCampos[num].index(":")
            nombre = listaCampos[num][ind+1:]
            Label(listado, text="Tiempo: " + nombre).pack()
            num += 1
        else:
            ind = listaCampos[num].index(":")
            tiempo = listaCampos[num][ind+1:]
            Label(listado, text="Usuario: " + tiempo).pack()
            num += 1
    #end for
    
    #Ejecuto la ventan
    listado.mainloop()
else:
    pass

#Función para recoger el nombre del usuario
def recoger_nombre():
    global nombreUsuario
    nombreUsuario = nombreEntrada.get()
    ventanaUsuario.destroy()
    return nombreUsuario
#end recoger_nombre

#Genero la ventana para introducir el nombre del usuario
ventanaUsuario = Tk()  
ventanaUsuario.geometry('300x150')  
ventanaUsuario.title('Introduce tu nombre')

#Genero el label
nombreLabel = Label(ventanaUsuario, text="Nombre")
nombreLabel.grid(row=0, column=0)

#Genero la entrada de texto
nombreEntrada = Entry(ventanaUsuario)
nombreEntrada.grid(row=0, column=1)

#Boton de aceptar
botonAceptar = Button(ventanaUsuario, text="Aceptar", command=recoger_nombre).grid(row=4, column=0)  

ventanaUsuario.mainloop()

#Función con la validación de diferencias
def click_raton(evento):
    
    #Recojo el tiempo en que se ejecuta
    tIni = time.time()
    
    #Hago globales las variables
    global x, y, num_dif, dif_list, nombreUsuario
    
    #Almaceno las coordenadas
    x = evento.x
    y = evento.y
        
#     print("x: " + str(x))
#     print("y: " + str(y))

    #Confirmo que el usuario ha pulsado correctamente
    if x >= 936 and x <= 985 and y >= 304 and y <= 350:
        if "a" not in dif_list:
            num_dif += 1
            dif_list += "a"
            messagebox.showinfo("Recuento diferencias", 
                                str(num_dif) + "º diferencia encontrada. Pendientes: "
                                + str(5-num_dif))
        else:
            messagebox.showinfo("Recuento diferencias","Diferencia ya encontrada.")    
    elif x >= 1167 and x <= 1215 and y >= 355 and y <= 389:
        if "b" not in dif_list:
            num_dif += 1
            dif_list += "b"
            messagebox.showinfo("Recuento diferencias", 
                                str(num_dif) + "º diferencia encontrada. Pendientes: "
                                + str(5-num_dif))
        else:
            messagebox.showinfo("Recuento diferencias","Diferencia ya encontrada.")
    elif x >= 938 and x <= 961 and y >= 195 and y <= 219:
        if "c" not in dif_list:
            num_dif += 1
            dif_list += "c"
            messagebox.showinfo("Recuento diferencias", 
                                str(num_dif) + "º diferencia encontrada. Pendientes: "
                                + str(5-num_dif))
        else:
            messagebox.showinfo("Recuento diferencias","Diferencia ya encontrada.")
    elif x >= 1416 and x <= 1445 and y >= 246 and y <= 275:
        if "d" not in dif_list:
            num_dif += 1
            dif_list += "d"
            messagebox.showinfo("Recuento diferencias", 
                                str(num_dif) + "º diferencia encontrada. Pendientes: "
                                + str(5-num_dif))
        else:
            messagebox.showinfo("Recuento diferencias","Diferencia ya encontrada.")
    elif x >= 1551 and x <= 1566 and y >= 265 and y <= 282:
        if "e" not in dif_list:
            num_dif += 1
            dif_list += "e"
            messagebox.showinfo("Recuento diferencias", 
                                str(num_dif) + "º diferencia encontrada. Pendientes: "
                                + str(5-num_dif))
        else:
            messagebox.showinfo("Recuento diferencias","Diferencia ya encontrada.")
    else:
        messagebox.showinfo("Recuento diferencias","Fallaste. " + str(5-num_dif) + 
                            " pendientes de encontrar.")
        
    if num_dif == 5:
        messagebox.showinfo("¡Ganador!", 
                            "¡Enhorabuena! Has encontrado todas las diferencias.")
        
        #Recojo el momento en que finaliza y se saca el tiempo final
        tFin = time.time()
        tRespuesta = tFin - tIni
        #Cierro ventana
        ventana.destroy()
        #Llamo a la función para que guarde los datos de la partida
        return grabar_log(tRespuesta,nombreUsuario)        
#end click_raton

#Función para grabar el fichero con los datos
def grabar_log(tRespuesta,nombreUsuario):
    fichero=open("log.txt","a")
    fichero.write("Nombre_usuario:" + str(nombreUsuario) +",Tiempo_respuesta:" + str(tRespuesta) + ";")
    fichero.close()
#end grabar_log

#Generao la ventana de las imagenes
ventana = Tk()

canvas = Canvas(ventana, width =800, height = 600)

#Cargo la imagen
imagen = PhotoImage(file="imagen.png")
canvas.create_image(0,0, image = imagen, anchor = NW)
canvas.pack(expand = YES, fill = BOTH)

#Se le da a ventana las proporciones (el doble de la imagen)
ventana.geometry("1600x600")

ventana.title("Busca las diferencias.")
#Muestro las instrucciones
messagebox.showinfo(title="Instrucciones", message="""
Bienvenido, usuario.

Debes encontrar las 5 diferencias entre estas dos imágenes
pulsando en la imagen de la derecha
""")


ventana.bind("<Button 1>",click_raton)
#Le damos a la ventana una función para que se ejecute al clickar
#Button 1 es el click izquierdo del ratón
ventana.mainloop()
