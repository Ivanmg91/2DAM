#Escribir en el archivo
archivo=open("archivo.txt", "w")
archivo.write("Hola\n")
archivo.write("Mundo\n")
archivo.write("Python\n")
archivo.close()

#Imprimir por lineas
archivo=open("archivo.txt")

linea = archivo.readline().strip()
i = 0
while linea != '':
    
    i += 1
    print(i,linea)
    
    #procesar linea
    linea=archivo.readline().strip()
    
archivo.close()