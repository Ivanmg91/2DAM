archivo=open("archivo.txt")

linea = archivo.readline().strip()
i = 0
while linea != '':
    
    i += 1
    print(i,linea)
    
    #procesar linea
    linea=archivo.readline().strip()
    
archivo.close()