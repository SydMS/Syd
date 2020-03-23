'''
Created on 20 mar. 2020

@author: Sidney

Escribir un programa para una empresa que tiene salas de juegos para 
todas las edades y quiere calcular de forma automática el precio que 
debe cobrar a sus clientes por entrar. El programa debe preguntar al 
usuario la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años puede entrar gratis, si tiene 
entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

http://aprendeconalf.es/python/ejercicios/condicionales.html

'''

edad = int(input("¿Qué edad tienes? "))

if edad < 4:
    print("Entrada gratuita.")
elif edad <= 18:
    print("Entrada 5€")
else:
    print("Entrada 10€")