# Etapas 2 e 3
# import statistics
# horas_netflix = [4, 20, 6, 7, 30, 8, 10, 12, 15, 7000, 18, 100]
# horas_ordenadas = horas_netflix.sort()
# print(horas_ordenadas)
# def quartis():
    # q = statistics.quantiles(horas_netflix, n = 4, method='exclusive')
    # q1 = q[0]
    # q2 = q[1]
    # q3 = q[2]
    # iqr = q3 - q1
    # return q1, q2, q3, iqr
# quartis_final = quartis()
# q1 = quartis()[0]
# q2 = quartis()[1]
# q3 = quartis()[2]
# iqr = quartis()[3]

# Não consegui remover os outliers, nem calcular a média, mas pelo menos cheguei até aqui
# Minha solução estava totalmente errada!

horas_netflix = [4, 20, 6, 7, 30, 8, 10, 12, 15, 7000, 18, 100]

def calcular_quartis(dados):
  # Ordenar os dados
  dados_ordenados = sorted(dados)
  n = len(dados_ordenados)
  
  # Calcular Q1
  q1 = dados_ordenados[int(n * 0.25)]
  
  # Calcular Q3
  q3 = dados_ordenados[int(n * 0.75)]
  
  # Calcular IQR
  iqr = q3 - q1
  print(q1)
  print(q3)
  print(iqr)
  return q1, q3, iqr


  
def remover_outliers(dados):
  # Calcular Q1, Q3 e IQR
  q1, q3, iqr = calcular_quartis(dados)
  
  # Calcular limites
  limite_inferior = q1 - (1.5 * iqr)
  limite_superior = q3 + (1.5 * iqr)
  
  # Filtrar dados dentro dos limites
  dados_sem_outliers = []
  for i in dados:
    if (i >= limite_inferior) and (i <= limite_superior):
      dados_sem_outliers.append(i)
  
  print(limite_inferior)
  print(limite_superior)
  return dados_sem_outliers
  
# Remover outliers e calcular a média
novos_dados = remover_outliers(horas_netflix)
print(f'Dados sem outliers: {novos_dados}')

media = sum(novos_dados) / len(novos_dados)
print(f'Média de horas assistidas (sem outliers): {round(media)}h')