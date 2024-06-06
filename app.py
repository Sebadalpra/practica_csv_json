from data_stark import *
from paquete.modulo import *

""" 
Analizar detenidamente el set de datos
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
la altura del mismo
D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
F. Recorrer la lista y determinar la altura promedio de los superhéroes
(PROMEDIO)
G. Informar cual es la identidad del superhéroe asociado a cada uno de los
indicadores anteriores (MÁXIMO, MÍNIMO)
H. Calcular e informar cual es el superhéroe más y menos pesado.
I. Ordenar el código implementando una función para cada uno de los valores
informados.
J. Construir un menú que permita elegir qué dato obtener
 """

def imprimir_lista_elementos(lista):
    for el in lista:
        print(el)

# PUNTO A
def mapear_lista_valor(lista, clave):
    # Es necesario hacer una lista vacia ya que no puedo retornar todos los valores en cada iteracion. Si retorno al final solo obtengo el ultimo valor.
    lista_retorno = []
    for heroe in lista:
        valor = heroe[clave]
        lista_retorno.append(valor)
    return lista_retorno

# PUNTO C
def mapear_lista_valores(lista, clave):
    # Es necesario hacer una lista vacia ya que no puedo retornar todos los valores en cada iteracion. Si retorno al final solo obtengo el ultimo valor.
    lista_retorno = []
    for heroe in lista:
        valor = heroe[clave]
        lista_retorno.append(valor)
    return lista_retorno


while True:
    opcion = input("Elija una opción: ")
    match opcion:
        case "A":
            resultado = mapear_lista_valor(lista_personajes, "nombre")
            imprimir_lista_elementos(resultado)
        case "B":
            pass
        case "C":
            pass
        case "D":
            pass
        case "E":
            pass
        case "F":
            pass
        case "G":
            pass
        case "H":
            pass
        case "I":
            pass
