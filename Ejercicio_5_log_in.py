"""
LOG-IN:
Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta). 
Si la contraseña es correcta el script debe darle la bienvenida al usuario. 
De lo contrario debe indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la contraseña. 
Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse. 
Cambia el script para que no distinga entre mayúsculas y minúsculas.
(Pista: Necesitarás in If Statement anidado)
"""
import time
import termcolor

def verificar_pass(contrasenia, contrasenia_correcta):
    #seteamos la variable resultado_long
    resultado_pass = "NO OK"
    #fijamos las condiciones
    if contrasenia != contrasenia_correcta:
        #imprimimos mensaje
        print("Verificando contraseña")
        #esperamos 2 segundos
        time.sleep(2)
        print(termcolor.colored("LONG IN INCORRECTO", 'red'))
        contrasenia = input("Vuelva a ingresar la contraseña. Última oportunidad.\n")
        if contrasenia.upper() != contrasenia_correcta:
            #imprimimos mensaje
            print("Verificando la longitud de la contraseña")
            #esperamos 2 segundos
            time.sleep(2)
            print(termcolor.colored("LONG IN INCORRECTO", 'red'))
            print(termcolor.colored("FIN DEL PROGRAMA", 'red'))
        else:
            resultado_pass = "OK"
    else:
        resultado_pass = "OK"
    #devolvemos la variable
    return resultado_pass

def resultado(resultado_pass):
    if resultado_pass == "OK":
        print("Verificando contraseña")
        time.sleep(2)
        print("Por favor, espepre unos segundos")
        time.sleep(2)
        print(termcolor.colored("CONTRASEÑA OK", 'green'))

#imprimimos el mensaje
print("----------------------------------------------")
print("Por favor ingrese su contraeña:\n")

#solicitamos por pantalla la contraeña
contrasenia = input()
contrasenia_correcta = "casa"

#formateamos ambas contraseñas
contrasenia = contrasenia.upper()
contrasenia_correcta = contrasenia_correcta.upper()

#llamar a la funcion
resultado_pass = verificar_pass(contrasenia, contrasenia_correcta)

#llamamos a la funcion resultado
resultado(resultado_pass)

