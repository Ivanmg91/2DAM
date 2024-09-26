delimitador = ";"
campos = ["provincia", "poblacion", "codigopostalid", "lat", "lon"]
campos_para_imprimir = []

# Bucle que recorre la lista preguntando si quiere imprimir el campo | SI NO HAY RESPUESTA ES COMO QUE NO
for campo in campos:
    siono = input(f"Quieres imprimir el campo {campo}? (S/N) ")
    # Si dice S lo añado a la lista de campos para imprimir
    if siono.upper() == "S":
        campos_para_imprimir.append(campo)

# Abrir el archivo para lectura
with open("listado-codigos-postales.csv", "r") as fichero:
    # Leer la primera línea que contiene los nombres de los campos
    encabezados = fichero.readline().strip().split(delimitador)

    # Crear un diccionario para mapear los nombres de los campos a sus índices
    indices_campos = {campo: index for index, campo in enumerate(encabezados)}

    # Leer el resto del archivo línea por línea
    for linea in fichero:
        linea_separada = linea.strip().split(delimitador)
        string_concatenar = []

        # Añadir los campos seleccionados a la lista de concatenación
        for campo in campos_para_imprimir:
            if campo in indices_campos:
                string_concatenar.append(linea_separada[indices_campos[campo]])

        # Imprimir la línea concatenada con el delimitador
        print(delimitador.join(string_concatenar))