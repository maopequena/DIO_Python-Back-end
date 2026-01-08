#
#! Aprendendo a usar o @property
#
from datetime import datetime, date

class Pessoa:
  def __init__(self, nome, data_nascimento):
    self._nome = nome
    
    if isinstance(data_nascimento, str):
        self._data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
    else:
        self._data_nascimento = data_nascimento

  @property
  def nome(self):
    return self._nome
  
  @property
  def idade(self):
    hoje = date.today()
    idade = hoje.year - self._data_nascimento.year

    if (hoje.month, hoje.day) < (self._data_nascimento.month, self._data_nascimento.day):
        idade -= 1

    return idade
  
pessoa = Pessoa("Lizandra", "1979-06-06")
print(f"Nome: {pessoa.nome} \nIdade: {pessoa.idade}")