'''
Created on 20 mar. 2020

@author: Sidney

Escribir un programa que almacene la cadena de caracteres contraseña
en una variable, pregunte al usuario por la contraseña e imprima 
por pantalla si la contraseña introducida por el usuario coincide 
con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

http://aprendeconalf.es/python/ejercicios/condicionales.html
'''

passw = "contraseña"

passw_int = input("Introduce la contraseña: ")

if passw == passw_int.lower():
    print("Correcta.")
else:
    print("Incorrecta.")