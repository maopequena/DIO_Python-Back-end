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

LIMITE_SAQUES = 3
usuarios = []
contas = []

def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, extrato, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado. Retire seu dinheiro.")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques
    
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario():
    nome = input("Digite o nome do cliente: ")
    data_nasc = input("Digite a data de nascimento do cliente no formato DD/MM/AAAA: ")
    CPF = input("Digite o CPF do cliente (somente números): ").strip().replace(".", "").replace("-", "")

    for usuario in usuarios:
        if usuario["CPF"] == CPF:
            print("Usuário já existe!")
            return
    
    logradouro = input("Digite o logradouro, sem o número da residência: ")
    nro = input("Digite o número da residência: ")
    complemento = input("Digite os complementos (apto, casa, etc.): ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    endereco = f"{logradouro}, {nro}, {complemento} - {bairro} - {cidade}/{estado}"
      
    usuario = {
        "nome": nome,
        "data_nasc": data_nasc,
        "CPF": CPF,
        "endereco": endereco
    }
      
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")
    
def criar_conta():
    CPF = input("Digite o CPF do cliente (somente números): ").strip().replace(".", "").replace("-", "")
    
    usuario_existente = [usuario for usuario in usuarios if usuario["CPF"] == CPF]

    if not usuario_existente:
        print("Usuário não existe. Crie um usuário primeiro.")
        return
    
    usuario = usuario_existente[0]
    nro_conta = len(contas) + 1

    conta = {
        "agencia": "0001",
        "conta_corrente": nro_conta,
        "cliente": usuario,
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0
    }
    
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: 0001 / C/C: {nro_conta}")

def selecionar_conta():
    if not contas:
        print("Não há contas cadastradas! Crie um usuário e uma conta primeiro.")
        return
    
    print("=== Selecione uma conta ===")
    for conta in contas:
        print(f"Conta corrente: {conta['conta_corrente']} - Cliente: {conta['cliente']['nome']}\n")
    
    escolha = input("Digite o número da conta: ")

    for conta in contas:
        if str(conta["conta_corrente"]) == escolha:
            return conta
    
    print("Conta não encontrada.")
    return

def listar_contas():
    if not contas:
        print("Não há contas cadastradas.")
        return
    
    print("========== CONTAS CADASTRADAS ==========\n")

    for conta in contas:
        print(f"""Agência: {conta['agencia']}\nC/C: {conta['conta_corrente']}\nCliente: {conta['cliente']['nome']}\n\n""")

    print("=========================================")
    
def listar_usuarios():
    if not usuarios:
        print("Não há usuários cadastrados.")
        return
    
    print("========== USUÁRIOS CADASTRADOS ==========\n")
    for usuario in usuarios:
        print(f"""Nome: {usuario['nome']}\nCPF: {usuario['CPF']}\nData de nascimento: {usuario['data_nasc']}\nEndereço: {usuario['endereco']}\n\n""")
    print("==========================================")
    
while True:
    opcao = input(menu).strip().lower()
    
    if opcao == "d":
        if not contas:
            print("Nenhuma conta cadastrada! Crie um usuário e uma conta primeiro.")
            continue
        conta = selecionar_conta()
        if conta:
            conta["saldo"], conta["extrato"] = depositar(conta["saldo"], conta["extrato"])

    
    elif opcao == "s":
        if not contas:
            print("Nenhuma conta cadastrada! Crie um usuário e uma conta primeiro.")
            continue

        conta = selecionar_conta()
        if conta:
            conta["saldo"], conta["extrato"], conta["numero_saques"] = sacar(
                saldo=conta["saldo"],
                extrato=conta["extrato"],
                numero_saques=conta.get("numero_saques", 0),
                LIMITE_SAQUES=LIMITE_SAQUES
            )
    
    elif opcao == "e":
        conta = selecionar_conta()
        if conta:
            exibir_extrato(conta["saldo"], extrato=conta["extrato"])
    
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