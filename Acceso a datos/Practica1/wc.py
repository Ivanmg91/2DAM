#Escribir un programa, llamado wc.py que reciba un archivo, lo procese e
#imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el
#archivo.

lineas = int(0)
palabras = int(0)
caracteres = int(0)

with open("fundacion.txt", "r") as fichero:
    for a in fichero:
        # contar las lineas
        lineas = lineas + 1

        # contar las palabras
        spliteao = a.split(" ")
        palabras += len(spliteao)

        # contar los caracteres
        caracteres += len(a)



print(lineas)
print(palabras)
print(caracteres)
