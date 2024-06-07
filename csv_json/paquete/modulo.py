def burbujeo(function, lista: list):
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if function(lista[i], lista[j]):
                # swap
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

