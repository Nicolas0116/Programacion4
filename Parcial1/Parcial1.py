import sqlite3
import os

APP_PATH = os.getcwd()
DB_PATH = APP_PATH + 'Parcial1.db'

conexion = sqlite3.connect(DB_PATH)
cursor = conexion.cursor()

cursor.execute("Drop table if exists TBL_Inventario")
conexion.commit()
cursor.execute(""" 
    Create table if not exists TBL_Inventario(
        Id text primary key,
        articulo text,
        cantidad int
    )  
""")
conexion.commit()

inventario = [("1","MANZANAS",20)]
cursor.executemany("insert into TBL_Inventario values (?,?,?);",inventario)
conexion.commit()

def VolverMenu():
    z = int(input(f"1.Volver al menu principal\n2.Salir\n"))
    if z == 1:
        x = 0
    else:
        x = 5
    return x

x = 0


while x < 5:
    if x == 0:
        print("***************** Sistema de inventario **********************\n")
        x = int(input(f"Menu principal \n1.Agregar aritculo\n2.Busqueda de articulo\n3.Editar cantidad"
                      f"\n4.Eliminar articulo\n5.Salir\n"))
    elif x == 1:
        valor = (input(f"Que articulo desea ingresar: "))
        cursor.execute('select articulo from TBL_Inventario where articulo = "' + valor.upper() + '";')
        val = cursor.fetchone()
        if val == None:
            y = input(f"Cantidad: ")
            cursor.execute("select max(id)+1 from TBL_Inventario")
            m = cursor.fetchone()
            dato = [m[0], valor.upper(), y]
            cursor.execute("insert into TBL_Inventario values (?,?,?)", dato)
            conexion.commit()
            print("Se ingreso el articulo con exito !!!\n")
            x = VolverMenu()
        else:
            print("Esa articulo ya existe en el inventario\n")
            x = VolverMenu()
    elif x == 2:
        valor = (input(f"Que articulo desea buscar: "))
        cursor.execute('select articulo from TBL_Inventario where articulo = "' + valor.upper() + '";')
        val = cursor.fetchone()
        if val is not None:
            cursor.execute('select cantidad from TBL_Inventario where articulo = "' + valor.upper() + '";')
            val1 = cursor.fetchone()
            # r = val1[0]
            print("Del articulo " + valor + " registran " + str(val1[0]) + " unidades.\n")
            x = VolverMenu()
        else:
            print("Ese articulo no existe en el inventario.\n")
            x = VolverMenu()
    elif x == 3:
        valor = (input(f"De cual articulo desea actualizar la cantidad: "))
        cursor.execute('select articulo from TBL_Inventario where articulo = "' + valor.upper() + '";')
        val = cursor.fetchone()
        if val is not None:
            new = input(f"Ingrese la nueva cantidad: ")
            cursor.execute('update TBL_Inventario set cantidad = "'+new.upper()+'" where articulo = "'+valor.upper()+'";')
            conexion.commit()
            print("Se actualizo la cantidad con exito !!\n")
            x = VolverMenu()
        else:
            print("El articulo ingresado no existe en el inventario.")
            x = 0
    elif x == 4:
        valor = (input(f"Que articulo desea eliminar: "))
        cursor.execute('select articulo from TBL_Inventario where articulo = "' + valor.upper() + '";')
        val = cursor.fetchone()
        if val is not None:
            cursor.execute('delete from TBL_Inventario where articulo = "' + valor.upper() + '";')
            print("Se elimina con exito el articulo "+valor.upper()+"\n")
            x = VolverMenu()
        else:
            print("El articulo " + valor.upper() + " no existe en el inventario.\n")
            x = VolverMenu()
