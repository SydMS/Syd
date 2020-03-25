'''
Created on 21 mar. 2020

@author: Sidney

Escribir un programa que muestre el eco de todo lo que el usuario introduzca
hasta que el usuario escriba “salir” que terminará.

http://aprendeconalf.es/python/ejercicios/bucles.html

'''



salir = False

while not salir:
    palabra = input("Introduce una palabra: ")
    if palabra.lower() == "salir":
        salir = True
    else:
        print(palabra)