#Escribir un programa, llamado cp.py, que copie todo el contenido de un archivo
#a otro, de modo que quede exactamente igual.

archivo1=input("Nombre del archivo del que quieres copiar el contenido: ")
archivo2=input("Nombre del archivo al que quieres copiar el contenido: ")

archivo=open(archivo1)
copia=open(archivo2, "w")

contenido=archivo.read()
copia.write(contenido)

archivo.close()
copia.close()

print("Contenido copiado correctamente")