#Escribir un programa, llamado grep.py que reciba una expresión y un archivo e
#imprima las líneas del archivo que contienen la expresión recibida.

imprimir=input("Escribe lo que quieres buscar: ")

with open("fundacion.txt", "r") as fichero:
    for a in fichero:
        if imprimir in a:
            print(a)