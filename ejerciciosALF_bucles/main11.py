'''
Created on 21 mar. 2020

@author: Sidney

Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.

http://aprendeconalf.es/python/ejercicios/bucles.html

'''

a = input("Introduce una frase: ")
letra = input("¿Qué letra quieres contabilizar? ")

contador = 0
for i in a:
    if i == letra:
        contador += 1

print(contador)