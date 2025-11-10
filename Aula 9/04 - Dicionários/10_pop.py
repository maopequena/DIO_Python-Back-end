contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
  "lizandra@gmail.com": {"nome": "lizandra", "telefone": "4444-3332"}
  }

print(contatos)

resultado1 = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado1)

resultado2 = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado2)

print(contatos)
