'''
Created on 20 mar. 2020

@author: Sidney

Escribir un programa que pregunte el nombre del usuario en la consola y después
de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de
letras que tienen el nombre.

http://aprendeconalf.es/python/ejercicios/tipos-datos.html

'''

nombre = input("Introduce tu nombre: ")

print("El nombre ", nombre.upper(), " tiene ",len(nombre), " letras.")