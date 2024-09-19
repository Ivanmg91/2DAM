class Persona:
    def __init__(self):
        self.cadena = ""

    def get_string(self):
        self.cadena = input("Introduce una cadena: ")

    def print_string(self):
        print(self.cadena.upper())

    def rev_string(self):
        lista_palabras = self.cadena.split(" ")
        lista_palabras.reverse()
        print(" ".join(lista_palabras))

persona = Persona()
persona.get_string()
persona.print_string()
persona.rev_string()