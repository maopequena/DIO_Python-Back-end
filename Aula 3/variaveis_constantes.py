import platform

age = 44
name = "Lizandra"
print(f'Meu nome é {name} e eu tenho {age} anos.')

age2, name2 = (44, "Lizandra") # pode ser com ou sem parênteses: age2, name2 = 44, "Lizandra"
print(f'Meu nome é {name2} e eu tenho {age2} anos.')

# Note que é possível definir múltiplas variáveis na mesma linha
# mas não é uma boa prática, pois prejudica a legibilidade do código.

# variáveis
idade = 44
endereço = "Rua das Flores, 123"
cidade = "Piracaia"

# CONSTANTES
NOME = 'Lizandra'
PAÍS = 'Brasil'
PI = 3.14

print(f'Nome: {NOME}, País: {PAÍS}, Pi: {PI}, Idade: {idade}, Endereço: {endereço}, Cidade: {cidade}')

ABS_PATH = '/home/user/Documentos'
DEBUG = True
STATES = ['SP', 'RJ', 'MG', 'ES']
AMOUNT = 30.25

print(f'Caminho absoluto: {ABS_PATH}, Modo de depuração: {DEBUG}, Estados: {STATES}, Valor: {AMOUNT}')