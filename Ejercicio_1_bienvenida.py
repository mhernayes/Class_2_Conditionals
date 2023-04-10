"""
BIENVENIDA AL USUARIO:
Un ordenador tiene tres usuarios distintos (Alejandro, Naomi y Sergio) y otro usuario invitado.
Haz un script que pida el nombre al usuario y le dé una bienvenida personalizada. Crea el script
de tal manera que si el usuario no es ninguno de los tres se le dé un saludo genérico.
¿Que ocurre si uno de los usuarios introduce su nombre completamente en minúsculas?¿Y si lo
introduce en mayúsculas? ¿Y si sin querer pone in punto en mitad de su nombre (p.e. nao.mi)?¿Y
si se le cuela una almohadilla (p.e se#rgio)?
"""

usuario_1 = "Alejandro"
usuario_2 = "Naomi"
usuario_3 = "Sergio"
usuario_invitado = "quien quiera que seas"
nombre = input("Por favor ingrese su nombre de usuario: \n")
nombre = nombre.replace(".","")
nombre = nombre.replace("#","")

if nombre.title() == usuario_1:
    print("Bienvenido, ", usuario_1)
elif nombre.title() == usuario_2:
    print("Bienvenido, ", usuario_2)
elif nombre.title() == usuario_3:
    print("Bienvenido, ", usuario_3)
else:
    print("Bienvenido, ", usuario_invitado)

