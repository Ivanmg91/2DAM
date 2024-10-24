# manipular ficheros binarios
contenido = archivo.read
# en lugar de readlines()

# para escribir
archivo.write(contenido)

# importante conocer la posicion en el ficheros
archivo.tell()
# que indica la cantidad de bytes desde el comienzo del archivo

# modificar la posición actual
archivo.seek(inicio, desde)
# permite desplazarse una cantidad inicio de bytes en el archivo, 
# contando desde el comienzo del archivo, desde la posición actual o desde el final

