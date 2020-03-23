'''
Created on 21 mar. 2020

@author: Sidney

Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

http://aprendeconalf.es/python/ejercicios/bucles.html

'''

a = 1
b = 1

while a <= 10:    
    while b <= 10:
        print(str(a) + " x " + str(b) + " = " + str(a*b))
        b += 1
    b = 1
    a += 1