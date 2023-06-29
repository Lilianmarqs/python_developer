nome = "lILian"

print(nome.upper()) #deixa todas as letras maiúsculas 
print(nome.lower()) # deixa todas as letras minúsculas
print(nome.title()) # deixa a prmeira letra maiúsculas

texto = "  olá mundo!   "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))