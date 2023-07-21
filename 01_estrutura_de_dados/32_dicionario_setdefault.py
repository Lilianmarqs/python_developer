#se o valor nao tiver a chave no dicionário, ele adiciona, se existir, ele retornará o valor 
contatos = {"nome": "Lilian", "telefone": "3333222"}


contatos.setdefault("nome", "Adriel")
print(contatos)

contatos.setdefault("idade", 27)
print(contatos)

