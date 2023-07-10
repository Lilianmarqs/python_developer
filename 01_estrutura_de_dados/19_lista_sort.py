frutas = ["morango", "uva", "laranja", "cereja", "banana", "mamão", "maçã"]
frutas.sort()
print(frutas)

frutas.sort(reverse=True)
print(frutas)

frutas.sort(key=lambda x: len(x)) #lambda é uma função pra ordener por tamanho 
print(frutas)

frutas.sort(key=lambda x: len(x), reverse=True)
print(frutas)