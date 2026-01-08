class Veiculo:
    def __init__(self, cor, ano, placa, eixos, combustivel, licenciamento=True):
        print("Iniciando a classe Veículo")
        self.cor = cor
        self.ano = ano
        self.placa = placa
        self.eixos = eixos
        self.combustivel = combustivel
        self.licenciamento = licenciamento

    def buzinar(self):
        print("Honk!")

    def ligar(self):
        print("Girando ignição")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __del__(self):
        print("Excluindo a classe Veículo")


class Motocicleta(Veiculo):
    def __init__(self, cor, ano, placa, eixos, combustivel, licenciamento, bau=False):
        super().__init__(cor, ano, placa, eixos, combustivel, licenciamento)
        self.bau = bau

    def para_trabalho(self):
        print(f'A moto {"é" if self.bau else "não é"} para trabalho.')


class Carro(Veiculo):
    def __init__(
        self,
        cor,
        ano,
        placa,
        eixos,
        combustivel,
        licenciamento,
        porta_malas,
        cargueiro_superior=False,
        cacamba=False,
    ):
        super().__init__(cor, ano, placa, eixos, combustivel, licenciamento)
        self.porta_malas = porta_malas
        self.cargueiro_superior = cargueiro_superior
        self.cacamba = cacamba

    def aceita_carga(self):
        print(
            f'Este carro {"aceita" if (self.porta_malas != "" or self.cargueiro_superior or self.cacamba)  else "não aceita"} carga pesada.'
        )


class Caminhao(Veiculo):
    def __init__(
        self, cor, ano, placa, eixos, combustivel, licenciamento, carregado=True
    ):
        super().__init__(cor, ano, placa, eixos, combustivel, licenciamento)
        self.carregado = carregado

    def carga(self):
        print(f'{"Sim, " if self.carregado else "Não"} tenho carga.')


moto = Motocicleta("preta", 2010, "ABC-1234", 1, "álcool", False, False)

carro = Carro("prata", 2006, "DXT-3998", 2, "gasolina", True, "411 L", True, False)

caminhao = Caminhao("azul", 1990, "DEF-5678", 6, "diesel", False, False)


print(moto)
moto.para_trabalho()

print(carro)
carro.aceita_carga()

print(caminhao)
caminhao.carga()