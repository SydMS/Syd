'''
Created on 2 abr. 2020

@author: Sidney

Clases de elemento que usaremos

'''

class Artista_Banda():
    def __init__(self):
        self.nombre = ""
        self.pais = ""
    #end __init__
#end Artista_Banda

class Album():
    def __init__(self):
        self.banda = ""
        self.nombre_disco = ""
        self.genero = ""
        self.num_pistas = 0
        self.year = ""
    #end __init__
#end Album
        
class Genero():
    def __init__(self):
        self.nombre = ""
    #end __init__
#end Genero
        