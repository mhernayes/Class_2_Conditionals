"""
RESTAURANTE ONLINE:
En una hamburguesería han abierto la posibilidad de hacer pedidos online. 
Ofrecen básicamente dos productos de fama mundial: su hamburguesa clásica y la hamburguesa vegana.
Los ingredientes extra de la hamburguesa clásica son: 
- Queso Idiazabal
- Bacon
- Huevo
Los ingredientes extra de la hamburguesa vegana son: 
- Tofu
- Cebolla caramelizada
Crea un script que le pregunte al usuario que tipo de hamburguesa quiere. 
En función de la respuesta debe enseñarle los ingredientes extra disponibles y permitirle escoger uno de ellos. 
Finalmente debe imprimir por pantalla que tipo de hamburguesa se ha elegido 2y cuales son sus ingredientes.
"""
def menu():
    #definimos el menu de la hamburguesa
    _menu = {"Clasica": 1, "Vegana": 2}
    return _menu

def ing_clasica():
    #definimos los ingredientes
    _ing_clasica = {"Queso Idiazabal": 1, "Bacon": 2, "Huevo": 3}
    return _ing_clasica

def ing_vegana():
    _ing_vegana = {"Tofu": 1, "Cebolla Caramelizada": 2}
    return _ing_vegana
    
