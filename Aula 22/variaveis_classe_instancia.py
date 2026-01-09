class Estudante:
    escola = "DIO"
    
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

gui = Estudante("Guilherme", 56451)
gi = Estudante("Giovanna", 17323)

mostrar_valores(gui, gi)

Estudante.escola = "Python"
mostrar_valores(gui, gi)