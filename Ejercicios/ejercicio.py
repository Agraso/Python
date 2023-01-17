import sqlite3

# conexion = sqlite3.connect("basededatos.db")

# cursor= conexion.cursor()

# cursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER, Nombre TEXT, Precio INTEGER)")

# conexion.commit()
# conexion.close()

# conexion = sqlite3.connect("basededatos.db")

# cursor = conexion.cursor()

# Lista_productos = [ (1,'Impresora',300),
#                     (2, 'Raton', 20),
#                     (3, 'Ordenador', 600) ]

# cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",Lista_productos)

# conexion.commit()

# conexion.close()

conexion = sqlite3.connect("basededatos.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PRODUCTOS")

productos = cursor.fetchall()

for producto in productos:
    print(producto)
    
conexion.close()
    