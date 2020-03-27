'''
Created on 26 mar. 2020

@author: Sidney

Escribir un programa que almacene el abecedario en una lista,
elimine de la lista las letras que ocupen posiciones múltiplos de 3,
y muestre por pantalla la lista resultante.

'''
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o',
              'p','q','r','s','t','v','w','y','z']

#El bucle recorrerá la lista desde el final hasta el principio
for i in range(len(abecedario),1,-1):
    #Si i es múltiplo de 3
    if i % 3 == 0:
        #Eliminamos el índice (i-1) de la lista
        abecedario.pop(i-1)
       
print(abecedario)

