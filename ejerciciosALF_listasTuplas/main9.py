'''
Created on 26 mar. 2020

@author: Sidney

Escribir un programa que pida al usuario una palabra y 
muestre por pantalla el número de veces que contiene cada vocal.

'''

palabra = input("Introduce un palabra: ")
vocales = ("a","e","i","o","u")


#Para cada una de las vocales
for vocal in vocales:
    #Almacenaremos cuántas veces aparece y lo reseteamos para cada vocal
    veces = 0
    #Recorre las letras de la palabra introducida y se compara con la vocal
    for letra in palabra:
        if letra.lower() == vocal:
            veces += 1
    print("Tu palabra contiene " + str(veces) + " " + vocal + "'s.")
