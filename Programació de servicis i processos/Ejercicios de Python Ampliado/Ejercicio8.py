def contar_vocales(frase):
    vocales = ['a', 'e', 'i', 'o', 'u']
    contadora = 0
    contadore = 0
    contadori = 0
    contadoro = 0
    contadoru = 0

    for letra in frase:
        if letra.lower() == 'a' or letra.lower() == 'á':
            contadora += 1
        elif letra.lower() == 'e' or letra.lower() == 'é':
            contadore += 1
        elif letra.lower() == 'i' or letra.lower() == 'í':
            contadori += 1
        elif letra.lower() == 'o' or letra.lower() == 'ó':
            contadoro += 1
        elif letra.lower() == 'u' or letra.lower() == 'ú':
            contadoru += 1
    return f"Hay {contadora} 'a', {contadore} 'e', {contadori} 'i', {contadoro} 'o' y {contadoru} 'u'."

frase = input("Introduce una frase: ")
print(contar_vocales(frase))