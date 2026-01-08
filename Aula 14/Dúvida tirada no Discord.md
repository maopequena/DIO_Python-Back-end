# DÚVIDA NO DISCORD

**Eu:**
https://discord.com/channels/689887036110274618/1428081202879004805/1440874117996875867
E lá venho eu com outra dúvida! Neste código do vídeo sobre decoradores:

```python
def envelope():
    print("faz algo antes de executar")
    funcao()
    print("faz algo depois de executar")

    return envelope


def ola_mundo():
    print("Olá mundo!")


**ola_mundo** = meu_decorador(__ola_mundo__)
ola_mundo()
```

a função que ele chamou no final é a definida com "def" **E** a variável que está entre asteriscos **E** o parâmetro que está entre sublinhados??

**Rogério:**
https://discord.com/channels/689887036110274618/1428081202879004805/1440877204903956603
De onde você tirou esse fragmento de código?

__Eu:__
https://discord.com/channels/689887036110274618/1428081202879004805/1440878634469687396
do github: https://github.com/digitalinnovationone/trilha-python-dio/blob/main/03%20-%20Decoradores%2C%20Iteradores%20e%20Geradores/4_primeiro_decorador.py. Ele é explicado no Vídeo 1 da aula sobre decoradores, iteradores e geradores.

**Rogério:**
https://discord.com/channels/689887036110274618/1428081202879004805/1440878944273563779
os asteriscos e os sublinhados foi você que colocou, para destacar qual a sua dúvida?
por que no repositório não consta

**Eu:**
https://discord.com/channels/689887036110274618/1428081202879004805/1440879060568772659
isso

**Rogério:**
https://discord.com/channels/689887036110274618/1428081202879004805/1440879114138681346
Ok

__Eu:__
https://discord.com/channels/689887036110274618/1428081202879004805/1440879152801644647
Pelo que eu entendi pelo vídeo é exatamente isso, as três ocorrências são a mesma função, mas eu queria confirmar. Depois ele altera esse código colocando um "@meu_decorador" e remove essa linha onde coloquei os asteriscos e os sublinhados

**Rogério:**
https://discord.com/channels/689887036110274618/1428081202879004805/1440879346301534271
o que está entre asteriscos é uma variavel qualquer e que vai receber a referencia para esse decorator
e o que está entre os sublinhados é o nome da função decorada que no exemplo é ola mundo

**Eu:**
https://discord.com/channels/689887036110274618/1428081202879004805/1440879654100799564
ah, agora faz mais sentido. a variável poderia ter qq outro nome, então?

**Rogério:**
https://discord.com/channels/689887036110274618/1428081202879004805/1440879753060946040

```lua
def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envelope


def funcao_decarada():
    print("Olá mundo!")


qualquer_variavel = meu_decorador(funcao_decarada)
qualquer_variavel()
```

**Eu:**
https://discord.com/channels/689887036110274618/1428081202879004805/1440879814998364220
exato! Obrigada de novo, Rogério!

__Rogério:__
https://discord.com/channels/689887036110274618/1428081202879004805/1440879921470898236
o uso do @meu_decorador é mais comum e uma sintaxe mais simples do que a forma mostrada nesse fragmento
mas produzem exatamente o mesmo efeito

**Eu:**
https://discord.com/channels/689887036110274618/1428081202879004805/1440880119152508988
Muitíssimo obrigada, foi above and beyond essa sua resposta!
