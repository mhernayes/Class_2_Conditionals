"""EL MAYOR DE CUATRO:
Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por pantalla.
"""

#funcion que define que numero es mayor
def mayor(num1, num2, num3, num4):
    if (num1 > num2) and (num1 > num3) and (num1 > num4):
        print("El " + str(num1) + " es el más grande")
    elif (num2 > num1) and (num2 > num3) and (num2 > num4):
        print("El " + str(num2) + " es el más grande")
    elif (num3 > num1) and (num3 > num2) and (num3 > num4):
        print("El " + str(num3) + " es el más grande")
    elif (num4 > num1) and (num4 > num2) and (num4 > num3):
        print("El " + str(num4) + " es el más grande")



#pedir por pantalla los 4 numeros
num1 = float(input("Ingrese el numero 1:\n"))
num2 = float(input("Ingrese el numero 2:\n"))
num3 = float(input("Ingrese el numero 3:\n"))
num4 = float(input("Ingrese el numero 4:\n"))

#llamar a la funcion mayor

mayor(num1, num2, num3, num4)


