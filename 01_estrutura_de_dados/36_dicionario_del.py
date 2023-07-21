contatos = {
    "lilian@gmail.com": {"nome": "Lilian", "telefone": "3333222"},
    "carla@gmail.com": {"nome": "Carla", "telefone": "34432222"},
    "jose@gmail.com": {"nome": "José", "telefone": "32244444" },
    "maria@gmail.com": {"nome": "Maria", "telefone": "334411111"}
}

del contatos["lilian@gmail.com"]["telefone"]
del contatos["jose@gmail.com"]

print(contatos)