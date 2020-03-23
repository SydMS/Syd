'''
Created on 21 mar. 2020

@author: Sidney


Escribir un programa que pida al usuario un número entero positivo
y muestre por pantalla todos los números impares desde 1 hasta ese
número separados por comas.

http://aprendeconalf.es/python/ejercicios/bucles.html

'''

num = abs(int(input("Introduce un número: ")))
listado = None
for a in range(1,num+1,2):
    print(a,end=",")