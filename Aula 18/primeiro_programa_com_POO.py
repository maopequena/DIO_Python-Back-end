class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Honk-honk")

    def correr(self):
        print("correndo")

    def parar(self):
        print("parando")

    # def __str__(self):
    #     return f"Esta bicicleta tem as seguintes características:\n\tcor: {self.cor},\n\tmodelo: {self.modelo},\n\tano: {self.ano},\n\tvalor: R$ {self.valor}."

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


bicicleta1 = Bicicleta("preta", "BM123", 2010, 1200.00)
bicicleta2 = Bicicleta("roxa", "BM456", 2015, 1400.00)
bicicleta3 = Bicicleta("azul", "BM789", 2020, 1800.00)

bicicleta1.buzinar()  # Pode ser escrito como Bicicleta.buzinar(bicicleta1)
bicicleta2.parar()  # Pode ser escrito como Bicicleta.parar(bicicleta2)
bicicleta3.correr()  # Pode ser escrito como Bicicleta.correr(bicicleta3)

print(bicicleta1.cor, bicicleta1.modelo, bicicleta1.ano, bicicleta1.valor)
print(bicicleta2.cor, bicicleta2.modelo, bicicleta2.ano, bicicleta2.valor)
print(bicicleta3.cor, bicicleta3.modelo, bicicleta3.ano, bicicleta3.valor)

print(bicicleta1)
print(bicicleta2)
print(bicicleta3)
