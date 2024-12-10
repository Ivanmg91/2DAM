def rot13(texto):
    resultado = []
    for char in texto:
        if 'a' <= char <= 'z':
            resultado.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            resultado.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            resultado.append(char)
    return ''.join(resultado)

archivo_origen = input("Nombre del archivo de origen: ")
archivo_destino = input("Nombre del archivo de destino: ")

with open(archivo_origen, 'r') as origen, open(archivo_destino, 'w') as destino:
    for linea in origen:
        destino.write(rot13(linea))

print("Archivo cifrado correctamente")

