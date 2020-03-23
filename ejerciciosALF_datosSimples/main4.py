'''
Created on 20 mar. 2020

@author: Sidney

Escribir un programa que pregunte al usuario por el número de horas
trabajadas y el coste por hora. Después debe mostrar por pantalla 
la paga que le corresponde
'''

horas = input("¿Cuántas horas has trabajado? ")
coste = input("¿Cuál es el coste por hora? ")

print("Debes cobrar " + str(float(horas) * float(coste)) + " euros.")