import os
import csv
from functions_heroes import * 

def get_path_actual(nombre_archivo):
    # __file__ me trae el directorio actual
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

ruta = get_path_actual("personas.csv")

with open(ruta) as archivo:
    # Encabezado en lista
    personas = []

    encabezado = archivo.readline().strip("\n").split(",")
    print(encabezado)

    # Contenido en lista
    for linea in archivo.readlines():
        persona = {}

        linea = linea.strip("\n").split(",")
        print(linea)
        
        id, nombre, apellido, genero, edad, peso = linea

        persona["id"] = int(id)
        persona["nombre"] = nombre.capitalize()
        persona["apellido"] = apellido
        persona["genero"] = genero
        persona["edad"] = int(edad)
        persona["peso"] = float(peso)
        personas.append(persona)

    promedio_edades_male = filtrar_lista(lambda per: per["genero"] == "Male",personas)
    promedio_edades = promedio_lista(filtrar_atributo("edad",promedio_edades_male))
    
#///////////////////////////////////////////////////////////////////////

nueva_ruta = get_path_actual("personas_nombres_mayuscula.csv")
# Abrir el nuevo archivo en modo escritura
with open(nueva_ruta, mode='w', newline='', encoding = "utf-8") as archivo_modificado:
    escritor_csv = csv.writer(archivo_modificado)
    # Escribir el encabezado
    escritor_csv.writerow(encabezado)
    
    # Escribir los datos modificados
    for persona in promedio_edades_male:
        escritor_csv.writerow([persona["id"], persona["nombre"], persona["apellido"], persona["genero"], persona["edad"], persona["peso"]])
    lista_msj = [f"El promedio de las edades male {promedio_edades}","El promedio de las edades male 10"]
    for elem in lista_msj:
        escritor_csv.writerow([elem])
print(f"Archivo modificado guardado en: {nueva_ruta}")
