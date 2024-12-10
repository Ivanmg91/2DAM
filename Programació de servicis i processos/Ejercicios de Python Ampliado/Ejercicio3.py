def filtrar_palabras(lista, n):
    for palabra in lista:
        if len(palabra) > n:
            print(palabra)

lista_palabras = ["Pablo", "Alejandro", "Ivan", "Marcos", "Carlos"]
filtrar_palabras(lista_palabras, 5)