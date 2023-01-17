import sqlite3

def conectar():
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS libros(Id INTEGER PRIMARY KEY, Titulo TEXT, Autor TEXT, Year INTEGER, ISBN INTEGER)")
    conexion.commit()
    conexion.close()
    
def insertar(titulo,autor,year,isbn):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO libros VALUES (NULL,?,?,?,?)",(titulo,autor,year,isbn))
    conexion.commit()
    conexion.close()
    
def visualizar():
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM libros')
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def buscar(titulo='',autor='',year=0,isbn=0):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM libros WHERE titulo=? OR autor=? OR year=? OR isbn=?',(titulo,autor,year,isbn))
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def borrar(Id):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE Id=?",(Id,))
    conexion.commit()
    conexion.close()
    
def actualizar(titulo,autor,year,isbn,Id):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE libros SET titulo=?, autor=?, year=?, isbn=? WHERE Id=?",(titulo,autor,year,isbn,Id))
    conexion.commit()
    conexion.close()
    
    
#Pruebas
conectar()
# insertar('Titulo1','Autor1',2001,111111111111111)
# insertar('Titulo2','Autor2',2002,222222222222222)
# insertar('Titulo3','Autor3',2003,3333333333333333)
# resultados = visualizar()
# for resultado in resultados:
#     print(resultado)

# resultados = buscar(year=2003)
# for resultado in resultados:
#     print(resultado)

# borrar(2)
# resultados = visualizar()
# for resultado in resultados:
#     print(resultado)

# actualizar(titulo='Titulo5',autor='Autor5',year=2005,isbn=5555555555,Id=3)
# resultados = visualizar()
# for resultado in resultados:
#     print(resultado)
