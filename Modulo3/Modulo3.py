from pymongo import MongoClient

def VolverMenu():
    z = int(input(f"1.Volver al menu principal\n2.Salir\n"))
    if z == 1:
        x = 0
    else:
        x = 6
    return x

x = 0

cliente = MongoClient ('mongodb://localhost:27017')
with cliente:
    db = cliente.slangdb
    db.slang.drop()
    slang = [{"palabra":"MOPRI","significado":"Se refiere al hijo del tío de una persona o  también describe a un amigo"}]
    db.slang.insert_many(slang)

#    db.slang.insert_many(insert())

    while x < 6:
        if x == 0:
            print("*************** Diccionario de slang panameño **********************\n")
            x = int(input(f"Menu principal \n1.Agregar una palabra\n2.Editar una palabra\n3.Eliminar una palabra"
                          f"\n4.Ver listado de palabras\n5.Buscar significado de palabra\n6.Salir\n"))
        elif x == 1:
            valor = (input(f"Que palabra desea ingresar: "))
            agr = [{'$match': {'palabra': valor.upper()}}]
            val = list(db.slang.aggregate(agr))
            if val == []:
                significado = input(f"Ingrese el significado: ")
                new = [{"palabra": valor.upper(), "significado": significado}]
                db.slang.insert_many(new)
                x = VolverMenu()
            else:
                print("Esa palabra ya existe en el diccionario\n")
                x = VolverMenu()
        elif x == 2:
            valor = (input(f"Que palabra desea editar: "))
            agr = [{'$match': {'palabra': valor.upper()}}]
            val = list(db.slang.aggregate(agr))
            if val != []:
                t = int(input(f"Que desea editar:\n1.Palabra\n2.Significado\n"))
                if t == 1:
                    new = input(f"Ingrese la palabra editada: ")
                    agr = [{'$match': {'palabra': new.upper()}}]
                    val1 = list(db.slang.aggregate(agr))
                    if val1 == []:
                        ant = {"palabra": valor.upper()}
                        newvalues = {"$set": {"palabra": new.upper()}}
                        db.slang.update_one(ant, newvalues)
                        print("Se edito la palabra con exito !!\n")
                        x = VolverMenu()
                    else:
                        print("La palabra ingresada ya existe")
                        x = 0
                else:
                    news = input(f"Ingrese el nuevo significado: ")
                    ant = {"palabra": valor.upper()}
                    newvalues = {"$set": {"significado": news}}
                    db.slang.update_one(ant, newvalues)
                    print("Se edito el significado con exito !!\n")
                    x = VolverMenu()
            else:
                print("Esa palabra no existe en el diccionario.\n")
                x = VolverMenu()
        elif x == 3:
            valor = (input(f"Que palabra desea eliminar: "))
            agr = [{'$match': {'palabra': valor.upper()}}]
            val = list(db.slang.aggregate(agr))
            if val != []:
                delete = {"palabra": valor.upper()}
                db.slang.delete_one(delete)
                print("Se elimino la palabra con exito !!\n")
                x = VolverMenu()
            else:
                print("La palabra " + valor + " no existe en el diccionario.\n")
                x = VolverMenu()
        elif x == 4:
            tl = db.slang.find()
            if list(tl) != []:
                print("El listado de palabras en el diccionario son: ")
                total = db.slang.find({}, {'_id': 0, 'palabra': 1})
                for t in total:
                    print(t)
                print("\n")
                x = VolverMenu()
            else:
                print("No existen registros en el diccionario.\n")
                x = VolverMenu()
        elif x == 5:
            valor = (input(f"El significado de que palabra desea buscar: "))
            agr = [{'$match': {'palabra': valor.upper()}}]
            val = list(db.slang.aggregate(agr))
            if val != []:
                print("\nEl significado es:\n"+val[0]["significado"]+"\n")
                x = VolverMenu()
            else:
                print("La palabra " + valor + " no existe en el diccionario.\n")
                x = VolverMenu()

