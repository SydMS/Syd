'''
Created on 20 mar. 2020

@author: Sidney

Los tramos impositivos para la declaración de la renta en un determinado país
son los siguientes:

Renta                Tipo impositivo
Menos de 10000€            5%
Entre 10000€ y 20000€      15%
Entre 200000€ y 35000€     20%
Entre 350000€ y 60000€     30%
Más de 60000€              45%

Escribir un programa que pregunte al usuario su renta anual y muestre por
pantalla el tipo impositivo que le corresponde.

http://aprendeconalf.es/python/ejercicios/condicionales.html

'''

renta = float(input("Introduce tu renta anual: "))

if renta > 60000:
    print("Tipo impositivo: 45%")
elif renta > 35000 and renta <= 60000:
    print("Tipo impositivo: 30%")
elif renta > 20000 and renta <= 35000:
    print("Tipo impositivo: 20%")
elif renta > 10000 and renta <= 20000:
    print("Tipo impositivo: 15%")
else:
    print("Tipo impositivo: 5%")