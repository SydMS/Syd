'''
Created on 21 mar. 2020

@author: Sidney


Escribir un programa que pida al usuario un número entero y
muestre por pantalla un triángulo rectángulo como el de más abajo,
de altura el número introducido.

http://aprendeconalf.es/python/ejercicios/bucles.html

'''

num = abs(int(input("¿Introduce un número?: ")))

aste = "*"

for a in range(1,num+1):
    print(aste*a)