#Escriba un programa que pida primero un número par y luego un número impar
#(positivos o negativos). En caso de que uno o los dos valores no sea correcto, se
#mostrará un único aviso.

"""
#NO ES LO Q PIDE
num_par = int(input("Introduce un numero par: "))
while num_par % 2 != 0:
    num_par = int(input("El numero introducido no es par. Introduce otro: "))

num_impar = int(input("Introduce un numero impar: "))
while num_impar % 2 == 0:
    num_impar = int(input("El numero introducido no es impar. Introduce otro: "))

print("Los numeros introducidos son: ", num_par, "y", num_impar)
"""

num_par = int(input("Introduce un numero par: "))
num_impar = int(input("Introduce un numero impar: "))

if num_par % 2 != 0:
    print("El primer numero no es par")
if num_impar % 2 == 0:
    print("El segundo numero no es impar")
if num_par % 2 != 0 & num_impar % 2 == 0:
    print("Ninguno de los dos numeros es correcto")
if num_par % 2 == 0 and num_impar % 2 != 0:
    print("Ambos numero son correctos")
