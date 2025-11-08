# Estruturas Condicionais em Python
# IF, ELIF, ELSE
# MAIOR_IDADE = 18
# idade = int(input("Digite sua idade: "))

# if idade >= MAIOR_IDADE:
#     print("Você é maior de idade, pode tirar ou renovar sua CNH.")

# if idade < MAIOR_IDADE:
#     print("Você é menor de idade. Ainda não pode tirar a carteira de motorista.")

# if idade >= MAIOR_IDADE:
#     print("Você é maior de idade, pode tirar ou renovar sua CNH.")
# else:
#     print("Você é menor de idade. Ainda não pode tirar a carteira de motorista.")

# if idade == 19:
#     print("Você precisa pegar sua carteira de motorista permanente!")
# elif idade >= MAIOR_IDADE:
#     print("Você é maior de idade, pode tirar ou renovar sua CNH.")
# else:
#     print("Você é menor de idade. Ainda não pode tirar a carteira de motorista.")

# IF, ELIF, ELSE ANINHADOS
# conta_normal = False
# conta_universitaria = False
# conta_vip = False
# conta_black = True
saldo = 600
# cheque_especial = 200
saque = 500

# if conta_normal:
#     if saldo >= saque:
#         print('Saque realizado com sucesso!')
#     elif saldo <= (saldo + cheque_especial):
#         print('Saque realizado com uso do cheque especial!')
#     else:
#         print('Não foi possível realizar o saque: saldo insuficiente.')
# elif conta_universitaria:
#     if saldo >= saque:
#         print('Saque realizado com sucesso!')
#     else:
#         print('Não foi possível realizar o saque: saldo insuficiente.')
# else:
#     if conta_vip:
#         if saldo >= saque:
#             print('Saque realizado com sucesso!')
#         else:
#             print('Não foi possível realizar o saque: saldo insuficiente. \nFale com seu gerente a qualquer hora: (11) 99999-8888.')
#     elif conta_black:
#         if saldo >= saque:
#             print('Saque realizado com sucesso!')
#         else:
#             print('Saque realizado com sucesso! \nPorém, houve uso do cheque especial, fale com seu gerente a qualquer hora: (11) 99999-8888.')

# IF TERNÁRIO
status = "Sucesso" if saldo >= saque else "Falha"

print(f'{status} ao realizar o saque.')