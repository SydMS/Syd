'''
Created on 21 mar. 2020

@author: Sidney

Escribir una función que pida dos números n y m entre 1 y 10,
lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
y muestre por pantalla la línea m del fichero. Si el fichero no existe
debe mostrar un mensaje por pantalla informando de ello.

http://aprendeconalf.es/python/ejercicios/ficheros.html

'''

from os import path
#si importase * de os daría error el open porque hay que poner un integer

n = input("Introduce un número entre 1 y 10: ")
m = int(input("Introduce un segundo número entre 1 y 10: "))
archivo = "tabla-"+n+".txt"


if path.isfile("tabla-"+n+".txt"):
    f = open(archivo,"r")
    completo = f.readlines()
    f.close()
    print(completo[m])
else:
    print("El fichero no existe.")