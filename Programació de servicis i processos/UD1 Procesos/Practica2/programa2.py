import multiprocessing

def hijo():
    print(f"Soy el hijo. Valor variable {valor - 5}")

def padre(valor):
    hijo1 = multiprocessing.Process(target=hijo)
    hijo1.start()
    hijo1.join()
    print(f"Soy el padre. Valor variable {valor + 5}")

if __name__ == "__main__":
    valor = 6
    padre(valor)

# Creamos el proceso padre que inicia el proceso hijo. Luego el padre espera a que el hijo termine y muestra su resultado.
# El hijo muestra el valor de la variable valor - 5 y el padre muestra el valor de la variable valor + 5.