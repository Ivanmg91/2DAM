#Escribir un programa, llamado cut.py, que dado un archivo de texto, un
#delimitador, y una lista de campos, imprima solamente esos campos, separados por ese
#delimitador.

delimitador=";"
campos=["provincia", "poblacion" , "codigopostalid", "lat", "lon"]
campos_para_imprimir=[]
string_concatenar=""

#Bucle q recorra la lista preguntando si quiere imprimir el campo | SI NO HAY RESPUESTA ES COMO Q NO
for i in range(len(campos)):
    siono=input("Quieres imprimir el campo " + campos[i] + "? (S/N)")
    #Si dice S lo añado a la lista de campos para imprimir
    if siono=="S":
        campos_para_imprimir.append(campos[i])

fichero=open("listado-codigos-postales.csv")
for a in fichero:
    linea=fichero.readline().strip()
    linea_separada=linea.split(delimitador)

    for i in range(len(campos)):
        #Bucle q recorra el array de campos_para_imprimir, si coincide el campo de el primer bucle con alguno de campos_para_imprimir se concatena a un string
        for j in range(len(campos_para_imprimir)):
            if campos[i]==campos_para_imprimir[j]:
                string_concatenar+=linea_separada[i] + delimitador

    print(string_concatenar)

fichero.close()
