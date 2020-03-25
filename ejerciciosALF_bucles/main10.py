'''
Created on 21 mar. 2020

@author: Sidney

Escribir un programa que pida al usuario una palabra y luego muestre
por pantalla una a una las letras de la palabra introducida empezando
por la última.

http://aprendeconalf.es/python/ejercicios/bucles.html

'''

a = input("Introduce una palabra: ")

for i in reversed(a):
    print(i)