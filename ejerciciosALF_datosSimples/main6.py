'''
Created on 20 mar. 2020

@author: Sidney

Escribir un programa que pida al usuario su peso (en kg) y 
estatura (en metros), calcule el índice de masa corporal y
lo almacene en una variable, y muestre por pantalla la frase:
"Tu índice de masa corporal es <imc>" donde <imc> es el índice
de masa corporal calculado redondeado con dos decimales.
'''

weigth = input("Introduce tu peso (kilos): ")
height = input("Introduce tu altura (metros): ")

imc = float(weigth) / float (height)

print("Tu índice de masa corporal es " + str(round(imc,2)))