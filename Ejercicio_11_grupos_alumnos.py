"""
GRUPOS DE ALUMNOS:
En uno de los cursos se ha dividido a una clase en dos grupos A y B. 
Para mezclar a los alumnos lo mejor posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la M en el grupo A y el resto en el B. 
A los chicos con nombres empezando por la letra A hasta la H y R hasta la Z se les ha asignado al grupo A también, el resto están en el B.
Crea un script que pregunte al usuario si es chica o chico y el nombre. 
El script debe mostrar por pantalla el grupo que le corresponde a ese alumno.
"""

print("-----------------------")

#seteamo en cero las listas
grupo_A = []
grupo_B = []

while(True):
  #pedimos por pantalla el nombre y formateamos a minuscula
  nombre = input("Ingrese su nombre:\n")
  nombre = nombre.title()
  #pedimos por pantalla el sexo y formateamos a minuscula
  sexo = input("Ingrese el sexo (h/m):\n")
  sexo = sexo.lower()
  if sexo == "m":
    if nombre[0] >= "e" and nombre[0] <= "m":
        grupo_A.append(nombre)
    else: grupo_B.append(nombre)
  elif sexo == "h":
    if nombre[0] >= "i" and nombre[0] <= "q":
        grupo_B.append(nombre)
    else:
        grupo_A.append(nombre)
  pregunta = input("¿Desea ingresar algun otro estudiante? (s/n)\n")
  if pregunta == "n":
    break

print("El grupo A es:")
print(grupo_A)

print("el grupo B es:")
print(grupo_B)
