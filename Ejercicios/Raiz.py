import tkinter
from tkinter import messagebox
from tkinter import filedialog

#-----------------COMPONENTE PRINCIPAL-------------------

# raiz= tkinter.Tk()
# raiz.title("Mi programa")

# raiz.mainloop()

#--------------------------------------------------------


#--------------------------FRAME-------------------------

# raiz= tkinter.Tk()
# raiz.title("Mi programa")

# frame = tkinter.Frame(raiz)
# frame.config(bg='blue', width=400,height=300)
# frame.pack()


# raiz.mainloop()

#--------------------------------------------------------


#------------------------LABEL---------------------------

# raiz= tkinter.Tk()
# raiz.title("Mi programa")

# texto = "Hola mundo"
# etiqueta = tkinter.Label(raiz, text=texto)
# etiqueta.config(fg="green", bg="lightgrey", font=("Cortana",30))
# etiqueta.pack()

# raiz.mainloop()

#--------------------------------------------------------


#-----------------COMPONENTE ENTRY-------------------

# raiz= tkinter.Tk()
# raiz.title("Mi programa")

# entrada = tkinter.Entry(raiz)
# entrada.config(justify='center', show="*")
# entrada.pack()

# raiz.mainloop()

#--------------------------------------------------------


#-----------------COMPONENTE TEXTL-------------------

# raiz= tkinter.Tk()
# raiz.title("Mi programa")

# entrada = tkinter.Text(raiz)
# entrada.config(width=20 , height=10 , font=("Verdana",10), padx=10 , pady=10, fg='green', selectbackground="lightgrey")
# entrada.pack()

# raiz.mainloop()

#--------------------------------------------------------


#-----------------COMPONENTE BUTTON-------------------

# raiz= tkinter.Tk()
# raiz.title("Mi programa")

# def accion():
#     print('Hola Mundo')

# boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
# boton.config(fg='green')
# boton.pack()

# raiz.mainloop()

#--------------------------------------------------------


#--------------COMPONENTE BOTON MULTIPLE-----------------

# raiz= tkinter.Tk()
# raiz.title("Mi programa")

# #definicion de la funcion
# def seleccionar():
#     print('La opción seleccionada es {}'.format(opcion.get()))

# opcion = tkinter.IntVar()

# radiobutton1 = tkinter.Radiobutton(raiz, text='Opción 1', variable= opcion , value=1, command=seleccionar)
# radiobutton1.pack()

# radiobutton2 = tkinter.Radiobutton(raiz, text='Opción 2', variable= opcion , value=2, command=seleccionar)
# radiobutton2.pack()

# radiobutton3 = tkinter.Radiobutton(raiz, text='Opción 3', variable= opcion , value=3, command=seleccionar)
# radiobutton3.pack()

# raiz.mainloop()

#--------------------------------------------------------


#----------------COMPONENTE CHECKBUTTON------------------

# raiz= tkinter.Tk()
# raiz.title("Mi programa")

# #definir la funcion
# def verificar():
#     valor = check1.get()
#     if (valor == 1):
#         print("El check está activado")
#     else:
#         print("El check está desactivado")

# check1 = tkinter.IntVar()

# boton = tkinter.Checkbutton(raiz, text='Opción 1', variable=check1, onvalue=1, offvalue=0, command=verificar)
# boton.pack()

# raiz.mainloop()

#--------------------------------------------------------


#-------------COMPONENTE MENSAJE EN CAJA----------------

# raiz= tkinter.Tk()
# raiz.title("Mi programa")

# #funcion avisar
# def avisar():
#     info = tkinter.messagebox.showinfo("Titulo","Mensaje con la información")

# boton = tkinter.Button(raiz, text='Pulsar para aviso', command=avisar)
# boton.pack()

# raiz.mainloop()

#-------------------------------------------------------


#-----------MENSAJE EN CAJA PARA PREGUNTA---------------

# raiz= tkinter.Tk()
# raiz.title("Mi programa")

# def preguntar():
#     resultado = tkinter.messagebox.askquestion("Titulo de la pregunta", "¿Quieres borrar este fichero?")
#     if (resultado == "yes" ):
#         print("Si, quiero borrar el fichero")
#     else:
#         print("No, no quiero borrar el fichero")

# boton = tkinter.Button(raiz, text="Pulsar para preguntar", command=preguntar)
# boton.pack()

# raiz.mainloop()

#-------------------------------------------------------


#-----------------COMPONENTE FILEDIALOG-----------------

# raiz= tkinter.Tk()
# raiz.title("Mi programa")

# def abrirfichero():
#     rutafichero = filedialog.askopenfilename(title="Abrir un fichero")
#     print(rutafichero)

# boton = tkinter.Button(raiz, text='Pulsar para empezar', command=abrirfichero)
# boton.pack()

# raiz.mainloop()

#-------------------------------------------------------