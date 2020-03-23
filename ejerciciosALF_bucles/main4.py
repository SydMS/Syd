'''
Created on 21 mar. 2020

@author: Sidney


Escribir un programa que pida al usuario un número entero positivo
y muestre por pantalla la cuenta atrás desde ese número hasta cero 
separados por comas.

http://aprendeconalf.es/python/ejercicios/bucles.html

'''

num = abs(int(input("Introduce un número: ")))

a = 0

while num >= a:
    print(str(num),end=',')
    num -= 1