# A. Animal:
#   1. Mamífero:
#     a. Cachorro
#     b. Gato
#     c. Leão
#   2. Ave:
#     a. Ornitorrinco (que também herda de Mamífero)


class Animal:
    """
    The Animal class is the base class for all animals. It has attributes for color, number of eyes, weight, number of legs, and half-nipple rule.

    Attributes:
        cor (str): The color of the animal.
        qtdd_olhos (int): The number of eyes the animal has.
        peso (float): The weight of the animal.
        qtdd_patas (int): The number of legs the animal has.
        half_nipple_rule (int): The maximum amount of nipples this animal can have, according to the half-nipple rule.

    Methods:
        __init__(self, cor, qtdd_olhos, peso, qtdd_patas, half_nipple_rule): Initializes the attributes of the animal.
        __str__(self): Returns a string representation of the animal.
        __del__(self): Deletes the animal object.
    """
  
    def __init__(self, cor, qtdd_olhos, peso, qtdd_patas, half_nipple_rule):
        self.cor = cor
        self.qtdd_olhos = qtdd_olhos
        self.peso = peso
        self.qtdd_patas = qtdd_patas
        self.half_nipple_rule = half_nipple_rule

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __del__(self):
        print("Excluindo a classe Animal")


class Mamifero(Animal):
    """
    The Mamifero class is a subclass of the Animal class and represents a mammal. It inherits all the attributes and methods of the Animal class.

    Attributes:
        domestico (bool): Whether the mammal is domestic or not.
        carnivoro (bool): Whether the mammal is carnivorous or not.

    Methods:
        __init__(self, **kwargs): Initializes the attributes of the mammal by calling the __init__ method of the Animal class.
        __del__(self): Deletes the mammal object."""
    def __init__(self, domestico=False, carnivoro=True, **kwargs):
        super().__init__(**kwargs)
        self.domestico = domestico
        self.carnivoro = carnivoro

    def __del__(self):
        print("Excluindo a classe Mamífero")


class Ave(Animal):
    """
    The Ave class is a subclass of the Animal class and represents a bird. It inherits all the attributes and methods of the Animal class.

      Attributes:
          domesticado (bool): Whether the bird is domestic or not.

      Methods:
          __init__(self, domesticado=False, **kwargs): Initializes the attributes of the bird by calling the __init__ method of the Mamifero class.
          __del__(self): Deletes the bird object.
    """
    def __init__(self, domesticado=False, **kwargs):
        super().__init__(**kwargs)
        self.domesticado = domesticado

    def __del__(self):
        print("Excluindo a classe Ave")


class Cachorro(Mamifero):
    """
    The Cachorro class is a subclass of the Mamifero class and represents a dog. It inherits all the attributes and methods of the Mamifero class.

    Attributes:
        raca (str): The breed of the dog.
        nome (str): The name of the dog.

    Methods:
        __init__(self, raca, nome, **kwargs): Initializes the attributes of the dog by calling the __init__ method of the Mamifero class.
        __del__(self): Deletes the dog object.
        latir(self): Prints a message indicating that the dog is barking.
    """
    def __init__(self, raca, nome, **kwargs):
        super().__init__(**kwargs)
        self.raca = raca
        self.nome = nome
        print(f"A classe pai é: {self.__class__.__base__}")

    def __del__(self):
        print("Excluindo a classe Cachorro")

    def latir(self):
        print("Au au!")


class Gato(Mamifero):
    """
    The Gato class is a subclass of the Mamifero class and represents a cat. It inherits all the attributes and methods of the Mamifero class.

    Attributes:
        raca (str): The breed of the cat.
        nome (str): The name of the cat.

    Methods:
        __init__(self, raca, nome, **kwargs): Initializes the attributes of the cat by calling the __init__ method of the Mamifero class.
        __del__(self): Deletes the cat object.
        miar(self): Prints a message indicating that the cat is meowing.
    """
    def __init__(self, raca, nome, **kwargs):
        super().__init__(**kwargs)
        self.raca = raca
        self.nome = nome
        print(f"A classe pai é: {self.__class__.__base__}")

    def __del__(self):
        print("Excluindo a classe Gato")

    def miar(self):
        print("Miau!")


class Leao(Mamifero):
    """
    The Leao class is a subclass of the Mamifero class and represents a lion. It inherits all the attributes and methods of the Mamifero class.

    Attributes:
        em_cativeiro (bool): A boolean indicating whether the lion is in captivity.

    Methods:
        __init__(self, em_cativeiro=False, **kwargs): Initializes the attributes of the lion by calling the __init__ method of the Mamifero class.
        __del__(self): Deletes the lion object.
        roar(self): Prints a message indicating that the lion is roaring.
    """
    def __init__(self, em_cativeiro=False, **kwargs):
        super().__init__(**kwargs)
        self.em_cativeiro = em_cativeiro
        print(f"A classe pai é: {self.__class__.__base__}")

    def __del__(self):
        print("Excluindo a classe Leão")

    def roar(self):
        print("Roar!")


class Ornitorrinco(Ave, Mamifero):
    """
    The Ornitorrinco class is a subclass of the Ave and Mamifero classes and represents an ornitorhynchus. It inherits all the attributes and methods of the Ave and Mamifero classes.

    Attributes:
        registrado (bool): A boolean indicating whether the ornitorhynchus is registered with IBAMA.

    Methods:
        __init__(self, **kwargs): Initializes the attributes of the ornitorhynchus by calling the __init__ method of the Ave class.
        __del__(self): Deletes the ornitorhynchus object.
        info(self): Prints a message indicating whether the ornitorhynchus is registered with IBAMA.
    """
    def __init__(self, registrado=False, **kwargs):
        super().__init__(**kwargs)
        self.registrado = registrado
        print(f"A classe pai é: {self.__class__.__base__}")

    def __del__(self):
        print("Excluindo a classe Ornitorrinco")

    def info(self):
        print(
            f"Este ornitorrinco {'está' if self.registrado else 'não está'} registrado com o IBAMA."
        )


cachorro = Cachorro(
    "SRD",
    "Koda",
    cor="marrom",
    qtdd_olhos=2,
    peso="20 Kg",
    qtdd_patas=4,
    half_nipple_rule=8,
    domestico=True,
    carnivoro=True,
)

gato = Gato(
    "SRD",
    "Kiko",
    cor="cinza",
    qtdd_olhos=2,
    peso="4,5 Kg",
    qtdd_patas=4,
    half_nipple_rule=8,
    domestico=True,
    carnivoro=True,
)

leao = Leao(
    False,
    cor="amarelo",
    qtdd_olhos=2,
    peso="100 Kg",
    qtdd_patas=4,
    half_nipple_rule=8,
    domestico=False,
    carnivoro=True,
)

ornitorrinco = Ornitorrinco(
    True,
    cor="marrom",
    qtdd_olhos=2,
    peso="30 Kg",
    qtdd_patas=4,
    half_nipple_rule=8,
    domesticado=False,
)

print(cachorro)
cachorro.latir()

print(gato)
gato.miar()

print(leao)
leao.roar()

print(ornitorrinco)
ornitorrinco.info()
