# Funções de decoração com argumentos
def duplicar(func):
		def envelope(*args, **kwargs):
				func(*args, **kwargs) # executa a função usada como parâmetro duas vezes
				func(*args, **kwargs)
		
		return envelope

@duplicar # aplica a função abaixo a esta função, definida acima
def aprender(tecnologia):
		print(f"Estou aprendendo {tecnologia}")
		
aprender("Python")