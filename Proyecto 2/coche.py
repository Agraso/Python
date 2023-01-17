import sys
from zipfile import ZipFile
import pandas as pd
import sqlite3
from sqlite3 import Error
from os import remove

basededatos = 'coches.bd'


def descomprimir_fichero(nombre):
    with ZipFile(nombre,'r') as zip:
        zip.extractall()
        
def leer_datos(nombre):
    datos = pd.read_csv(nombre, sep=';')
    return datos

def crear_conexion_bd():
    try:
        conexion = sqlite3.connect(basededatos)
        return conexion
    except:
        print(Error)
        
def borrar_datos():
    try:
        remove(basededatos)
    except FileNotFoundError:
        pass
        
def crear_tabla_coches(conexion):
    cursor = conexion.cursor()
    cursor.execute('CREATE TABLE coches (Marca TEXT, Modelo TEXT, Combustible TEXT, Transmision TEXT, Estado TEXT, Matriculacion TEXT, Kilometraje INTEGER, Potencia REAL, Precio REAL)')
    conexion.commit()
    
    
def grabar_coches(conexion, datos):
    for fila in datos.itertuples():
        Marca = fila[1]
        Modelo = fila[2]
        Combustible = fila[3]
        Transmision = fila[4]
        Estado = fila[5]
        Matriculacion = fila[6]
        Kilometraje = fila[7]
        Potencia = fila[8]
        Precio = fila[9]
        
        coche = (Marca, Modelo, Combustible, Transmision, Estado, Matriculacion, Kilometraje, Potencia, Precio)
        
        insertar_tabla_coches(conexion, coche)
        
        
def insertar_tabla_coches(conexion, coche):
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO coches(Marca, Modelo, Combustible, Transmision, Estado, Matriculacion, Kilometraje, Potencia, Precio) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', coche)
    conexion.commit()
    
def consultar_coches(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM coches LIMIT 20')
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

def numero_coches_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT COUNT(*) FROM coches')
    dato = cursor.fetchall()
    numero = dato[0][0]
    return numero

def precio_total_coches(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT SUM(Precio) FROM coches')
    dato = cursor.fetchall()
    numero = dato[0][0]
    return numero

def marca_coche_mas_barato(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT Marca, Modelo, MIN(Precio) FROM coches')
    datos = cursor.fetchall()
    return datos

def marca_coche_mas_caro(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT Marca, Modelo, MAX(Precio) FROM coches')
    datos = cursor.fetchall()
    return datos

def precio_medio_por_marca(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT Marca, AVG(Precio) FROM coches GROUP BY marca')
    datos = cursor.fetchall()
    return datos
        
        
            
        

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print("Error. Número de parámetros incorrecto. Puede faltar el nombre del archivo")
    else:
        nombre_fichero = sys.argv[1]
        
        borrar_datos()
        
        
        descomprimir_fichero(nombre_fichero)
        
        datos = leer_datos(nombre_fichero)
        print(datos)
        
        conexion = crear_conexion_bd()
        
        crear_tabla_coches(conexion)
        
        grabar_coches(conexion, datos)
        
        
        print("\n Consultamos los datos de la tabla")
        consultar_coches(conexion)
        
        dato = numero_coches_tabla(conexion)
        print("\n El número de coches es de {}".format(dato))
        
        
        numero = precio_total_coches(conexion)
        dinero = '{:,}'.format(numero).replace(',','.')
        print("\n El precio total de todos los coches es de {}".format(dinero))
        
        datos= marca_coche_mas_barato(conexion)
        marca = datos[0][0]
        modelo = datos[0][1]
        precio = datos[0][2]
        print('\n El coche más barato es : Marca = {}, modelo = {}, precio = {}'.format(marca,modelo,precio))
        
        datos= marca_coche_mas_caro(conexion)
        marca = datos[0][0]
        modelo = datos[0][1]
        precio = datos[0][2]
        print('\n El coche más caro es : Marca = {}, modelo = {}, precio = {}'.format(marca,modelo,precio))
        
        datos = precio_medio_por_marca(conexion)
        
        print("\n Precio medio por marca\n")
        for dato in datos:
            marca = dato[0]
            precio = dato[1]
            print(marca, precio)
            
        conexion.close()
        
        