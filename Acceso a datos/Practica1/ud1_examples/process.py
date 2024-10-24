#Imprime las líneas de un archivo con su número

archivo = open("archivo.txt")
i = 1

for linea in archivo:
    linea = linea.rstrip("\\n")
    print(" %4d: %s" % (i, linea))
    i+=1

archivo.close()

# alternativa
archivo = open("archivo.txt")

for i, línea in enumerate(archivo):
    línea = línea.rstrip("\\n")
    print(" %4d: %s" % (i, línea))

archivo.close()