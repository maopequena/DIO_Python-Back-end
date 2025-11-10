frutas = ["laranja", "maca", "uva"] # lista com três frutas
# ["laranja", "maca", "uva"]

frutas_vazia = [] # lista vazia

letras = list("python") # criação de lista a partir de uma string, exibe cada letra da palavra entre parênteses
# ["p", "y", "t", "h", "o", "n"]

numeros = list(range(10)) # criação de lista a partir da função range, que exibe os números de 0 a 9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True, ["BMW", "Fiat", "Ford"]]

print(frutas[1])      # Acessa o segundo elemento da lista frutas
print(letras[3])      # Acessa o quarto elemento da lista letras
print(numeros[5])     # Acessa o sexto elemento da lista numeros
print(carro[7][2])    # Acessa o terceiro elemento da lista dentro da lista carro

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

# Exemplo de fatiamento de listas
carros = ["gol", "celta", "palio", "onix", "camaro"]

for carro in carros:
    print(carro)      # Imprime o nome de cada carro na lista carros
    print(carro[1])  # Imprime a segunda letra de cada nome de carro na lista carros
    print(carro[:2:-1])  # Imprime as três últimas letras de cada nome de carro na lista carros, de trás para frente

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')  # Imprime o índice e o nome de cada carro na lista carros

# Filtros (versão 1)
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# Filtros (versão 2)
pares2 = [numero for numero in numeros if numero % 2 == 0]
print(pares2)

# Alterar valores (versão 1)
quadrado = []

for numero in numeros:
    quadrado.append(numero**2)

print(quadrado)

# Alterar valores (versão 1)
quadrado2 = [numero**2 for numero in numeros]
print(quadrado2)

# Copy
lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(l2)
print(id(lista), id(l2))  # IDs diferentes, ou seja, são listas diferentes

# Count
cores = ["vermelho", "azul", "verde", "azul", "amarelo", "verde"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 2
print(cores.count("amarelo"))  # 1

linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5
print(len(linguagens[3])) # 4

numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(numeros)  # [0, 2, 4, 49, 64]