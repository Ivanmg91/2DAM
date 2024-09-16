import puntajes

valores = [("Pepe", 108, "4:16"), ("Juana", 2315, "8:42")]
puntajes.guardar_puntajes("puntajes.txt", valores)
recuperado = puntajes.recuperar_puntajes("puntajes.txt")

print(recuperado)