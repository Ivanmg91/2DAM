class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}")

    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False

persona = Persona("Juan", 25, "12345678Z")
persona.mostrar()
print(persona.esMayorDeEdad())