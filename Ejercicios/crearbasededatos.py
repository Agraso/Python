import sqlite3

#----------------CREACION DE COLUMNAS-------------------

# conexion = sqlite3.connect("basededatos1.db")

# cursor = conexion.cursor()

# cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")

# conexion.commit()

# conexion.close()

# ------------------------------------------------------


#-----------------------INSERTAR FILA---------------

# conexion = sqlite3.connect("basededatos1.db")

# cursor = conexion.cursor()

# cursor.execute("INSERT INTO PERSONAS VALUES('Antonio', 'Perez','Gomez',35)")

# conexion.commit()

# conexion.close()

#-------------------------------------------------------


#----------------INSERTAR VARIAS LINEAS-----------------

# conexion = sqlite3.connect("basededatos1.db")

# cursor = conexion.cursor()

# lista_personas = [ ('Pedro','Rodriguez','Perez',26),
#                    ('Maria', 'Lopez', 'Gomez', 45),
#                    ('Luis', 'Gonzales', 'Aumente',57) ]

# cursor.executemany("INSERT INTO PERSONAS VALUES(?,?,?,?)", lista_personas)

# conexion.commit()

# conexion.close()

#-------------------------------------------------------

#---------------------CONSULTAR------------------------

# conexion = sqlite3.connect("basededatos1.db")

# cursor = conexion.cursor()

# cursor.execute("SELECT * FROM PERSONAS")

# personas = cursor.fetchall()

# for personas in personas:
#     print(personas)
    
# conexion.close()

#------------------------------------------------------ 


#-------------CONSULTAR SEGUN CRITERIOS-----------------

# conexion = sqlite3.connect("basededatos1.db")

# cursor = conexion.cursor()

# cursor.execute("SELECT * FROM PERSONAS WHERE edad > 40")

# personas = cursor.fetchall()

# for personas in personas:
#     print(personas)
    
# conexion.close()

#-------------------------------------------------------

#----------CONSULTAR Y ORDENAR SEGUN CRITERIOS----------

# conexion = sqlite3.connect("basededatos1.db")

# cursor = conexion.cursor()

# cursor.execute("SELECT * FROM PERSONAS ORDER BY edad ")

# personas = cursor.fetchall()

# for personas in personas:
#     print(personas)
    
# conexion.close()

#-------------------------------------------------------


#---------------BORRAR DATOS DE LA TABLA----------------

# conexion = sqlite3.connect("basededatos1.db")

# cursor = conexion.cursor()

# cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'Luis'")

# conexion.commit()
    
# conexion.close()

#-------------------------------------------------------


#-------------------ACTUALIZAR DATOS--------------------

# conexion = sqlite3.connect("basededatos1.db")

# cursor = conexion.cursor()

# cursor.execute("UPDATE PERSONAS SET edad = 30 WHERE nombre = 'Antonio'")

# conexion.commit()
    
# conexion.close()

#-------------------------------------------------------