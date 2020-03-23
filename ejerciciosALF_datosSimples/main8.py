'''
Created on 20 mar. 2020

@author: Sidney

Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión.

'''

money = float(input("¿Cuánto quieres invertir? "))
interes = float(input("¿Cuál es el interés? "))
year = int(input("¿Cuántos años? "))

capital = round(money * (interes / 100+1) ** year,2)

print("Capital final: " + str(capital))