'''
Created on 20 mar. 2020

@author: Sidney

Escribir un programa que pida al usuario dos números enteros y
muestre por pantalla la <n> entre <m> da un cociente <c> y 
un resto <r> donde <n> y <m> son los números introducidos por el usuario,
y <c> y <r> son el cociente y el resto de la división entera respectivamente.

'''

n = input("Introduce el primer número: ")
m = input("Introduce el segundo número: ")

r = int(n) % int (m)
c = int(n) // int(m)

print(n + " entre " + m + " da un cociente de " + str(c) + " y un resto de " + str(r))