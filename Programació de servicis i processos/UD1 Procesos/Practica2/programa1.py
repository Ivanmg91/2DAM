import multiprocessing
import os
import time

def abuelo():
    print(f"Soc l'avi (PID: {os.getpid()}, fill de {os.getppid()})")

def padre():
    print(f"Soc el pare (PID: {os.getpid()}, fill de {os.getppid()})")
    nieto1 = multiprocessing.Process(target=nieto)
    nieto2 = multiprocessing.Process(target=nieto)
    nieto1.start()
    nieto2.start()
    nieto1.join()
    nieto2.join()
    print(f"Soc el pare (PID: {os.getpid()}, fill de {os.getppid()})")

def nieto():
    print(f"Soc el net (PID: {os.getpid()}, fill de {os.getppid()})")

if __name__ == "__main__":
    abuelo_proc = multiprocessing.Process(target=abuelo)
    abuelo_proc.start()
    abuelo_proc.join()

    padre_proc = multiprocessing.Process(target=padre)
    padre_proc.start()
    padre_proc.join()

    abuelo_proc = multiprocessing.Process(target=abuelo)
    abuelo_proc.start()
    abuelo_proc.join()

    print("Finalitzat tot el procés")