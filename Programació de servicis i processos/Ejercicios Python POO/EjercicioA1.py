from attr.validators import instance_of

import Ejercicio4

class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
        isinstance(titular, Ejercicio4.Persona)

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular.get_nombre()}\nCantidad: {self.cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad

cuenta = Cuenta(Ejercicio4.Persona("Juan", 25, "12345678Z"), 1000)
cuenta.mostrar()
cuenta.ingresar(500)
cuenta.mostrar()
cuenta.retirar(200)
cuenta.mostrar()