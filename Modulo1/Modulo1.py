import sqlite3
import os

APP_PATH = os.getcwd()
DB_PATH = APP_PATH + 'Modulo1.db'

conexion = sqlite3.connect(DB_PATH)
cursor = conexion.cursor()

cursor.execute("Drop table if exists TBL_Slang")
conexion.commit()
cursor.execute(""" 
    Create table if not exists TBL_Slang(
        Id text primary key,
        Slang text,
        Significado text
    )  
""")
conexion.commit()

slang = [("1","MOPRI","Se refiere al hijo del tío de una persona o  también describe a un amigo"),
        ("2","CHUZO","Es una interjección que utilizamos para verbalizar algún sentimiento o impresión"),
         ("3","TONGO","Los agentes de la fuerza del orden")]
cursor.executemany("insert into TBL_Slang values (?,?,?);",slang)
conexion.commit()

def VolverMenu():
    z = int(input(f"1.Volver al menu principal\n2.Salir\n"))
    if z == 1:
        x = 0
    else:
        x = 6
    return x

x = 0


while x < 6:
    if x == 0:
        print("*************** Diccionario de slang panameño **********************\n")
        x = int(input(f"Menu principal \n1.Agregar una palabra\n2.Editar una palabra\n3.Eliminar una palabra"
                      f"\n4.Ver listado de palabras\n5.Buscar significado de palabra\n6.Salir\n"))
    elif x == 1:
        valor = (input(f"Que palabra desea ingresar: "))
        cursor.execute('select slang from tbl_slang where slang = "' + valor.upper() + '";')
        val = cursor.fetchone()
        if val == None:
            y = input(f"Ingrese su significado: ")
            cursor.execute("select max(id)+1 from tbl_slang")
            m = cursor.fetchone()
            dato = [m[0], valor.upper(), y]
            cursor.execute("insert into tbl_slang values (?,?,?)", dato)
            conexion.commit()
            print("Se ingreso la palabra con exito !!!\n")
            x = VolverMenu()
        else:
            print("Esa palabra ya existe en el diccionario\n")
            x = VolverMenu()
    elif x == 2:
        valor = (input(f"Que palabra desea editar: "))
        cursor.execute('select slang from tbl_slang where slang = "' + valor.upper() + '";')
        val = cursor.fetchone()
        if val is not None:
            t = int(input(f"Que desea editar:\n1.Palabra\n2.Significado\n"))
            if t == 1:
                new = input(f"Ingrese la palabra editada: ")
                cursor.execute('select slang from tbl_slang where slang = "' + new.upper() + '";')
                val1 = cursor.fetchone()
                if val1 == None:
                    cursor.execute('update tbl_slang set slang = "'+new.upper()+'" where slang = "'+valor.upper()+'";')
                    conexion.commit()
                    print("Se edito la palabra con exito !!\n")
                    x = VolverMenu()
                else:
                    print("La palabra ingresada ya existe")
                    x = 0
            else:
                news = input(f"Ingrese el nuevo significado: ")
                cursor.execute('update tbl_slang set significado = "' + news + '" where slang = "' + valor.upper() + '";')
                conexion.commit()
                print("Se actualizo el significado con exito !!\n")
                x = VolverMenu()
        else:
            print("Esa palabra no existe en el diccionario.\n")
            x = VolverMenu()
    elif x == 3:
        valor = (input(f"Que palabra desea eliminar: "))
        cursor.execute('select slang from tbl_slang where slang = "' + valor.upper() + '";')
        val = cursor.fetchone()
        if val is not None:
            cursor.execute('delete from tbl_slang where slang = "' + valor.upper() + '";')
            print("Se elimina con exito la palabra "+valor.upper()+"\n")
            x = VolverMenu()
        else:
            print("La palabra " + valor.upper() + " no existe en el diccionario.\n")
            x = VolverMenu()
    elif x == 4:
        cursor.execute('select slang from tbl_slang;')
        val = cursor.fetchall()
        if val is not None:
            print("El listado de palabras en el diccionario son: ")
            for i in val:
                print(i[0])
            print("\n")
            x = VolverMenu()
        else:
            print("En este momento no existen palabras en el diccionario.")
            x = VolverMenu()
    elif x == 5:
        valor = (input(f"El significado de que palabra desea buscar: "))
        cursor.execute('select slang from tbl_slang where slang = "' + valor.upper() + '";')
        val = cursor.fetchone()
        if val is not None:
            print("Palabra: "+valor)
            cursor.execute('select significado from tbl_slang where slang = "' + valor.upper() + '";')
            val2 = cursor.fetchone()
            print("Significado: " + val2[0] + "\n")
            x = VolverMenu()
        else:
            print("Esa palabra no existe en el diccionario.")
            x = VolverMenu()


