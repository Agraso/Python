def sumar(numero1, numero2):
    """
    Esto es la documentacion de esta funcion.
    Recibe dos números como parámetros y delvuelve la suma
    
    >>> sumar(4,3)
    7
    
    >>> sumar(5,4)
    9
    
    >>> sumar(1,3)
    5
    
    """
    return numero1 + numero2


resultado = sumar(2,4)
print(resultado)

import doctest
doctest.testmod()