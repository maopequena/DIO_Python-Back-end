def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado de {a} / {b} = {resultado}")


# exibir_resultado(10, 10, somar)  # O resultado de 10 + 10 = 20
# exibir_resultado(23, 32, somar)  # O resultado de 23 + 32 = 55

# O interessante aqui é que podemos simplesmente criar novas funções e manter a função exibir resultado:
def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def varias_operações(a, b):
    return (a - 1) + (b * 2)

# exibir_resultado(23, 32, subtrair)  # O resultado de 23 - 32 = -9 
# exibir_resultado(23, 32, multiplicar)  # O resultado de 23 * 32 = 736 
# exibir_resultado(23, 32, dividir)  # O resultado de 23 / 32 = 0.71875
# exibir_resultado(23, 32, varias_operações)  # O resultado de (23 - 1) + (32 * 2) = 86

# operacao = somar
op_d = dividir


# print(operacao(1, 23)) # 24

print(round(exibir_resultado(23, 32, dividir), 2))
print(round(op_d(1, 23), 2))