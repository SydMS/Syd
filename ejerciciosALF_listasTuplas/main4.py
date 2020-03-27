'''
Created on 26 mar. 2020

@author: Sidney

Escribir un programa que pregunte al usuario los números ganadores
de la lotería primitiva, los almacene en una lista
y los muestre por pantalla ordenados de menor a mayor.

'''

#Pedimos los números ganadores de la lotería
loteria = input("Introduce los números ganadores en la lotería: ")
num_ganadores = []

#Los guardamos en una lista, por separado y convirtiéndolos en enteros
for l in loteria.split(" "):
    num_ganadores.append(int(l))

#Ordenamos los números
num_ganadores.sort()


print(num_ganadores)

#Ordenando sin sort
#num_ganadores_ord = []
#
# for i in range(0,(len(num_ganadores))):
#     a = min(num_ganadores)
#     num_ganadores_ord.append(a)
#     num_ganadores.remove(a)
#     
# print(num_ganadores_ord)