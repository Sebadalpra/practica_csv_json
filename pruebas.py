import os

# Abrir archivos
# ------------ FORMA 1
try:    
    archivo = open("./prueba1.txt", "r", encoding="utf-8")
except:
    raise FileNotFoundError ("No se encuentra el archivo")

datos = archivo.read()

archivo.close()

print(datos)

# ------------ FORMA 2

with open("./prueba1.txt", "r", encoding="utf-8") as archivo:

    datos = archivo.read()
    print(datos)

print("fin")



cadena = "      HOLA MUNDO      "
cadena = cadena.strip()
print(cadena)

with open("./hola_loco.txt", "w", encoding="utf-8") as archivo:
    dato = archivo.write("Buenos díassssss")

print("terminamos")


lista = [2, 3, 5, 1]

tam = len(lista)


for i in range(tam -1):
    for j in range(i + 1, tam):
        if lista[i] < lista[j]:
            # swap
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(lista)

