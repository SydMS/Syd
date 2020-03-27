'''
Created on 26 mar. 2020

@author: Sidney

Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura, y después las 
muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde 
<asignatura> es cada una des las asignaturas de la lista y <nota> cada una de
las correspondientes notas introducidas por el usuario.

'''

asignaturas = ["Matemáticas","Física","Química","Historia","Lengua","Filosofía"]
notas = []
indice = 0

#Pedimos la nota para cada una de las asignaturas y las guardamos en otra lista
for a in asignaturas:
    nota = input("Introduce tu nota en " + asignaturas[indice] + ": ")
    notas.append(nota)
    indice += 1

#Reiniciamos la variable
indice = 0
#Recorremos la lista de asignaturas y la mostramos con su correspondiente nota 
for a in asignaturas:
    print("Tu nota en " + asignaturas[indice] + " es de " + notas[indice] + "/10.")
    indice +=1
    