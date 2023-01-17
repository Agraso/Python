print('Bienvenido al juego de preguntas estilo beber')

respuesta1 = input('Decide: "Derecha" o "Izquierda"').lower()
if respuesta1 == 'izquierda':
    print('Nada te toca beber')
else:
    print('Te has salvado deberias estar agradecido')
    respuesta2 = input('Estas en una isla te toca de toca decidir otra vez: "Nadar" o "Caminar" por un puente').lower()
    if respuesta2 == 'nadar':
        print('Bueno pues te toca nadar en alcohol')
    else:
        print('UFFF te salvaste de nuevo...')
        respuesta3 = input('Bueno esta es la ultima va por todo. Decide la puerta "Rojo" , "Verde" o "Azul"').lower()
        if respuesta3 == 'verde':
            print('Enhorabuna te has salvado, como recompensa manda a beber a los demás')
        else:
            print('No vale solo te faltaba una por tonto/a te toca beber el doble')
            
print('\nFin del juego')