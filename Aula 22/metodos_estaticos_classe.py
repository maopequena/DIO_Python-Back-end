from datetime import datetime, date

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_nascimento(cls, nome, ano):
        idade = date.today().year - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior(idade):
        return idade >= 18

p = Pessoa.criar_de_nascimento("Maria", 1995)
print(p.nome, p.idade)
print(Pessoa.e_maior(p.idade))

p1 = Pessoa.criar_de_nascimento("Lizandra", 1979)
print(p1.nome, p1.idade)
print(Pessoa.e_maior(p1.idade))

p2 = Pessoa.criar_de_nascimento("Mia", 2015)
print(p2.nome, p2.idade)
print(Pessoa.e_maior(p2.idade))