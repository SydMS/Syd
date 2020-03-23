'''
Created on 21 mar. 2020

@author: Sidney

Ejercicio MasterMind http://www.pythondiario.com/2013/06/ejercicios-en-python-parte-3.html
'''

#Importo la librería necesaria
import random

#Declaro variable
bet = None

def generar_cadena(longitud):
    #Esta función generará una cadena en función de cuánta longitud quiera el usuario.
    cadena = []
    while len(cadena) < longitud:
        #Ejecuta el bucle hasta que tenga la longitud deseada
        for a in range(0,longitud-1):
            #a será el índice de nuestra lista
            b = random.randint(1,longitud)
            #b será el valor de elemento
            #Si el valor ya existe en la lista no se introducirá
            if b not in cadena:
                cadena.insert(a, b)
            else:
                continue 
            
    return cadena
#end generar_cadena
        
def comparador(cadena,bet):
    #Esta función comparará la cadena autogenerada con la introducida por el usu.
    
    #Declaramos un booleano para que se ejecute hasta que el usuario acierte.
    party = True
    while party:
        #Pedimos al usuario que introduzca su apuesta
        bet = input("Intenta adivinar la cadena: ")
        #Transforma la apuesta del usuario en una lista para poder comparar
        lista_bet = []
        i = 0
        for a in bet:
            lista_bet.insert(i,int(a))
            i += 1
    #end while
        
        #k será el índice en de las listas
        k = 0
        #Contador de aciertos del usuario
        aciertos = 0
        for j in range(0,len(cadena)):
            #Se ejecutará el bucle tantas veces como valores haya en el cadena
            if cadena[k] == lista_bet[k]:
                k += 1
                aciertos += 1
            else:
                k +=1
        #end for
        
        #Si el contador de aciertos llega a 4 felicitamos, en caso contrario
        #mostramos el número de aciertos y se ejecutrá el bucle  de nuevo.
        if aciertos == 4:
            print("Enhorabuena, has acertado.")
            party = False
        else:
            print("Lo sentimos, has obtenido " + str(aciertos) + " aciertos. Vuelve a intentarlo.")
#end comparador

longitud = int(input("Introduce la longitud de la cadena (1 a 9): "))
cadena = generar_cadena(longitud)

comparador(cadena, bet)
print("Fin del programa.")

