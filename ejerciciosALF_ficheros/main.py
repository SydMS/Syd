'''
Created on 21 mar. 2020

@author: Sidney

Escribir una función que pida un número entero entre 1 y 10
y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar
de ese número, donde n es el número introducido.

http://aprendeconalf.es/python/ejercicios/ficheros.html

'''


num = int(input("Introduce un número entre 1 y 10: "))
f = open("tabla-"+str(num)+".txt","w")
for i in range(1,11):
    f.write(str(i)+" x "+str(num)+" = "+str((i*num))+"\n")
f.close()