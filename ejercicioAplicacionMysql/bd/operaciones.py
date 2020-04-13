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

def Obtener_ID_Album(id_artista,nombre):
    #Cargamos en la variable la sentencia sql
    sql = sentencias_sql.SQL_OBTENER_ID_ALBUM
    #Cargamos en la variable la conexión a la bd
    mydb = Conectar()
    #Creamos un cursor de la bd
    cursor = mydb.cursor()
    #Cargamos los valores dentro de una tupla
    valores = (id_artista,nombre)
        
    cursor.execute(sql,valores)
    #El resultado de la consulta lo almacenamos en una varible en forma de array
    id_disco = cursor.fetchall()
    mydb.disconnect()
    #Tratamos el resultado para modificar el formato tupla y la ","
    id_disco = str(id_disco[0])
    id_disco = id_disco[1:id_disco.index(",")]
    #Devolvemos la variable para mostrarla
    return id_disco
#end Obtener_ID_Album

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

def Modificar_Banda(nueva_banda,id_banda):
    #Cargamos la sentencia sql en una variable
    sql = sentencias_sql.SQL_MODIFICAR_BANDA
    #Cargamos también la conexión a nuestra bd
    mydb = Conectar()
    #Creamos un cursor
    cursor = mydb.cursor()
    #Almacenamos los valores para la sentencia
    valor = (nueva_banda.nombre,nueva_banda.pais,id_banda)
    #Ejecutamos la sentencia con los valores
    cursor.execute(sql,valor)
    
    mydb.commit()
    mydb.disconnect()
    
def Eliminar_Banda(id_banda):
    #En este caso necesitaremos dos sentencias, puesto que al borrar la banda
    #también se borrarán sus discos
    sql1 = sentencias_sql.SQL_ELIMINAR_DISCOS_POR_BANDA
    sql2 = sentencias_sql.SQL_ELIMINAR_BANDA
    
    mydb = Conectar()
    #Creamos un cursor
    cursor = mydb.cursor()
    #Almacenamos en una tupla el valor del id de la banda
    valor = (id_banda,)
    #Ejecutamos las sentencias con el id de la banda
    cursor.execute(sql1,valor)
    cursor.execute(sql2,valor)
    
    mydb.commit()
    mydb.disconnect()
    
def Modificar_Album(disco,id_disco):
    #Almacenamos la sentencia sql
    sql = sentencias_sql.SQL_MODIFICAR_DISCO
    #Almacenamos la conexión a la bd
    mydb = Conectar()
    #Creamos un cursor
    cursor = mydb.cursor()
    #Almacenamos los valores que necesitaremos
    valor = (disco.banda,disco.genero,disco.nombre_disco,disco.num_pistas,disco.year,id_disco)
    
    #Ejecutamos la sentencia con los valores
    cursor.execute(sql,valor)
    
    mydb.commit()
    mydb.disconnect()
    
def Eliminar_Disco(id_album):
    #Almacenamos la sentencia sql
    sql = sentencias_sql.SQL_ELIMINAR_DISCO
    #Almacenamos la conexión a la bd
    mydb = Conectar()
    #Creamos un cursor
    cursor = mydb.cursor()
    #Almacenamos el valor del ID del album
    valor = (id_album,)
    #Ejecutamos la sentencia con los valores
    cursor.execute(sql,valor)
    
    mydb.commit()
    mydb.disconnect()