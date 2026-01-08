def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("faz algo depois de executar")
        return resultado # este resultado não é "guardado" em lugar nenhum, somente retornado
    
    return envelope


@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome} e {outro_argumento}!")
    return nome.upper(), float(outro_argumento)


resultado = ola_mundo("João", 1000) # este resultado armazena a função e retorna o nome como maiúscula e outro_argumento como float
print(resultado)