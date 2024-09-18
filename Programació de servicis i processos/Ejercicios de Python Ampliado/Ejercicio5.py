def cuantosanostiene (ano):
    return 2024 - ano

def cuantoscumplira (ano):
    return cuantosanostiene(ano) + 1

anoestas = int(input("Introduce el año en el que estás: "))
personas = []
tieneycumplira = []

print("A continuación escribe el nombre y año de nacimiento de tres personas (Ej. Pablo 1990):")
for i in range(3):
    persona = input().split(" ")
    personas.append(persona)

    tiene = cuantosanostiene(int(persona[1]))
    cumplira = cuantoscumplira(int(persona[1]))
    tieneycumplira.append((tiene, cumplira))

#Imprimir el nombre, cuantos años tiene y cuantos cumplira de cada persona
for i in range(3):
    print(f"{personas[i][0]} tiene {tieneycumplira[i][0]} años y cumplirá {tieneycumplira[i][1]} años")