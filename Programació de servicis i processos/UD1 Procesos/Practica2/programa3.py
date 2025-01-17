import multiprocessing
import os

def procesoA(valor1, valor2):
    print(f"Soy el proceso A (Raíz). PID: {os.getpid()}, No tengo padre.")
    procesoC_proc = multiprocessing.Process(target=procesoC, args=(os.getpid(),))
    procesoC_proc.start()
    procesoC_proc.join()

    procesoG_proc = multiprocessing.Process(target=procesoG, args=(os.getpid(),))
    procesoG_proc.start()
    procesoG_proc.join()

    procesoB_proc = multiprocessing.Process(target=procesoB, args=(valor1, valor2, os.getpid()))
    procesoB_proc.start()
    procesoB_proc.join()

    procesoE_proc = multiprocessing.Process(target=procesoE, args=(valor1, valor2, os.getpid()))
    procesoE_proc.start()
    procesoE_proc.join()

def procesoB(valor1, valor2, parent_pid):
    print(f"Soy el proceso B (Nivel 2). PID: {os.getpid()}, Padre PID: {parent_pid}")
    procesoD_proc = multiprocessing.Process(target=procesoD, args=(valor1, valor2, os.getpid()))
    procesoD_proc.start()
    procesoD_proc.join()


def procesoC(parent_pid):
    print(f"Soy el proceso C (Nivel 2). PID: {os.getpid()}, Padre PID: {parent_pid}")

def procesoD(valor1, valor2, parent_pid):
    print(f"Soy el proceso D (Nivel 2). PID: {os.getpid()}, Padre PID: {parent_pid}")
    print(f"Operación: {valor1} / {valor2} = {valor1 / valor2}")

def procesoE(valor1, valor2, parent_pid):
    print(f"Soy el proceso E (Nivel 3). PID: {os.getpid()}, Padre PID: {parent_pid}")
    print(f"Operación: {valor1} + {valor2} = {valor1 + valor2}")

    procesoF_proc = multiprocessing.Process(target=procesoF, args=(valor1, valor2, os.getpid()))
    procesoF_proc.start()
    procesoF_proc.join()

def procesoF(valor1, valor2, parent_pid):
    print(f"Soy el proceso F (Nivel 3). PID: {os.getpid()}, Padre PID: {parent_pid}")
    print(f"Operación: {valor1} - {valor2} = {valor1 - valor2}")

def procesoG(parent_pid):
    print(f"Soy el proceso G (Nivel 3). PID: {os.getpid()}, Padre PID: {parent_pid}")
    print(f"Operación: {valor1} * {valor2} = {valor1 * valor2}")

if __name__ == "__main__":
    valor1 = int(input("Introduce el primer valor entero positivo: "))
    valor2 = int(input("Introduce el segundo valor entero positivo: "))

    procesoA(valor1, valor2)