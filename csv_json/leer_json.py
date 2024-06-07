import json 
import os
from paquete.modulo import * 

# ......... Obtengo la ruta actual del json ------------

def get_path_actual(nombre_archivo):
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

ruta = get_path_actual("personas.json")



# --------------- ABRO EL ARCHIVO JSON ORIGINAL ---------------------------

# Abro el archivo JSON a partir de la ruta y le doy el nombre de archivo
with open(ruta,"r",encoding = "utf-8") as archivo:

    # Verifico que haya abierto. Si está en false es porque aun no se cerró
    print(f"{archivo.closed}")   

    # Cargo el archivo (personas.json) y lo guardo en la variable personas_json
    personas_json = json.load(archivo)

for persona in personas_json:
    print(persona)



# -------------------- MODIFICACIONES ---------------------------------

# Multiplico las edaes * 2
for i in range(len(personas_json)):
    personas_json[i]["edad"] = personas_json[i]["edad"] * 2
    
# Ordenamiento de mayor a menor
burbujeo(lambda x, y: x["edad"] < y["edad"], personas_json)



# ------------- CREO EL NUEVO ARCHIVO JSON MODIFICADO ----------------

new_ruta = get_path_actual("personas_modificado.json")

with open(new_ruta, "w", encoding = "utf-8") as archivo:

    # Convertir el codigo Python en formato JSON
    json.dump(personas_json, archivo, ensure_ascii=False, indent=4)

print(f"Archivo guardado en: {new_ruta}")