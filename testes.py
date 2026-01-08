# HORA FORMATADA
# from datetime import datetime

# agora = datetime.now()
# data_formatada = agora.strftime("%d.%m.%Y %H:%M:%S")

# print(data_formatada)

# Gerador com base em prompt fornecido pelo GPT:
# "Digamos que temos uma lista com 100 usuários.
# Para economizar a memória da máquina que comporta essa lista,
# podemos usar um gerador para retornar cada um
# dos usuários por vez, em vez da lista toda."

# Versão 1
# def gerar_usuarios(usuarios):
#     for usuario in usuarios:
#         # Em vez de devolver a lista inteira
#         # devolve UM usuário por vez
#         return usuario

# # Lista grande (exemplo simples)
# usuarios = [f"Usuário {i}" for i in range(1, 101)]

# for u in gerar_usuarios(usuarios):
#     print(u)

# Versão 2
# def gerar_usuarios(usuarios):
#     index = 0
#     while index < len(usuarios):
#         return usuarios[index]
#         index += 1

# usuarios = [f"Usuário {i}" for i in range(1, 11)]

# for u in gerar_usuarios(usuarios):
#     print(u)

it = iter([1, 2, 3])

print(next(it))
print(next(it))
print(next(it))
print(next(it))
