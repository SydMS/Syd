'''
Created on 21 mar. 2020

@author: Sidney

Puntuación: 
El jugador acumulará 50 puntos por cada victoria y perderá 75 por cada derrota.

http://www.pythondiario.com/2013/06/ejercicios-en-python-parte-3.html
'''

#Importo las librerías necesarias para el juego
import random
import time

#Declaro las variables
puntuacion = 0
inicio = 0

def cueva():
    #En esta función el jugador a qué cueva quiere entrar, devolviendo el número.
    
    num_cueva = ''
    while num_cueva != "1" and num_cueva != "2":
        num_cueva = input("¿A qué cueva quieres entrar? (Elige 1 o 2): ")
    return num_cueva

def juego_cueva(cueva):
    #Esta función es el juego en sí, al que le pasamos la cueva del usuario 
    #Primero hay una pequeña introducción.
    global puntuacion
    print("Te acercas a la cueva,")
    time.sleep(2)
    print("...está oscuro y el ambiente es tenebroso.")
    time.sleep(2)
    print("De repente, un gran dragón salta delante de ti, abre su boca y...")
    print("")
    time.sleep(2)
    
    #Se genera y guarda el número que será la cueva con el dragón amable.
    cueva_buena = random.randint (1, 2)
    
    #Si el número generado coincide con el número introducido por el usuario...
    if juego_cueva == str(cueva_buena):
        print ("Te entrega su tesoro.")
        #y además se le otorgan 50 puntos
        puntuacion += 50
    else:
        print ("El dragon te come de un bocado.")
        #si no coinciden, se le quitarán 75
        puntuacion -= 75
        
#Para que se ejecute el while, por defecto le damos valor sí.
empezarNuevo = "si"

#Si el jugador decide no jugar, no se ejecturá todo lo que está a continuación.
while empezarNuevo.lower() == ("s") or empezarNuevo.lower() == ("si"):
    #Mostramos la introducción del juego sólo cuando es la priemra vez.
    if inicio == 0:
        print("Estamos en una tierra llena de dragones. Delante nuestro hay dos cuevas.")
        print("En una de las cuevas, vive un dragon amable y compartirá su tesoro.")
        print("En la otra cueva, vive un dragón más malo que un dolor, no esperes")
        print("que te lo ponga fácil para poder conseguir su tesoro.\n")
        #Cambiamos la variable para no volver a mostra la intro.
        inicio = 1
    #Llamamos la función cueva, que devolverá el número seleccionado por el 
    #usuario y lo cargará en la variable
    num_cueva = cueva()
    #Le pasamos la variable a la función del juego
    juego_cueva(num_cueva)
    #Una vez finalizado el juego, se mostrará estos mensajes que, si el usuario
    #no tiene puntuación positiva no se mostrará, donde el usuario puede decidir
    #continuar jugando
    if puntuacion <= 0:
        empezarNuevo = input("Quieres jugar de nuevo? (si o no): ")
        puntuacion = 0
    else:
        empezarNuevo = input("Quieres jugar de nuevo? Tú actual puntuación es de " + str(puntuacion) + " (si o no): ")
    