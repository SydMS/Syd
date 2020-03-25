'''
Created on 21 mar. 2020

@author: Sidney

Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo,
de altura el número introducido.

http://aprendeconalf.es/python/ejercicios/bucles.html

'''

n = abs(int(input("Introduce la altura del triángulo: ")))

for altura in range(1, n*2, 2):
    for base in range(altura, 0, -2):
        print(base, end=" ")
    print("")