def mas_larga(lista):
    return max(lista, key=len)

lista_palabras = ["Pablo", "Alejandro", "Ivan", "Marcos", "Carlos"]
print(mas_larga(lista_palabras))