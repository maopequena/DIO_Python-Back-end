saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)
# True

print(saque <= limite)
# False

print(saldo >= saque and saque <= limite)
# False

contatos_emergencia = []

print(not 1000 > 1500)
# True
# 1000 NÃO É maior que 1500, portanto, True

print(not contatos_emergencia)
# True
# porque não há nada na lista

print(not "saque 1500;")
# False
# porque há algo na string

print(not "")
# True
# porque não há nada na string

saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)
# True

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))
# True