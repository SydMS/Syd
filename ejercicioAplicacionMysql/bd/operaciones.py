'''
Created on 2 abr. 2020

@author: Sidney

Diferentes operaciones que se realizarán contra la bd

'''

import mysql.connector
from sentencias_sql import sentencias_sql

#Datos de conexión para la bd
def Conectar():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "bd_directorio_musical"        
    )
    return mydb
#end Conectar


def Insertar_Banda(banda):
    #Cargamos en la variable la sentencia sql
    sql = sentencias_sql.SQL_INSERCION_BANDA
    #Cargamos en la variable la conexión a la bd
    mydb = Conectar()
    #Creamos un cursor de la bd
    cursor = mydb.cursor()
    #Cargamos los valores dentro de una tupla
    valores = (banda.nombre,banda.pais)
    #El cursor ejecuta la sentencia y proporciona los valores para la sentencia
    cursor.execute(sql,valores)
    
    mydb.commit()
    mydb.disconnect()
#end Insertar_Banda
    
    
def Listar_Bandas():
    #Cargamos en la variable la sentencia sql
    sql = sentencias_sql.SQL_LISTADO_BANDAS
    #Cargamos en la variable la conexión a la bd
    mydb = Conectar()
    #Creamos un cursor de la bd
    cursor = mydb.cursor()
    cursor.execute(sql)
    #El resultado de la consulta lo almacenamos en una varible en forma de array
    listado = cursor.fetchall()
    mydb.disconnect()
    #Devolvemos la variable para mostrarla
    return listado
#end Listar_Bandas

def Insertar_Genero(genero):
    #Cargamos en la variable la sentencia sql
    sql = sentencias_sql.SQL_INSERCION_GENERO
    #Cargamos en la variable la conexión a la bd
    mydb = Conectar()
    #Creamos un cursor de la bd
    cursor = mydb.cursor()
    #Cargamos los valores dentro de una tupla
    valores = (genero.nombre,)
    #El cursor ejecuta la sentencia y proporciona los valores para la sentencia
    cursor.execute(sql,valores)
    
    mydb.commit()    
    mydb.disconnect()
#end Insertar_Genero
    
    
def Listar_Generos():
    #Cargamos en la variable la sentencia sql
    sql = sentencias_sql.SQL_LISTADO_GENEROS
    #Cargamos en la variable la conexión a la bd
    mydb = Conectar()
    #Creamos un cursor de la bd
    cursor = mydb.cursor()
    cursor.execute(sql)
    #El resultado de la consulta lo almacenamos en una varible en forma de array
    listado = cursor.fetchall()
    mydb.disconnect()
    #Devolvemos la variable para mostrarla
    return listado
#end Listar_Generos

def Insertar_Album(disco):
    #Cargamos en la variable la sentencia sql
    sql = sentencias_sql.SQL_INSERCION_ALBUM
    #Cargamos en la variable la conexión a la bd
    mydb = Conectar()
    #Creamos un cursor de la bd
    cursor = mydb.cursor()
    #Cargamos los valores dentro de una tupla
    valores = (disco.banda,disco.genero,disco.nombre_disco,disco.num_pistas,disco.year)
    #El cursor ejecuta la sentencia y proporciona los valores para la sentencia
    cursor.execute(sql,valores)
    
    mydb.commit()
    mydb.disconnect()
#end Insertar_Album
    
def Obtener_ID_Banda(disco):
    #Cargamos en la variable la sentencia sql
    sql = sentencias_sql.SQL_OBTENER_ID_BANDA
    #Cargamos en la variable la conexión a la bd
    mydb = Conectar()
    #Creamos un cursor de la bd
    cursor = mydb.cursor()
    #Cargamos los valores dentro de una tupla
    valores = (disco,)
        
    cursor.execute(sql,valores)
    #El resultado de la consulta lo almacenamos en una varible en forma de array
    banda = cursor.fetchall()
    mydb.disconnect()
    #Tratamos el resultado para modificar el formato tupla y la ","
    banda = str(banda[0])
    banda = banda[1:banda.index(",")]
    #Devolvemos la variable para mostrarla
    return banda
#end Obtener_ID_Banda

def Obtener_ID_Genero(genero):
    #Cargamos en la variable la sentencia sql
    sql = sentencias_sql.SQL_OBTENER_ID_GENERO
    #Cargamos en la variable la conexión a la bd
    mydb = Conectar()
    #Creamos un cursor de la bd
    cursor = mydb.cursor()
    #Cargamos los valores dentro de una tupla
    valores = (genero,)
        
    cursor.execute(sql,valores)
    #El resultado de la consulta lo almacenamos en una varible en forma de array
    genero = cursor.fetchall()
    mydb.disconnect()
    #Tratamos el resultado para modificar el formato tupla y la ","
    genero = str(genero[0])
    genero = genero[1:genero.index(",")]
    #Devolvemos la variable para mostrarla
    return genero
#end Obtener_ID_Genero

def Listar_Discos(banda):
    #Cargamos en la variable la sentencia sql
    sql = sentencias_sql.SQL_LISTADO_DISCOS
    #Cargamos en la variable la conexión a la bd
    mydb = Conectar()
    #Creamos un cursor de la bd
    cursor = mydb.cursor()
    #Creamos una variable con la banda que ha seleccionado el usuario
    valor = (banda,)
    
    cursor.execute(sql,valor)
    #El resultado de la consulta lo almacenamos en una varible en forma de array
    listado = cursor.fetchall()
    mydb.disconnect()
    #Devolvemos la variable para mostrarla
    return listado
#end Listar_Discos