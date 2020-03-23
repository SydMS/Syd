'''
Created on 20 mar. 2020

@author: Sidney

Escribir un programa que lea un entero positivo, 𝑛, 
introducido por el usuario y después muestre en pantalla la suma de todos
los enteros desde 1 hasta 𝑛. La suma de los 𝑛 primeros enteros positivos 
puede ser calculada de la siguiente forma: suma=𝑛(𝑛+1)2
'''

num = int(input("Introduce un número: "))

suma = abs(num)*(abs(num) + 1)/2

print("Suma de los números positivos: ", suma)