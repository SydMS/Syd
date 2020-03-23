'''
Created on 21 mar. 2020

@author: Sidney


Escribir un programa que pregunte al usuario su edad y muestre por pantalla
todos los años que ha cumplido (desde 1 hasta su edad).

http://aprendeconalf.es/python/ejercicios/bucles.html

'''

edad = int(input("Introduce tu edad: "))
a = 1

while edad >= a:
    print(a)
    a += 1