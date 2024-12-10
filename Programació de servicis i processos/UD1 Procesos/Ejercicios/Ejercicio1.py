# Crea un programa en Python que utilice la función fork para generar un número
# determinado de procesos hijos a partir de un proceso padre. Cada proceso hijo deberá
# imprimir su PID y el PID de su proceso padre

import  os

def padre():
    n = int(input("Introduce el número de hijos que quieres crear: "))
    for i in range(n):
        newpid = os.fork()
        if newpid == 0:
            hijo()
        else:
            pids = (os.getpid(), newpid)
            print("Padre: %d, Hijo: %d\n" % pids)
        reply = input("Pulsa 's' si quieres crear un nuevo proceso")
        if reply != 's':
            break

def hijo():
    print()
    os._exit(0)
padre()