'''
Created on 2 abr. 2020

@author: Sidney

Sentencias SQL para la aplicación Directorio Musical creada con QtDesigner

'''

SQL_INSERCION_BANDA = """INSERT INTO tbl_artistas_bandas (nombre, pais_procedencia)
                         VALUES (%s, %s);"""

SQL_INSERCION_ALBUM = """INSERT INTO tbl_album (id_artista,id_genero,nombre,num_pistas,year)
                         VALUES (%s, %s, %s, %s, %s);"""

SQL_INSERCION_GENERO = "INSERT INTO tbl_genero (nom_genero) VALUES (%s);"


SQL_LISTADO_BANDAS = """SELECT nombre, pais_procedencia FROM tbl_artistas_bandas
                        ORDER BY nombre;"""

SQL_LISTADO_GENEROS = "SELECT nom_genero FROM tbl_genero ORDER BY nom_genero;"


SQL_LISTADO_DISCOS = """SELECT a.nombre, a.num_pistas, a.year, b.nom_genero
                         FROM tbl_album a INNER JOIN tbl_genero b 
                         WHERE a.id_artista = %s AND a.id_genero = b.id_genero 
                         ORDER BY a.year"""

SQL_OBTENER_ID_BANDA = """SELECT id_artista_banda FROM tbl_artistas_bandas
                          WHERE nombre = %s"""

SQL_OBTENER_ID_GENERO = "SELECT id_genero FROM tbl_genero WHERE nom_genero = %s"

