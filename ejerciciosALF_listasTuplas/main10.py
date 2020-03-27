'''
Created on 26 mar. 2020

@author: Sidney

Escribir un programa que almacene en una lista los siguientes precios:
50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y
el mayor de los precios.

'''

precios = [50,75,46,22,80,65,8]

#Guardamos el valor máximo y el mínimo
maximo = max(precios)
minimo = min(precios)

print("De los precios " + str(precios) + ". El mayor es " + str(maximo) +
      " y el menor " + str(minimo) + ".")