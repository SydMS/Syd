'''
Created on 21 mar. 2020

@author: Sidney 


Escribe un programa que pida dos palabras y diga si riman o no.
Si coinciden las tres últimas letras tiene que decir que riman.
Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no,
que no riman.

http://www.pythondiario.com/2013/06/ejercicios-en-python-parte-3.html
'''

def rimando(poesia):
    poesia = poesia.split(sep=" ")
    aciertos = 0
    if poesia[0][-1] == poesia[1][-1]:
        aciertos += 1
        if poesia[0][-2] == poesia[1][-2]:
            aciertos += 1
            if poesia[0][-3] == poesia[1][-3]:
                aciertos += 1
            else:
                pass
        else:
            pass
    else:
        print("no way.")
        
    if aciertos == 3:
        print("Tenemos aquí a Becquer.")
    elif aciertos == 2:
        print("Dale una vuelta a eso, estás cerca de conseguirlo.")
    else:
        print("Dedícate a otra cosa.")
            
poesia = input("Introduce dos palabras (separadas por un espacio): ")

try:
    rimando(poesia)
except IndexError:
    print("Debe introducir dos palabras.")