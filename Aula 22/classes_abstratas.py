from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        print("Ligando")

    @abstractmethod
    def desligar(self):
        print("Desligando")

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self): # Sobrescrevendo o método abstrato; AMBOS os métodos PRECISAM ser implementados, senão o código diz que falta um dos métodos, porque a classe pai é abstrata e não pode ser instanciada
        print("Ligando a TV")

    def desligar(self):
        print("Desligando a TV")

    @property
    def marca(self):
        print("LG")

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o ar condicionado")

    def desligar(self):
        print("Desligando o ar condicionado")

    @property
    def marca(self):
        print("Samsung")

controle = ControleTV()
controle2 = ControleArCondicionado()

controle.ligar()
controle.desligar()
controle.marca

controle2.ligar()
controle2.desligar()
controle2.marca