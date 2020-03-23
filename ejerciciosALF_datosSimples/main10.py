'''
Created on 20 mar. 2020

@author: Sidney

Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la empresa de logística les cobra por peso de 
cada paquete así que deben calcular el peso de los payasos y muñecas que 
saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
Escribir un programa que lea el número de payasos y muñecas vendidos en el 
último pedido y calcule el peso total del paquete que será enviado.

http://aprendeconalf.es/python/ejercicios/tipos-datos.html

'''

clown = 112
doll = 75

c_vend = int(input("Número de payasos vendidos: "))
d_vend = int(input("Número de muñecas vendidas: "))

peso_total = (c_vend * clown) + (d_vend * doll)

print("El peso total del pequete será de " + str(peso_total) + " gramos.")