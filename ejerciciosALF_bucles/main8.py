'''
Created on 21 mar. 2020

@author: Sidney

Escribir un programa que almacene la cadena de caracteres contraseña
en una variable, pregunte al usuario por la contraseña hasta que introduzca
la contraseña correcta.

http://aprendeconalf.es/python/ejercicios/bucles.html

'''
pw_ini = "PassWord"

pw_usu = ""

while not pw_ini == pw_usu:
    pw_usu = input("Introduce la contraseña: ")    

print("Contraseña correcta.")