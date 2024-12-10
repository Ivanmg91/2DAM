#Escribir un programa, llamado head que reciba un archivo y un número N e
#imprima las primeras N líneas del archivo.

fichero=open("fundacion.txt")
numero=input("Hasta que linea quieres leer: ")

# La variable num es para hacer q solo cuente en el bucle las lineas q tienen contenido
Numero=int(numero)
num=int(0)

while num<Numero:
    linea=fichero.readline().strip()
    # Si la linea no esta vacía la imprime
    if linea!="":
        print(linea)
        num+=1


fichero.close()