import puntajes_csv

valores = [("Pepe", 108, "4:16"), ("Juana", 2315, "8:42")]
puntajes_csv.guardar_puntajes("puntajes.txt", valores)
recuperado = puntajes_csv.recuperar_puntajes("puntajes.txt")

print(recuperado)

# [('Pepe', 108, '4:16'), ('Juana', 2315, '8:42')]