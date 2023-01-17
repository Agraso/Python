from tkinter import *
from tkinter.colorchooser import askcolor



ventana = Tk()
ventana.title('Calculadora')
ventana.geometry('395x350')
ventana.resizable(False,False)
ventana.configure(background='#17202A')


#Funciones
operacion = ""
resultado = StringVar()

def borra():
    global operacion
    global resultado
    operacion=""
    pantalla.delete(0,END)

def pulsar(valor):
    global operacion
    global resultado
    operacion = operacion + str(valor)
    pantalla.delete(0,END)
    pantalla.insert(0,operacion)

def calcular():
    global operacion
    global resultado
    try:
        resultado = str(eval(operacion))
    except:
        resultado = 'Error'
    finally:
        pantalla.delete(0,END)
        pantalla.insert(0,resultado)



# Display
pantalla = Entry(ventana, font=('arial',20), borderwidth=2,foreground='white',bg='#1C2833')
pantalla.grid(row=0,column=0, columnspan=3, pady=10,padx=5)

#boton de reiniciar
boton_reset = Button(ventana, text='AC', width=8, height=2, command= lambda:borra())
boton_reset.grid(row=0,column=3,pady=10)

#botones de la primera fila
ancho = 8
alto = 3
boton1 = Button(ventana, text='1', width=ancho, height=alto, command= lambda:pulsar('1'))
boton1.grid(row=1, column=0, padx=1, pady=5)
boton2 = Button(ventana, text='2', width=ancho, height=alto, command= lambda:pulsar('2'))
boton2.grid(row=1, column=1, padx=1, pady=5)
boton3 = Button(ventana, text='3', width=ancho, height=alto, command= lambda:pulsar('3'))
boton3.grid(row=1, column=2, padx=1, pady=5)
boton4 = Button(ventana, text='4', width=ancho, height=alto, command= lambda:pulsar('4'))
boton4.grid(row=1, column=3, padx=1, pady=5)

#botones de la segunda fila
ancho = 8
alto = 3
boton5 = Button(ventana, text='5', width=ancho, height=alto, command= lambda:pulsar('5'))
boton5.grid(row=2, column=0, padx=1, pady=5)
boton6 = Button(ventana, text='6', width=ancho, height=alto, command= lambda:pulsar('6'))
boton6.grid(row=2, column=1, padx=1, pady=5)
boton7 = Button(ventana, text='7', width=ancho, height=alto, command= lambda:pulsar('7'))
boton7.grid(row=2, column=2, padx=1, pady=5)
boton8 = Button(ventana, text='8', width=ancho, height=alto, command= lambda:pulsar('8'))
boton8.grid(row=2, column=3, padx=1, pady=5)

#botones de la tercera fila
ancho = 8
alto = 3
boton9 = Button(ventana, text='9', width=ancho, height=alto, command= lambda:pulsar('9'))
boton9.grid(row=3, column=0, padx=1, pady=5)
boton0 = Button(ventana, text='0', width=ancho, height=alto, command= lambda:pulsar('0'))
boton0.grid(row=3, column=1, padx=1, pady=5)
boton_punto = Button(ventana, text='.', width=ancho, height=alto, command= lambda:pulsar('.'))
boton_punto.grid(row=3, column=2, padx=1, pady=5)
boton_suma = Button(ventana, text='+', width=ancho, height=alto, command= lambda:pulsar('+'))
boton_suma.grid(row=3, column=3, padx=1, pady=5)

#botones de la cuarta fila
ancho = 8
alto = 3
boton_resta = Button(ventana, text='-', width=ancho, height=alto, command= lambda:pulsar('-'))
boton_resta.grid(row=4, column=0, padx=1, pady=5)
boton_mult = Button(ventana, text='*', width=ancho, height=alto, command= lambda:pulsar('*'))
boton_mult.grid(row=4, column=1, padx=1, pady=5)
boton_div = Button(ventana, text='/', width=ancho, height=alto, command= lambda:pulsar('/'))
boton_div.grid(row=4, column=2, padx=1, pady=5)
boton_result = Button(ventana, text='=', width=ancho, height=alto, command= lambda:calcular())
boton_result.grid(row=4, column=3, padx=1, pady=5)




ventana.mainloop()