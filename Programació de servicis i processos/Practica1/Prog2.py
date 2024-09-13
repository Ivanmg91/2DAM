#Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de
#una persona y que calcule su índice de masa corporal (imc). (imc = peso / altura²)

peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = float(peso / altura ** 2)

print("IMC: ", imc)