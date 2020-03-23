'''
Created on 20 mar. 2020

@author: Sidney

Escribir un programa que pregunte al usuario su edad 
y muestre por pantalla si es mayor de edad o no.

http://aprendeconalf.es/python/ejercicios/condicionales.html

'''

edad = int(input("Introduce tu edad: "))

if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")