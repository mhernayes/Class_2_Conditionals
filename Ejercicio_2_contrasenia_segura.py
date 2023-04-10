"""
CONTRASEÑA SEGURA:
Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos
especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario,
comprueba si es una contraseña segura e indícalo por pantalla.
"""


#importamos tiempo y colores
import time
import termcolor

#utilizamos la funcion longitud
def longitud(long):
    #seteamos la variable resultado_long
    resultado_long = "NO OK"
    #colocamos la primera condicion que debe tener mas de 8 caracteres
    if long >= 8: 
        #imprimimos mensaje
        print ("Verificando la longitud de la contraseña")
        #esperamos 2 segundos
        time.sleep(2)
        #imprimimos mensaje
        print(termcolor.colored("longitud OK", 'green'))
        resultado_long = "OK"
    #en caso de no tener más de 8 caracteres
    else:
        #imprimimos mensaje
        print("Verificando la longitud de la contraseña")
        #esperamos 2 segundos
        time.sleep(2)
        print(termcolor.colored("Lontigud incorrecta", 'red'))
    #devolvemos la variable
    return resultado_long

#utilizamos la funcion simbolo
def simbolo(contrasenia, long):
    #seteamos la variable resultado_simbolo
    resultado_simbolo = "NO OK"
    #recorremos el array con el for hasta "long"
    for i in range(0, long):
        #fijamos los condicionales
        if contrasenia[i] == "*" or contrasenia[i] == "#":
            #le asignamos a una variables "OK"
            resultado_simbolo = "OK"
    #imprimimos mensaje
    if resultado_simbolo == "OK":
        print ("Verificando si contiene simbolos especiales")
        #esperamos 2 segundos
        time.sleep(2)
        #imprimimos mensaje
        print(termcolor.colored("Simbolos OK", 'green'))
    #en caso de no tener simbolos especiales
    else:
        #imprimimos mensaje
        print ("Verificando si contiene simbolos especiales")
        #esperamos 2 segundos
        time.sleep(2)
        print(termcolor.colored("No contiene simbolos especiales", 'red'))
    #devolvemos la variable
    return resultado_simbolo

def vocales(contrasenia, long):
    #seteamos la variable resultado_vocales
    resultado_vocales = "NO OK"
    for i in range(0, long):
        #fijamos los condicionales
        if contrasenia[i] == "a" or contrasenia[i] == "e" or contrasenia[i] == "i" or contrasenia[i] == "o" or contrasenia[i] == "u":
            resultado_vocales = "OK"
        #en caso de no tener vocales en minuscula
    if resultado_vocales == "OK":
        #imprimimos mensaje
        print ("Verificando si contiene vocales")
        #esperamos 2 segundos
        time.sleep(2)
        #imprimimos mensaje
        print(termcolor.colored("Vocales OK", 'green'))
    else:
        #imprimimos mensaje
        print ("Verificando si contiene vocales")
        #esperamos 2 segundos
        time.sleep(2)
        print(termcolor.colored("No contiene vocales", 'red'))
    #devolvemos la variable
    return resultado_vocales


def resultado(resultado_long, resultado_simbolo, resultado_vocales):
    if resultado_long == "OK" and resultado_simbolo == "OK" and resultado_vocales == "OK":
        print("Verificando contraseña")
        time.sleep(2)
        print("Por favor, espepre unos segundos")
        time.sleep(2)
        print(termcolor.colored("CONTRASEÑA OK", 'green'))
    else:
        print("Verificando contraseña")
        time.sleep(2)
        print("Por favor, espepre unos segundos")
        time.sleep(2)
        print(termcolor.colored("CONTRASEÑA INCORRECTA", 'red'))

#imprimimos el mensaje
print("----------------------------------------------")
print("Por favor ingrese su contraeña. Debe contener: ")
print("\t - más de 8 caracteres. \n \t - dos simbolos especiales (pueden ser solo '*' o '#).\n \t - una vocal en minuscula")

#solicitamos por pantalla la contraeña
contrasenia = input()
long = len(contrasenia)

#llamamos la funcion longitud
resultado_long = longitud(long)

#llamamos a la funcion simbolos
resultado_simbolo = simbolo(contrasenia, long)

#llamos a la funcion vocales
resultado_vocales = vocales(contrasenia, long)

#llamamos la funcion final
resultado(resultado_long, resultado_simbolo, resultado_vocales)