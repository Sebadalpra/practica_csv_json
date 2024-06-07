import json 
import os
from functions_heroes import * 

def get_path_actual(nombre_archivo):
    # __file__ me trae el directorio actual
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

ruta = get_path_actual("personas.json")


# archivo = open("./curso_uno/03-06/personas.json","r",encoding = "utf-8")
# personas = json.load(archivo)
# archivo.close()

with open(ruta,"r",encoding = "utf-8") as archivo:
    """
        Abro el archivo
    """
    print(archivo.closed)
    personas = json.load(archivo)

for persona in personas:
    print(persona)

print("................................................................................")

for i in range(len(personas)):
    personas[i]["edad"] = personas[i]["edad"] * 2
    
lista_machos = filtrar_lista(lambda per: per["genero"] == "Male",personas)

new_ruta = get_path_actual("personas_macho.json")
with open(new_ruta, "w", encoding = "utf-8") as archivo:
    """
        Guardo el archivo
        En caso de existir te borra lo sobreescribe lo anterior
    """
    
    json.dump(lista_machos,archivo,indent=4)