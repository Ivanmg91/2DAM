archivo = open("archivo.txt")

# tres formas

línea=archivo.readline()
while línea != '':
    # procesar línea
    línea=archivo.readline()
    print(linea)

for línea in archivo:
    # procesar línea
    print(linea)

líneas = archivo.readlines()
for línea in líneas:
    # procesar línea
    print(linea)

# liberar memoria siempre
# ficheros pequeños tienen un pequeño impacto
# con ficheros grandes cuidado con la memoria
archivo.close()
