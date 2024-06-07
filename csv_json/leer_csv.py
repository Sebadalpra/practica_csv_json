import os
import csv
from paquete.modulo import burbujeo

# ......... Obtengo la ruta actual del csv ------------

def get_path_actual(nombre_archivo):
    # __file__ me trae el directorio actual
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

ruta = get_path_actual("personas.csv")


# -------------- ABRO EL ARCHIVO CSV ORIGINAL -------------------------------

with open(ruta) as archivo:
    # Encabezado en lista
    lista_personas = []

    encabezado = archivo.readline().strip("\n").split(",")
    print(encabezado)

    # Contenido en lista
    for linea in archivo.readlines():

        dict_persona = {}

        linea = linea.strip("\n").split(",")
        print(f"linea 2| {linea}")

        # Asigna cada valor de la lista linea a las variables id, nombre, apellido, edad, correo y direccion.
        id, nombre, apellido, edad, correo, direccion = linea

        print(linea)

        dict_persona["id"] = int(id)
        dict_persona["nombre"] = nombre
        dict_persona["apellido"] = apellido
        dict_persona["edad"] = int(edad)
        dict_persona["correo"] = correo
        dict_persona["direccion"] = direccion
        lista_personas.append(dict_persona)
        

#  ------------------- MODIFICACIONES -------------------

burbujeo(lambda x, y: x["edad"] < y["edad"], lista_personas)


# --------------- CREACIÓN DEL NUEVO ARCHIVO CSV ------------

nueva_ruta = get_path_actual("personas_modificado.csv")

with open(nueva_ruta, "w", encoding="utf-8") as archivo_modificado:
    dato = csv.writer(archivo_modificado)

    # REUTILIZO EL ENCABEZADO
    dato.writerow(encabezado)

    # Que hay dentro de lista personas? diccionarios, entonces recorro cada uno de ellos usando dict_persona y se agregan como campos
    for dict_persona in lista_personas:
        dato.writerow([
            dict_persona["id"], 
            dict_persona["nombre"], 
            dict_persona["apellido"], 
            dict_persona["edad"], 
            dict_persona["correo"], 
            dict_persona["direccion"]
            ])

print(f"Archivo modificado se encuntra en: {nueva_ruta}")



