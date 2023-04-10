"""
BECAS PARA ESTUDIANTES (BONUS*):
El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media. 
Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. 
Crea un script que pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no.
*Los ejercicios bonus no se resolverán directamente en clase si no que están pensados para que los alumnos los discutan por el chat de Discord y compartan sus soluciones. 
Las soluciones compartidas de los alumnos se subirán en un archivo a la academia.
"""

def nota(nombre, edad, nota_media):
    resultado = "NG"
    if (edad > 16 and edad < 22) and (nota_media >= 8):
        resultado = nombre + ", lo felicitamos! recibirá la BECA"
    else: 
        print(nombre + ", lo lamentamos mucho, no recibirá la BECA")
    return resultado

print("----------------------------------------------")
nombre = input("Por favor ingrese el nombre del estudiante:\n")
edad = int(input("Por favor ingrese la eddad del estudiante;\n"))
nota_media = float(input("Ingrese la nota media:\n"))

nota = nota(nombre, edad, nota_media)

print(nota)

