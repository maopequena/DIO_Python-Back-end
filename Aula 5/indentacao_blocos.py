def sacar(valor: float):
    saldo = 500

    if saldo >= valor:
        saldo -= valor
        print("Saque realizado com sucesso.")
    else:
        print("Saldo insuficiente para realizar o saque.")
        print(f"Saldo atual: {saldo}. Tenha um ótimo dia!")
        return
    
    print(f"Saldo atual: {saldo}. Tenha um ótimo dia!")

sacar(100)