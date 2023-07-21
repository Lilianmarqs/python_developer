contatos = {
    "lilian@gmail.com": {"nome": "Lilian", "telefone": "3333222"},
    "carla@gmail.com": {"nome": "Carla", "telefone": "34432222"},
    "jose@gmail.com": {"nome": "José", "telefone": "32244444" },
    "maria@gmail.com": {"nome": "Maria", "telefone": "334411111"}
}
resultado = "lilian@gmail.com" in contatos
print(resultado)

resultado = "megui@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["lilian@gmail.com"]
print(resultado)

resultado = "telefone" in contatos["lilian@gmail.com"]
print(resultado)