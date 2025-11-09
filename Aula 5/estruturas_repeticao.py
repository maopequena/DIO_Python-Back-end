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

# WHILE
# opcao = -1

# while opcao != 0:
# 		opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair: "))
		
# 		if opcao == 1:
# 				print("Sacando...")
# 		elif opcao == 2:
# 				print("Exibindo o extrato")
				
# BREAK
# opcao = -1

# while opcao != 0:
# 		opcao = int(input("Informe um número: "))
		
# 		if opcao % 2 == 0:
# 				print("Continua executando...")
# 		else:
# 				break
		
# OUTRA FORMA DE USAR O BREAK
# opcao = -1

# while opcao != 0:
#   opcao = int(input("Informe um número: "))
#   if opcao == 10:
#     print("Você encontrou o número secreto!")
#     break
#   elif opcao % 2 == 0:
#     print("Esse não é o número secreto, mas é par.")
#   else:
#     print("Esse não é o número secreto, é impar.")

# MAIS UM JEITO DE USAR O BREAK COM LOOP INFINITO
# while True:
#   numero = int(input("Informe um número: "))
#   if numero == 42:
#     print("Você encontrou o número secreto! Encerrando o programa.")
#     break
  
#   print(numero)

# CONTINUE
# Exibir os números pares de 1 a 20
numero = 0

while numero in range(0, 21):
    numero += 1
    
    if numero % 2 != 0:
        continue
    
    print(numero, end=" ")