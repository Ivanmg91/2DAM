import EjercicioA1
import Ejercicio4

class CuentaJoven(EjercicioA1.Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def esTitularValido(self):
        if self.titular.get_edad() < 25 and self.titular.esMayorDeEdad():
            return True
        else:
            return False

    def retirar(self, cantidad):
        if self.esTitularValido():
            if cantidad > 0:
                self.cantidad -= cantidad
        else:
            print("No puedes retirar dinero porque no eres mayor de 25 años")

    def mostrar(self):
        print
        super().mostrar()
        print(f"Cuenta Joven: {self.bonificacion}")

cuenta_joven = CuentaJoven(Ejercicio4.Persona("Alberto", 24, "12345678Z"), 1000, 50)
cuenta_joven.mostrar()
cuenta_joven.ingresar(500)
cuenta_joven.mostrar()
cuenta_joven.retirar(200)
cuenta_joven.mostrar()