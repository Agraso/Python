import random
import replit

def generara_carta():
    cartas = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    carta = random.choice(cartas)
    return carta

def sumar_cartas(cartas):
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0
    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)

def mostrar_ganador(marcador_usuario, marcador_ordenador):
    if marcador_usuario == marcador_ordenador:
        texto = "Empate"
    elif marcador_ordenador == 0:
        texto = 'Has perdido el ordenador tiene 21 = BLACKJACK'
    elif marcador_usuario == 0:
        texto = 'Has ganado!!!! tienes 21 = BLACKJACK'
    elif marcador_usuario > 21:
        texto = 'Has perdido tu marcador es mayor a 21'
    elif marcador_ordenador > 21:
        texto = 'Has ganado!!!! la suma de las cartas del ordenador son mayor a 21 '
    elif marcador_usuario > marcador_ordenador:
        texto = 'Has ganado!!!!'
    else:
        texto = 'Has perdido'
    return texto
        
def jugar():
    print('Estamos jugando .....')
    
    cartas_usuario = []
    cartas_ordenador = []
    finalizado = False
    
    for valor in range(2):
        carta = generara_carta()
        cartas_usuario.append(carta)
        
        carta_ordenador = generara_carta()
        cartas_ordenador.append(carta_ordenador)
        
    while not finalizado:
        marcador_usuario = sumar_cartas(cartas_usuario)
        marcador_ordenador = sumar_cartas(cartas_ordenador)
        print(f"Cartas del usuario = {cartas_usuario}, marcador = {marcador_usuario}")
        print(f"Cartas del ordenador = {cartas_ordenador[0]}")
        if marcador_usuario == 0 or marcador_ordenador == 0 or marcador_usuario > 21:
            finalizado = True
        else:
            mas_cartas = input('¿Quieres más cartas? Escribe "Si" o "No"').lower()
            if mas_cartas == "si":
                carta = generara_carta()
                cartas_usuario.append(carta)
            else:
                finalizado = True
                
    while marcador_ordenador != 0 and marcador_ordenador < 17:
        carta_ordenador = generara_carta()
        cartas_ordenador.append(carta_ordenador)
        marcador_ordenador = sumar_cartas(cartas_ordenador)
        
    print(f"Cartas del usuario = {cartas_usuario}, marcador = {marcador_usuario}")
    print(f"Cartas del ordenador = {cartas_ordenador}, marcador {marcador_ordenador}")
    
    texto = mostrar_ganador(marcador_usuario,marcador_ordenador)
    print(texto)
        
                
    
    
    
    
    
    
#Principio del programa
while input('¿Quieres jugar al Blackjack? Escribe "Si" o "No"').lower() == 'si':
    replit.clear()
    jugar()
    


# texto = mostrar_ganador(18,25)
# print(texto)