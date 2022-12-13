from Modulo2 import Session, engine, Base
from Modulo2_Slang import Slang

## Creacion de esquemas de base de datos
Base.metadata.create_all(engine)
session = Session()

def VolverMenu():
    z = int(input(f"1.Volver al menu principal\n2.Salir\n"))
    if z == 1:
        x = 0
    else:
        x = 6
    return x

x = 0

def agregar(palabra, significado):
    agregar =  Slang(palabra.upper(),significado)
    session.add(agregar)
    session.commit()

def actualizar_palabra(palabra, new):
    x = session.query(Slang).filter(Slang.palabra == palabra.upper()).all()
    for pelicula in x:
        pelicula.palabra = new.upper()
    session.commit()

def actualizar_significado(palabra, news):
    x = session.query(Slang).filter(Slang.palabra == palabra.upper()).all()
    for pelicula in x:
        pelicula.significado = news
    session.commit()

def Existe(palabra):
    x = session.query(Slang).filter(Slang.palabra == palabra.upper()).all()
    lista = []
    for pelicula in x:
        if pelicula.palabra == palabra.upper():
            lista.append(pelicula)
    if lista == []:
        return 0
    else:
        return 1
    session.commit()

def eliminar(palabra):
    x = session.query(Slang).filter(Slang.palabra == palabra.upper()).all()
    for pelicula in x:
        if pelicula.palabra == palabra.upper():
            session.delete(pelicula)
    session.commit()

def obtener():
    x = session.query(Slang).all()
    for pelicula in x:
        print(pelicula.palabra)
    session.commit()

def significado(palabra):
    x = session.query(Slang).filter(Slang.palabra == palabra.upper()).all()
    for pelicula in x:
        if pelicula.palabra == palabra.upper():
            print("Significado: "+ pelicula.significado)
    session.commit()

def vacio():
    x = session.query(Slang).all()
    lista = []
    for pelicula in x:
        lista.append(pelicula.palabra)
    if lista == []:
        return 0
    else:
        return 1
    session.commit()


while x < 6:
    if x == 0:
        print("*************** Diccionario de slang panameño **********************\n")
        x = int(input(f"Menu principal \n1.Agregar una palabra\n2.Editar una palabra\n3.Eliminar una palabra"
                      f"\n4.Ver listado de palabras\n5.Buscar significado de palabra\n6.Salir\n"))
    elif x == 1:
        valor = (input(f"Que palabra desea ingresar: "))
        val = Existe(valor)
        if val == 0:
            y = input(f"Ingrese su significado: ")
            agregar(valor,y)
            print("Se ingreso la palabra con exito !!!\n")
            x = VolverMenu()
        else:
            print("Esa palabra ya existe en el diccionario\n")
            x = VolverMenu()
    elif x == 2:
        valor = (input(f"Que palabra desea editar: "))
        val = Existe(valor)
        if val == 1:
            t = int(input(f"Que desea editar:\n1.Palabra\n2.Significado\n"))
            if t == 1:
                new = input(f"Ingrese la palabra editada: ")
                val1 = Existe(new)
                if val1 == 0:
                    actualizar_palabra(valor,new)
                    print("Se edito la palabra con exito !!\n")
                    x = VolverMenu()
                else:
                    print("La palabra ingresada ya existe")
                    x = 0
            else:
                news = input(f"Ingrese el nuevo significado: ")
                actualizar_significado(valor,news)
                print("Se actualizo el significado con exito !!\n")
                x = VolverMenu()
        else:
            print("Esa palabra no existe en el diccionario.\n")
            x = VolverMenu()
    elif x == 3:
        valor = (input(f"Que palabra desea eliminar: "))
        val = Existe(valor)
        if val == 1:
            eliminar(valor)
            print("Se elimina con exito la palabra "+valor.upper()+"\n")
            x = VolverMenu()
        else:
            print("La palabra " + valor.upper() + " no existe en el diccionario.\n")
            x = VolverMenu()
    elif x == 4:
        val = vacio()
        if val == 1:
            print("El listado de palabras en el diccionario son: ")
            obtener()
            x = VolverMenu()
        else:
            print("En este momento no existen palabras en el diccionario.")
            x = VolverMenu()
    elif x == 5:
        valor = (input(f"El significado de que palabra desea buscar: "))
        val = Existe(valor)
        if val == 1:
            significado(valor)
            x = VolverMenu()
        else:
            print("Esa palabra no existe en el diccionario.")
            x = VolverMenu()


session.commit()
session.close()
