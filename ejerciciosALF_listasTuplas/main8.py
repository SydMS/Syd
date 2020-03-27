'''
Created on 26 mar. 2020

@author: Sidney

Escribir un programa que pida al usuario una palabra y
muestre por pantalla si es un palíndromo.

'''

palabra = input("Introduzca una palabra: ")
lista_palabra = []
lista_palabra_rev = []

#Convertimos la palabra introducida en una lista y la almacenamos
lista_palabra = list(palabra)
#Cargamos una lista con los mismos valores que la otra
lista_palabra_rev = lista_palabra
#y les damos la vuelta
lista_palabra_rev.reverse()

#Comparamos ambas listas para ver si es un palíndromo
if lista_palabra == lista_palabra_rev:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
