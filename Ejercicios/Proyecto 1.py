# # # import modulo1

# # # coche1 = modulo1.Coche('Fiat', 'Blanco', 'diesel', '2')

# # # print(coche1.mostrar_caracteristicas())

# # # media = modulo1.media(10,10,10)

# # # print("La nota media es {}".format(media))

# # # fichero = open("FicherodePrueba.txt","rt")

# # # datos_fichero = fichero.read()

# # # print(datos_fichero)

# # # # fichero = open("FicheroDePrueba.txt", "at")

# # # # cadena_para_incluir = "\nEsta es la tercera linea del fichero"

# # # # fichero.write(cadena_para_incluir)
# # # # fichero.close()

# # import os

# # os.remove("FicheroDePrueba.txt")



# # import modulofichero

# # nombre_fichero = "Fichero1.txt"

# # fichero = modulofichero.Fichero(nombre_fichero)

# # # texto = "Esta es la primera fila del fichero.\nEsta es la segunda fila del fichero"

# # # fichero.grabar_fichero(texto)

# # # texto= "\nEste es un texto mal escrito"

# # # fichero.incluir_fichero(texto)

# # # texto_leido = fichero.leer_fichero()

# # # print(texto_leido)

# # fichero.borrar_fichero()


# import pickle

# # lista_colores = ['azul','verde','rojo','amarillo']
# # fichero = open("fichero_colores.pckl","wb")
# # pickle.dump(lista_colores, fichero)
# # fichero.close()

# # fichero = open("fichero_colores.pckl","rb")

# # lista_leida = pickle.load(fichero)

# # print(lista_leida)


# # frutas = {'manzana':'apple', 'naranja':'orange', 'platano':'banana', 'limon':'lemon'}
# # fichero = open("fichero_frutas.pckl","wb")
# # pickle.dump(frutas,fichero)
# # fichero.close()

# fichero = open("fichero_frutas.pckl","rb")
# datos = pickle.load(fichero)

# print(datos)

# datos.values()