'''
Created on 20 mar. 2020

@author: Sidney 

Escribir un programa que pregunte el nombre del usuario en la consola
y un número entero e imprima por pantalla en líneas distintas
el nombre del usuario tantas veces como el número introducido.

http://aprendeconalf.es/python/ejercicios/tipos-datos.html
'''

nombre = input("Introduce tu nombre: ")
numero = int(input("Introduce un número entero: "))


while numero:
    print(nombre)
    numero -= 1