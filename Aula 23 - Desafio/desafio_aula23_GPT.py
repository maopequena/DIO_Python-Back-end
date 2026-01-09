from abc import ABC, abstractmethod
from datetime import datetime

class PessoaFisica:
    def __init__(self, nome: str, data_nasc: date, CPF: str):
        self._nome = nome
        self._data_nasc = data_nasc
        self._CPF = CPF
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def CPF(self):
        return self._CPF
    
    @property
    def data_nasc(self):
        return self._data_nasc

class Cliente(PessoaFisica):
    def __init__(self, nome: str, data_nasc: date, CPF: str, endereco: str):
        super().__init__(nome, data_nasc, CPF)
        self._endereco = endereco
        self._contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)


class ContaCorrente:
    LIMITE_SAQUES = 3

    def __init__(self, limite=500):
        self._limite = limite
        self._numero_saques = 0

    @property
    def limite(self):
        return self._limite

    @property
    def numero_saques(self):
        return self._numero_saques

    def sacar(self, valor):
        if valor <=0:
            return False
        
        if valor > self._limite:
            print("Saldo insuficiente.")
            return False

        if self._numero_saques >= self.LIMITE_SAQUES:
            print("Limite de saques diário atingido.")
            return False

        self._numero_saques += 1
        return True


class Conta(ContaCorrente):
    LIMITE_SAQUES = 3

    def __init__(self, numero, cliente, agencia="0001", limite=500):
        super().__init__(limite)
        self._saldo = 0.0
        self._numero_conta = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero_conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido.")

            return False
        self._saldo += valor
        return True

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
            return False

        if valor > self._saldo:
            print("Saldo insuficiente.")
            return False

        if not super().sacar(valor):
            return False

        self._saldo -= valor
        return True


class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.depositar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)
        return sucesso


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.sacar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)
        return sucesso


class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": round(transacao.valor, 2),
            "data": datetime.now()
        })

    def gerar_relatorio(self, tipo=None):
        for transacao in self._transacoes:
            if tipo is None or transacao["tipo"].lower() == tipo.lower():
                yield transacao

    def exibir(self):
        if not self._transacoes:
            return "Não foram realizadas movimentações."

        linhas = []
        for t in self.gerar_relatorio():
            linhas.append(
                f"{t['tipo']} | R$ {t['valor']:.2f} | {t['data']}"
            )

        return "\n".join(linhas)