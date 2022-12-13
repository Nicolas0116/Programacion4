import redis

r = redis.Redis(host="localhost")

def VolverMenu():
    z = int(input(f"1.Volver al menu principal\n2.Salir\n"))
    if z == 1:
        x = 0
    else:
        x = 6
    return x

x = 0
r.flushall()
r.set("MOPRI","Se refiere al hijo del tío de una persona o  también describe a un amigo")

while x < 6:
    if x == 0:
        print("*************** Diccionario de slang panameño **********************\n")
        x = int(input(f"Menu principal \n1.Agregar una palabra\n2.Editar una palabra\n3.Eliminar una palabra"
                      f"\n4.Ver listado de palabras\n5.Buscar significado de palabra\n6.Salir\n"))
    elif x == 1:
        valor = (input(f"Que palabra desea ingresar: "))
        if r.exists(valor.upper()):
            print("Esa palabra ya existe en el diccionario\n")
            x = VolverMenu()
        else:
            significado = input(f"Ingrese el significado: ")
            r.set(valor.upper(), significado)
            print("Se ingreso la palabra con exito.")
            x = VolverMenu()
    elif x == 2:
        valor = (input(f"Que palabra desea editar: "))
        if r.exists(valor.upper()):
            t = int(input(f"Que desea editar:\n1.Palabra\n2.Significado\n"))
            if t == 1:
                new = input(f"Ingrese la palabra editada: ")
                if r.exists(new.upper()):
                    print("La palabra ingresada ya existe")
                    x = 0
                else:
                    r.rename(valor.upper(),new.upper())
                    print("Se edito la palabra con exito !!\n")
                    x = VolverMenu()
            else:
                news = input(f"Ingrese el nuevo significado: ")
                r.set(valor.upper(),news)
                print("Se edito el significado con exito !!\n")
                x = VolverMenu()
        else:
            print("Esa palabra no existe en el diccionario.\n")
            x = VolverMenu()
    elif x == 3:
        valor = (input(f"Que palabra desea eliminar: "))
        if r.exists(valor.upper()):
            r.delete(valor.upper())
            print("Se elimino la palabra con exito !!\n")
            x = VolverMenu()
            print(r.keys())
        else:
            print("La palabra " + valor + " no existe en el diccionario.\n")
            x = VolverMenu()
    elif x == 4:
        z = r.keys()
        if z == []:
            print("No existen registros en el diccionario.\n")
            x = VolverMenu()
        else:
            print("El listado de palabras en el diccionario son: ")
            y = r.keys()
            for i in y:
                print(i.decode("utf-8"))
            print("\n")
            x = VolverMenu()
    elif x == 5:
        valor = (input(f"El significado de que palabra desea buscar: "))
        y = r.get(valor.upper())
        if y != None:
            z = r.get(valor.upper()).decode("utf-8")
            print("\nEl significado es:\n" + str(z) + "\n")
            x = VolverMenu()
        else:
            print("La palabra " + valor + " no existe en el diccionario.\n")
            x = VolverMenu()


