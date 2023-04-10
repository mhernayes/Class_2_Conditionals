"""
PAR O IMPAR:
Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa potencia es par o impar. 
(Pista: los números pares tiene resto = 0 al dividirlos por 2)
"""
#definimos la funcion par o impat
def par_impar(resultado):
    if (resultado % 2) == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

print("----------------------------------------------")
#pedimos por pantalla un numero
numero = int(input("Por favor, ingrese un numero:\n"))
#pedimos por pantalla una potencia
potencia = int(input("Por favor ingrese el valor de la potencia:\n"))
#realizamos el calculo
resultado = numero ** potencia 

#llamamos a la funcion potencia
par_impar(resultado)