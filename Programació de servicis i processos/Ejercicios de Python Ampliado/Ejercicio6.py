def imprimemayoresa20(diccionario):
    listapersonas = []
    for persona in diccionario:
        if diccionario[persona] > 20:
            listapersonas.append(persona)
    return listapersonas

personasyedad = {}

personas = ["Pablo", "Alejandro", "Ivan", "Marcos", "Carlos", "Alberto", "David", "Jorge", "Andres", "Samuel"]

for persona in personas:
    edad = int(input(f"Introduce la edad de {persona}: "))
    personasyedad[persona] = edad

print(imprimemayoresa20(personasyedad))