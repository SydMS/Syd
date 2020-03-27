'''
Created on 26 mar. 2020

@author: Sidney

Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la 
lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla
las asignaturas que el usuario tiene que repetir.

'''

asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
aprobados = []
indice = 0

#Recorremos la lista de asignaturas
for a in asignaturas:
    #Solicitamos que se introduzca la nota y la almacenamos
    nota = int(input("Introduce la nota de la asignatura " + a + ": "))
    #Si aprueba, guardamos la asignatura
    if nota >= 5:
        aprobados.append(a)

#Eliminamos de la lista de asignaturas las que están aprobadas        
for a in aprobados:
    asignaturas.remove(a)
    
print("Debes repetir " + str(asignaturas))
    