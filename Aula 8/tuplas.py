frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

print(frutas, letras, numeros, pais)

frutas = ("maca", "laranja", "uva", "pera",)

print(frutas[0]) # maca
print(frutas[2]) # uva

print(frutas[-1]) # pera
print(frutas[-3]) # laranja

carros = ("gol")
print(isinstance(carros, tuple))