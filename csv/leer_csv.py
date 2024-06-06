import os

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
        print(linea)
        
        id, nombre, apellido, edad, correo, direccion = linea
        persona["id"] = id(int)
        persona["nombre"] = nombre
        persona["edad"] = edad(int)
        persona["correo"] = correo
        persona["direccion"] = direccion
        lista.append(persona)
    
for persona in lista:
    print(persona)

