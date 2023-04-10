"""
RELACION ENTRE NÚMEROS:
Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma de los otros dos.

"""
#funcion que define que numero es mayor
def relacion(num1, num2, num3):
    if (num1 + num2 == num3):
        print("El " + str(num1) + " + " + str(num2) + " es igual a " + str(num3))
    elif (num2 + num3 == num1):
        print("El " + str(num2) + " + " + str(num3) + " es igual a " + str(num1))
    elif (num1 + num3 == num2):
        print("El " + str(num1) + " + " + str(num3) + " es igual a " + str(num2))
    else:
        print("No existe realcion entre los 3 numeros")
 
#pedir por pantalla los 4 numeros
num1 = int(input("Ingrese el numero 1:\n"))
num2 = int(input("Ingrese el numero 2:\n"))
num3 = int(input("Ingrese el numero 3:\n"))

#llamar a la funcion mayor

relacion(num1, num2, num3)