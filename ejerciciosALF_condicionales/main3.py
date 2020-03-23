'''
Created on 20 mar. 2020

@author: Sidney

Escribir un programa que pida al usuario dos números y muestre por 
pantalla su división. Si el divisor es cero el programa debe mostrar un error.

http://aprendeconalf.es/python/ejercicios/condicionales.html

'''

num1 = float(input("Introduce el primer dividendo: "))
num2 = float(input("Introduce el segundo divisor: "))

if num2 == 0:
    print("El divisor no debe ser 0.")
else:
    print(num1/num2)