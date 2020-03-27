'''
Created on 26 mar. 2020

@author: Sidney

Escribir un programa que pregunte por una muestra de números,
separados por comas, los guarde en una lista y muestre por pantalla 
su media y desviación típica.

'''
sum_cuad = 0.0

#Solicitamos los números necesarios 
num = input("Introduce los números que quieras (separados por coma): ")

#Los separamos usando la ,
num = num.split(",")

#Convertimos cada número de string a float
for i in range(len(num)):
    num[i] = float(num[i])

#Calculamos la media
media = sum(num) / len(num)

print("La media de los número es: " + str(media))

#Calculamos la suma de los cuadrados
for i in num:
    sum_cuad += i**2

#Calculamos la desviación
desviacion = (sum_cuad/len(num)-(sum(num)/len(num))**2)**(1/2)

print("La desviación típica de los números es: " + str(round(desviacion,2)))