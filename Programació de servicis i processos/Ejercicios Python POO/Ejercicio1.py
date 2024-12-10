class Numero:
    def __init__(self, numero):
        self.numero = numero

    def pasar_a_romano(self):
        numeros = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        romanos = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        num = self.numero
        i = 0
        while num> 0:
            for _ in range(num // numeros[i]):
                roman_num += romanos[i]
                num -= numeros[i]
            i += 1
        return roman_num

numero = Numero(int(input("Introduce un número: ")))
print(numero.pasar_a_romano())