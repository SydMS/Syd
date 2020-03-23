'''
Created on 21 mar. 2020

@author: Sidney

Escribir un programa que acceda a un fichero de internet mediante su url
y muestre por pantalla el número de palabras que contiene.

http://aprendeconalf.es/python/ejercicios/ficheros.html

'''
from urllib import request

f = request.urlopen("https://colab.research.google.com/github/asalber/asalber.github.io/blob/master/python/ejercicios/soluciones/ficheros/ejercicio4.ipynb")

numero = len(f.read().split())
print(numero)