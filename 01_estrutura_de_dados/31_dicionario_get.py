contatos = {
    "lilian@gmail.com": {"nome": "Lilian", "telefone": "3333222"}
}

#contatos["chave"]  #KeyError
#o metodo get se usa quando nao tem certeza se a chave existe ou não. Se a chave não existir, ele retorna "None"
print(contatos.get("chave")) #None
print(contatos.get("chave", {}))
print(contatos.get("lilian@gmail.com", {}))