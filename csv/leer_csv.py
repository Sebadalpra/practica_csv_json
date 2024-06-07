import os
import csv

def get_path_actual(nombre_archivo):
    # __file__ me trae el directorio actual
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

ruta = get_path_actual("personas.csv")

with open(ruta) as archivo:
    # Encabezado en lista
    lista = []

    encabezado = archivo.readline().strip("\n").split(",")
    print(encabezado)

    # Contenido en lista
    for linea in archivo.readlines():
        persona = {}

        linea = linea.strip("\n").split(",")
        
        id, nombre, apellido, edad, correo, direccion = linea

        persona["id"] = int(id)
        persona["nombre"] = nombre
        persona["apellido"] = apellido
        persona["edad"] = int(edad)
        persona["correo"] = correo
        persona["direccion"] = direccion
        lista.append(persona)
    
for persona in lista:
    print(persona)

nueva_ruta = get_path_actual("nuevo_archivo.csv")

with open("./hola_loco.csv", "w", encoding="utf-8") as archivo_modificado:
    dato = csv.writer(archivo_modificado)

print("terminamos")

