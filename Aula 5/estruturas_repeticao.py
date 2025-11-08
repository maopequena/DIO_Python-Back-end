# # texto = input('Informe um texto: ')
# # VOGAIS = 'AEIOU'

# # for letra in texto:
# #     if letra.upper() in VOGAIS:
# #         print(letra, end="")

# # print() # adiciona uma quebra de linha

# # exemplos digitados: Python, eucalipto, Paraguai, Saguão

# print(range(4))
# print(list(range(4)))

# for numero in range(0, 11):
# 		print(numero, end=" ")
		
# print()  # adiciona uma quebra de linha
# # Exibir a tabuada do 8
# for numero in range(0, 81, 8):
# 		print(numero, end=" ")
		
# print()  # adiciona uma quebra de linha
# from cmath import pi as PI

# print(PI)

opcao = -1

while opcao != 0:
		opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair: "))
		
		if opcao == 1:
				print("Sacando...")
		elif opcao == 2:
				print("Exibindo o extrato")