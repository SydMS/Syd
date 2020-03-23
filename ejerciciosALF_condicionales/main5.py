'''
Created on 20 mar. 2020

@author: Sidney

Para tributar un determinado impuesto se debe ser mayor de 16 años
y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos 
mensuales y muestre por pantalla si el usuario tiene que tributar o no.

http://aprendeconalf.es/python/ejercicios/condicionales.html
'''

edad = int(input("Introduce tu edad: "))
sueldo = float(input("Introduce tu salario mensual: "))


if edad >= 16:
    if sueldo >= 1000:
        print("Tienes que tributar.")
    else:
        print("Tus ingresos son insuficientes. No tienes que tributar.")
else:
    print("No tienes edad para tributar.")
    
# if edad >= 16 and sueldo >= 1000:
#     print("Tienes que tributar.")
# else:
#     print(" No tienes que tributar.")