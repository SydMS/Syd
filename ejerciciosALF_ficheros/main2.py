'''
Created on 21 mar. 2020

@author: Sidney

Escribir una función que pida un número entero entre 1 y 10,
lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
done n es el número introducido, y la muestre por pantalla.
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

http://aprendeconalf.es/python/ejercicios/ficheros.html

'''

from os import path
#si importase * de os daría error el open porque hay que poner un integer

num = input("Introduce un número entre 1 y 10: ")
archivo = "tabla-"+num+".txt"


if path.isfile("tabla-"+num+".txt"):
    f = open(archivo,"r")
    print (f.read())
    f.close()
else:
    print("El fichero no existe.")