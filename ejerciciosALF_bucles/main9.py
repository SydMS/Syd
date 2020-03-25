'''
Created on 21 mar. 2020

@author: Sidney

Escribir un programa que pida al usuario un número entero y 
muestre por pantalla si es un número primo o no.

http://aprendeconalf.es/python/ejercicios/bucles.html

'''
num = int(input("Introduce un número: "))
i = 2

while num % i != 0:
    i +=1
    
if num == i:
    print("El número es primo.")
else:
    print("El número no es primo.")