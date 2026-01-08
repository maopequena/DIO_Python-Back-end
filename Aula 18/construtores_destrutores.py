class Cachorro:
    def __init__(self, nome, raca, cor, acordado=True):
        print("Iniciando a classe...")
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe...")

    def latir(self):
        print("Au au!")


def criar_cachorro():
    c = Cachorro("Zeus", "dálmata", "branco e preto", False)
    print(c.nome)


c1 = Cachorro("Chappie", "SRD", "amarelo")
c1.latir()

print("Olá, mundo!")

del c1  #! sem essa linha, as duas instâncias são removidas no final da execução do código, com ela, a instância de c1 é removida aqui, antes dos próximos 3 "Olá, mundo!".

print("Olá, mundo!")
print("Olá, mundo!")
print("Olá, mundo!")

criar_cachorro()
