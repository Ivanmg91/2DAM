import sys

fichero = "./listado1"
fichero_oculto = "./listado_lopd"

# Comprobar si se ha introducido un argumento
if len(sys.argv) != 2:
    # n representa el número de caracteres ocultos del DNI
    n = 5
else:
    n = int(sys.argv[1])

# Guardar en una lista el todos los nombres y DNI
lista_nombresdni = []
lista_meterenlista = []
open(fichero, "r")
for linea in open(fichero, "r"):
    lista_meterenlista = linea.strip().split(" ")
    lista_nombresdni.append(lista_meterenlista)

# Encriptar los DNI con una funcion de encrpitacion
# El DNI se encripta ocultando los últimos n caracteres
# El nombre no se encripta
# Los apellidos se encriptan dejando las dos primeras letras sin ocultar
def encriptar_dni(lista, n):
    for i in lista:

        if len(i) == 4:
            i[0] = i[0][:-n] + "*" * n
            i[2] = i[2][:2] + "*" * (len(i[1]) - 2)
            i[3] = i[3][:2] + "*" * (len(i[1]) - 2)

        elif len(i) == 5:
            i[0] = i[0][:-n] + "*" * n
            i[3] = i[3][:2] + "*" * (len(i[1]) - 2)
            i[4] = i[4][:2] + "*" * (len(i[1]) - 2)

    return lista

# Guardar en un fichero los nombres y DNI encriptados
open(fichero_oculto, "w")
for i in encriptar_dni(lista_nombresdni, n):
    if len(i) == 4:
        open(fichero_oculto, "a").write(i[0] + " " + i[1] + " " + i[2] + " " + i[3] + "\n")
    elif len(i) == 5:
        open(fichero_oculto, "a").write(i[0] + " " + i[1] + " " + i[2] + " " + i[3] + " " + i[4] + "\n")

print("Fichero creado con éxito")
