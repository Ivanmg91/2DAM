class Lista:
    def __init__(self, lista):
        self.lista = lista

    def ordenar(self):
        return sorted(self.lista)

    def buscaparejas(self, resultado):
        posicion1 = 0
        posicion2 = 0

        for i in self.lista:
            for j in self.lista:
                if i+j == resultado:
                    posicion1 = self.lista.index(i) + 1
                    posicion2 = self.lista.index(j) + 1
                    return (posicion1, posicion2)


numeros = [10,20,10,40,50,60,70]
lista = Lista(numeros)
print(lista.buscaparejas(50))