'''
Created on 26 mar. 2020

@author: Sidney

Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) 
en dos listas y muestre por pantalla su producto escalar.

'''

tupla1 = (1,2,3)
tupla2 = (-1,0,2)

resultado = 0

#Para cada uno de los elmentos de la tupla1
for i in range(len(tupla1)):
        #La variable resultado almacenará el producto del elemento tupla1 x elemento tupla2
        resultado += tupla1[i]*tupla2[i] 
        
print("El resultado de multiplicar la tupla " + str(tupla1) + " por la tupla " +
      str(tupla2) + " es " + str(resultado))