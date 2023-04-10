"""
EL TRIÁNGULO:
En una obra es necesario construir para el tejado de una casa una estructura triangular con tres piezas. 
El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir este estructura. 
Crea un script que dados tres longitudes indique si podría construirse un triangulo con esas piezas.
(Pista: la suma de dos piezas tiene que ser mayor que el lado restante. Esto debe ser así para todas las posibles combinaciones)
"""

# Pedimos datos por pantalla
longd_1 = int(input('Introduce la longitud del primer lateral:\n'))
longd_2 = int(input('Introduce la longitud del segundo lateral:\n'))
longd_3 = int(input('Introduce la longitud del tercer lateral:\n'))
# Comprovamos que long de las tres es la mas alta
if (longd_1 > longd_2) and (longd_1 > longd_3):
    # si es la 1 sumamos la 2 mas la 3 y si es mayor podemos crear el triangulo si no no podemos crearlo
    if (longd_2 + longd_3) > longd_1:
        print('Podemos crear un triangulo')
    else:
        print('No podemos crear un triangulo')
    # si es la 2 sumamos la 1 mas la 3 y si es mayor podemos crear el triangulo si no no podemos crearlo
elif (longd_2 > longd_1) and (longd_2 > longd_3):
    if (longd_1 + longd_3) > longd_2:
        print('Podemos crear un triangulo')
    else:
        print('No podemos crear un triangulo')
    # si es la 3 sumamos la 1 mas la 2 y si es mayor podemos crear el triangulo si no no podemos crearlo
elif (longd_3 > longd_1) and (longd_3 > longd_2):
    if (longd_1 + longd_2) > longd_3:
        print('Podemos crear un triangulo')
    else:
        print('No podemos crear un triangulo')