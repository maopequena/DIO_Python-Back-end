contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
  "lizandra@gmail.com": {"nome": "lizandra", "telefone": "4444-3332"}
  }

print(contatos)

resultado1 = contatos.popitem() # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado1)

print(contatos)

resultado2 = contatos.popitem()  # ("lizandra@gmail.com": {"nome": "lizandra", "telefone": "4444-3332"})
print(resultado2)


contatos.popitem()  # KeyError
