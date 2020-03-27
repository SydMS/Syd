'''
Created on 26 mar. 2020

@author: Sidney

Escribir un programa que almacene en una lista los números del 1 al 10 y
los muestre por pantalla en orden inverso separados por comas.

'''

num = []

#Cargamos la lista con los números necesarios
for i in range(1,11):
    num.append(i)

#Invertimos el orden en que está guardad
num.reverse()

#Mostramos la lista incluyendo la coma
for i in num:
    print(str(i), end=", ")