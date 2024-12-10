# Busca todos los nombre independientemente de si empiezan por mayúscula o minúscula e independientemente si buscas por mayúscula o minúscula
def buscalosqempiezarpor(lista, letra):
    listanombres = []
    for nombre in lista:
        if nombre[0] == letra.lower() or nombre[0] == letra.upper():
            listanombres.append(nombre)
    return listanombres


listanombres = ["Juan", "Ana", "Luis", "Pedro", "Marta", "Alberto", "Raquel", "Sara", "Jorge", "Lucia", "laura", "Antonio", "Andrea", "Raul", "Rosa", "Ramon", "Rocio", "Ricardo", "Roberto", "Ruben", "Ruth", "Rebeca", "Rafael"]

n = int(input("1. Buscar por a\n2. Buscar por letra a elegir\n3. Salir"))
while n != 3:
    if n == 1:
        print("Buscaré todos los que empiecen por la letra a: ")
        print(buscalosqempiezarpor(listanombres, "A"))
        n = int(input("1. Buscar por a\n2. Buscar por letra a elegir\n3. Salir"))

    elif n == 2:
        letra = input("Introduce la letra por la que quieres buscar: ")
        print(buscalosqempiezarpor(listanombres, letra))
        n = int(input("1. Buscar por a\n2. Buscar por letra a elegir\n3. Salir"))

    else:
        print("Opción no válida")
        n = int(input("1. Buscar por a\n2. Buscar por letra a elegir\n3. Salir"))