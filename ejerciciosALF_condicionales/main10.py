'''
Created on 20 mar. 2020

@author: Sidney

La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.


Escribir un programa que pregunte al usuario si quiere una pizza vegetariana 
o no, y en función de su respuesta le muestre un menú con los ingredientes
disponibles para que elija. Solo se puede eligir un ingrediente además de la
mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar
por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

http://aprendeconalf.es/python/ejercicios/condicionales.html
'''

menu = input("¿Vegetariano? (S/N) ")
base = "Mozarella , tomate"

if menu.lower() == "s":
    menu = "vegetariano"
    ing = int(input("Elige uno de estos ingredientes: Pimiento(1) o tofu(2): "))
    if ing == 1:
        plus = "pimiento"
    else:
        plus = "tofu"
else:
    menu = "no vegetariano"
    ing = int(input("Elige uno de estos ingredientes: Peperoni(1), jamón(2) o salmón(3)"))
    if ing == 1:
        plus = "peperoni"
    elif ing == 2:
        plus = "jamón"
    else:
        plus = "salmón"
        
print("Has elegido el menú " + menu + " con estos ingredientes: " + base + " y " + plus)