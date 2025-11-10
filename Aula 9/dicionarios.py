# Declarar dicionários
pessoa = {"nome": "lizandra", "idade": 44}

pessoa1 = dict(nome="lizandra", idade=44)

print(pessoa)
print(pessoa1)

pessoa["telefone"] = "99999-1234"
pessoa1["telefone"] = "99999-1234"

print(pessoa)
print(pessoa1)

# Acesso aos dados
dados = {'nome': 'lizandra', 'idade': 44, 'telefone': '99999-1234'}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "99988-5678"

print(dados)

# Dicionários aninhados
contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
  "giovana@gmail.com": {"nome": "Giovana", "telefone": "3443-2121"},
  "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
  "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}
}

print(contatos)

print(contatos["giovana@gmail.com"]["telefone"]) # 3443-2121

# PAREI EM SETDEAFULT