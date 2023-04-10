"""
DECLARACION DE LA RENTA:
Para tributar en un determinado país es necesario ser mayor de edad y cobrar más de 1000 euros al mes. 
Además los tramos impositivos de la renta anual son los siguientes:
RENTA
Menos de 15.000 eu - 5%
Entre 15.000 y 25.000 eu - 15%
Entre 25.000 y 35.000 eu - 20%
Entre 35.000 y 60.000 eu - 30%
Más de 60.000 eu - 45%

Escribe un script que primero compruebe si eres susceptible de que se te aplique algún 
tipo impositivo y en caso afirmativo imprima por pantalla cuál te tocaría.
"""
import termcolor 

def resultado(nombre, edad, sueldo_anual, opcion):
    if sueldo_minimo == "n":
        print("Usted debe cobrar más de 1000 EU para tributar impuestos.")
    elif opcion == "1":
        print("Usted debe abonar en un 5 porciento de impuestos")
    elif opcion == "2":
        print("Usted debe abonar en un 15 porciento de impuestos")
    elif opcion == "3":
        print("Usted debe abonar en un 20 porciento de impuestos")
    elif opcion == "4":
        print("Usted debe abonar en un 30 porciento de impuestos")
    elif opcion == "5":
        print("Usted debe abonar en un 45 porciento de impuestos")

#solicitar datos
nombre = input("Por favor ingrese su nombre:\n")
edad = input("Por favor ingrese su edad:\n")
sueldo_minimo = input("Cobra más de 1000 EU por mes? s/n\n")

print("Vamos a comprobar si tenés que tributar algún impuesto de acuerdo a la tabla siguiente:")
tabla = """------------------------
1. Menos de 15.000 eu - 5%
2. Entre 15.000 y 25.000 eu - 15%
3. Entre 25.000 y 35.000 eu - 20%
4. Entre 35.000 y 60.000 eu - 30%
5. Más de 60.000 eu - 45%
------------------------"""
print(tabla)

#pedir la opcion de cuanto cobra por año
opcion = input("De acuerdo a la tabla anterior, por favor, ingrese el cuánto cobra por año?\n")

#llamar a la funcion
resultado(nombre, edad, sueldo_minimo, opcion)


