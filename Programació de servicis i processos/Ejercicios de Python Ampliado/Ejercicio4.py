def cuantasmayustiene(palabra):
    mayus = 0
    for letra in palabra:
        if letra.isupper():
            mayus += 1
    return mayus

palabra = input("Introduce una palabra: ")
print(cuantasmayustiene(palabra))