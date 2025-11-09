# COM %
# nome = "Lizandra"
# idade = 44
# profissao = "tradutora"
# idioma = "inglês"

# print("Olá, me chamo %s. Eu tenho %d anos, trabalho como %s de %s para português." % (nome, idade, profissao, idioma))

# COM .format()
# nome = "Lizandra"
# idade = 44
# profissao = "tradutora"
# idioma = "inglês"

# print("Olá, me chamo {}. Eu tenho {} anos, trabalho como {} de {} para português.".format(nome, idade, profissao, idioma))

# print("Olá, me chamo {3}. Eu tenho {2} anos, trabalho como {1} de {0} para português.".format(idioma, profissao, idade, nome))

# print("Olá, me chamo {nome}. Eu tenho {idade} anos, trabalho como {profissao} de {idioma} para português.".format(idioma=idioma, profissao=profissao, idade=idade, nome=nome))

pessoa = {
  "nome": "Lizandra",
  "idade": 44,
  "profissao": "tradutora",
  "idioma": "inglês"
}

print("Olá, me chamo {nome}. Eu tenho {idade} anos, trabalho como {profissao} de {idioma} para português.".format(**pessoa))

# PI = 3.14159

# print(f"Valor de pi: {PI:.2f}")

# print(f"Valor de pi: {PI:10.2f}")