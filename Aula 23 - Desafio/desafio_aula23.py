from abc import ABC, abstractmethod
from datetime import datetime

class PessoaFisica:
    def __init__(self, nome, data_nasc, CPF):
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
    def __init__(self, nome, data_nasc, CPF, endereco):
        super().__init__(nome, data_nasc, CPF)
        self._endereco = endereco
        self._contas = []
    
    def realizar_transacao(self, conta, transacao):
        return transacao.registrar(conta)
    
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

    def exibir_extrato(self):
        print("\n========== EXTRATO ==========")
        print(self._historico.exibir())
        print(f"\nSaldo atual: R$ {self._saldo:.2f}")
        print("==============================")


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
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
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
# Menu and utility functions
menu = """
Seja bem-vindo(a)! Digite uma das opções:

[d] Depositar
[s] Sacar
[e] Extrato
[n] Novo usuário
[c] Nova conta corrente
[l] Exibir contas
[u] Exibir usuários
[q] Sair

=> """

usuarios = []
contas = []

def criar_usuario():
    nome = input("Digite o nome do cliente: ")
    data_nasc_str = input("Digite a data de nascimento do cliente no formato DD/MM/AAAA: ")
    data_nasc = datetime.strptime(data_nasc_str, "%d/%m/%Y").date()
    CPF = input("Digite o CPF do cliente (somente números): ").strip().replace(".", "").replace("-", "")

    for usuario in usuarios:
        if usuario.CPF == CPF:
            print("Usuário já existe!")
            return
    
    logradouro = input("Digite o logradouro, sem o número da residência: ")
    nro = input("Digite o número da residência: ")
    complemento = input("Digite os complementos (apto, casa, etc.): ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    endereco = f"{logradouro}, {nro}, {complemento} - {bairro} - {cidade}/{estado}"
      
    usuario = Cliente(nome, data_nasc, CPF, endereco)
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")

def criar_conta():
    CPF = input("Digite o CPF do cliente (somente números): ").strip().replace(".", "").replace("-", "")
    
    usuario_existente = [usuario for usuario in usuarios if usuario.CPF == CPF]

    if not usuario_existente:
        print("Usuário não existe. Crie um usuário primeiro.")
        return
    
    usuario = usuario_existente[0]
    _numero_conta = len(contas) + 1
    conta = Conta(_numero_conta, usuario)
    usuario.adicionar_conta(conta)
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: 0001 / C/C: {_numero_conta}")

def selecionar_conta():
    if not contas:
        print("Não há contas cadastradas! Crie um usuário e uma conta primeiro.")
        return None
    
    print("=== Selecione uma conta ===")
    for conta in contas:
        print(f"Conta corrente: {conta._numero_conta} - Cliente: {conta._cliente.nome}\n")
    
    escolha = input("Digite o número da conta: ")

    for conta in contas:
        if str(conta._numero_conta) == escolha:
            return conta
    
    print("Conta não encontrada.")
    return None

def listar_contas():
    if not contas:
        print("Não há contas cadastradas.")
        return
    
    print("========== CONTAS CADASTRADAS ==========\n")
    for conta in contas:
        print(f"""Agência: {conta._agencia}\nC/C: {conta._numero_conta}\nCliente: {conta._cliente.nome}\n\n""")
    print("=========================================")
    
def listar_usuarios():
    if not usuarios:
        print("Não há usuários cadastrados.")
        return
    
    print("========== USUÁRIOS CADASTRADOS ==========\n")
    for usuario in usuarios:
        print(f"""Nome: {usuario.nome}\nCPF: {usuario.CPF}\nData de nascimento: {usuario._data_nasc}\nEndereço: {usuario._endereco}\n\n""")
    print("==========================================")

# Main program loop
def main():
    while True:
        opcao = input(menu).strip().lower()
        
        if opcao == "d":
            if not contas:
                print("Nenhuma conta cadastrada! Crie um usuário e uma conta primeiro.")
                continue
            conta = selecionar_conta()
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                transacao = Deposito(valor)

                cliente = conta.cliente
                
                if cliente.realizar_transacao(conta, transacao):
                    print("Depósito realizado com sucesso!")
                else:
                    print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            if not contas:
                print("Nenhuma conta cadastrada! Crie um usuário e uma conta primeiro.")
                continue

            conta = selecionar_conta()
            if conta:
                valor = float(input("Informe o valor do saque: "))
                transacao = Saque(valor)
                
                cliente = conta.cliente
                
                if cliente.realizar_transacao(conta, transacao):
                    print("Saque realizado. Retire seu dinheiro.")
                else:
                    print("Operação falhou! Verifique saldo, limite de saques ou valor informado.")
        
        elif opcao == "e":
            conta = selecionar_conta()
            if conta:
                conta.exibir_extrato()
        
        elif opcao == "n":
            criar_usuario()
        
        elif opcao == "c":
            criar_conta()
        
        elif opcao == "l":
            listar_contas()
        
        elif opcao == "u":
            listar_usuarios()
        
        elif opcao == "q":
            print("Tenha um bom dia e volte sempre!")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()