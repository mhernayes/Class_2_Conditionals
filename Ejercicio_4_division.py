"""
DIVISION:
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.
"""
#definimos la funcion par o impat
def division(numero1,numero2):
    resultado = 0
    if numero2 == 0:
        print("El segundo numero no puede ser 0")
        numero2 = float(input("Por favor vuevla ingresar un segundo numero. Tiene una última oportunidad.\n"))
        if numero2 == 0:
            print("ERROR")
        else:
            resultado = numero1 / numero2

    else:
        resultado = numero1 / numero2

    return resultado

print("----------------------------------------------")
#pedimos por pantalla un numero
numero1 = float(input("Por favor, ingrese un numero:\n"))
#pedimos por pantalla una potencia
numero2 = float(input("Por favor ingrese el segundo numero:\n"))
#realizamos el calculo
 

#llamamos a la funcion potencia
resultado = division(numero1,numero2)

print("El resultado es de la divsion entre ambos numeros es: ", resultado)