def hamburguesa():
    #definimos la variable control = true para que se repita el bucle
    control = True
    #seteamos la lista en "vacio"
    lista = []
    while control == True:
        try:
            #definimos esta variable para el bucle infinito en caso de que la respuesta no coincida
            respuesta1 = True
            #solicitar al usuario que tipo de hamburguesa quiere
            pedido = int(input("¿Que tipo hamburguesa quiere?\n"))
            while respuesta1 == True:
                #si el pedido elegido coincice con la informacion cargada en el diccionario mostrará lo que eligio
                if pedido == menu().get("Clasica"):
                    print("Usted eligio la Hamburguesa Clasica")
                    #solicitamos los ingredientes
                    respuesta3 = True
                    ingrediente = int(input("Elija un ingrediente:\n"))
                    while respuesta3 == True:
                        if ingrediente == ing_clasica().get("Queso Idiazabal"):
                            print("Usted eligio la Queso Idiazabal") 
                            #agregmos el pedido a la lista
                            lista.append("1 Hamburguesa Clasica con Queso Idiazabal")
                            #salimos del while ingredientes
                            respuesta3 = False
                        elif ingrediente == ing_clasica().get("Bacon"):
                            print("Usted eligio Bacon") 
                            #agregmos el pedido a la lista
                            lista.append("1 Hamburguesa Clasica con Bacon")
                            #salimos del while ingredientes
                            respuesta3 = False
                        elif ingrediente == ing_clasica().get("Huevo"):
                            print("Usted eligio Huevo") 
                            #agregmos el pedido a la lista
                            lista.append("1 Hamburguesa Clasica con Huevo")
                            #salimos del while ingredientes
                            respuesta3 = False
                        else:
                            #indicamos las posibles respuestas y volvemos a preguntar 
                            print('Debe ingresar "1", "2" o "3"')
                            ingrediente = int(input("Elija un ingrediente:\n"))
                    #finalizamos while
                    respuesta1 = False
                elif pedido == menu().get("Vegana"):
                    print("Usted eligio la Hamburguesa Vegana")
                     #solicitamos los ingredientes
                    respuesta4 = True
                    ingrediente = int(input("Elija un ingrediente:\n"))
                    while respuesta4 == True:
                        if ingrediente == ing_vegana().get("Tofu"):
                            print("Usted eligio Tofu")  
                            #agregmos el pedido a la lista
                            lista.append("1 Hamburguesa Vegana con Tofu")
                            #salimos del while ingredientes
                            respuesta4 = False
                        elif ingrediente == ing_vegana().get("Cebolla Caramelizada"):
                            print("Usted eligio Cebolla Caramelizada") 
                            #agregmos el pedido a la lista
                            lista.append("1 Hamburguesa Vegana con Cebolla Caramelizada")
                            #salimos del while ingredientes
                            respuesta4 = False
                        else:
                            #indicamos las posibles respuestas y volvemos a preguntar 
                            print('Debe ingresar "1" o "2"')
                            ingrediente = int(input("Elija un ingrediente:\n"))
                    #finalizamos while
                    respuesta1 = False
                    
                else: 
                    #indicamos las posibles respuestas y volvemos a preguntar 
                    print('Debe ingresar "1" o "2"')
                    pedido = int(input("'¿Que tipo hamburguesa quiere?\n"))

            #preguntamos si quiere seguir agregando algo mas al pedido
            pregunta = str(input("'¿Desea pedir algo más? (s/n)\n"))
            #definimos esta variable para el bulce infinito en caso de que la respuesta no coincida
            respuesta2 = True
            while respuesta2 == True:
                if pregunta.lower() == "n" and pregunta.lower() != "s":
                    #si no quiere agregar algo mas, se termina el while cambiando la variable control = false
                    #imprime el pedido consolidado
                    print("--------------------------------")
                    print("El pedido consolidado es:\n")
                    cant_01 = lista.count("1 Hamburguesa Clasica con Queso Idiazabal")
                    cant_02 = lista.count("1 Hamburguesa Clasica con Bacon")
                    cant_03 = lista.count("1 Hamburguesa Clasica con Huevo")
                    cant_04 = lista.count("1 Hamburguesa Vegana con Tofu")
                    cant_05 = lista.count("1 Hamburguesa Vegana con Cebolla Caramelizada")
                    if cant_01 > 1:
                        print("Usted llevará ", cant_01, "Hamburguesas Clasicas con Queso Idiazabal.")
                    elif cant_01 == 1:
                        print("Usted llevará ", cant_01, "Hamburguesa Clasica con Queso Idiazabal.")
                    if cant_02 > 1:
                        print("Usted llevará ", cant_02, "Hamburguesas Clasicas con Bacon.")
                    elif cant_02 == 1:
                        print("Usted llevará ", cant_02, "Hamburguesa Clasica con Bacon.")
                    if cant_03 > 1:
                        print("Usted llevará ", cant_03, "Hamburguesas Clasicas con Huevo.")
                    elif cant_03 == 1:
                        print("Usted llevará ", cant_03, "Hamburguesa Clasica con Huevo.")
                    if cant_04 > 1:
                        print("Usted llevará ", cant_04, "Hamburguesas Vegana con Tofu.")
                    elif cant_04 == 1:
                        print("Usted llevará ", cant_04, "Hamburguesa Vegana con Tofu.")
                    if cant_05 > 1:
                        print("Usted llevará ", cant_05, "Hamburguesas Vegana con Cebolla Caramelizadas.")
                    elif cant_05 == 1:
                        print("Usted llevará ", cant_05, "Hamburguesa Vegana con Cebolla Caramelizadas.")
            
                    #fin del primer while
                    control = False
                    respuesta2 = False
                elif pregunta.lower() == "s":
                    respuesta2 = False
                else:
                    #indicamos las posibles respuestas y volvemos a preguntar 
                    print('Debe ingresar "s" o "n"')
                    pregunta = str(input("¿Desea pedir algo más? (s/n)\n"))
                   
        except: 
           print("Los datos ingresados son incorrectos Vuelva a elegir la Hamburguesa.")
              
    print("Gracias por su orden. ")
    

#mensaje de bienvenida
print("--------------------------------")
print("Bievenidos al Restaurante ConquerBlocks")
mensaje = """("--------------------------------"
Las Hamburguesas con las que contamos son las siguiente:
1. Clasica
2. Vegana
--------------------------------
Estos son los ingredientes extra para la Hamburguesa Clasica:
1. Queso Idiazabal
2. Bacon
3. Huevo
--------------------------------
Estos son los ingredientes extra para la Hamburguesa Vegana:
1. Tofu
2. Cebolla Caramelizada
--------------------------------
"""
print(mensaje)
#llamamos a la funcion hamburguesa
hamburguesa()




