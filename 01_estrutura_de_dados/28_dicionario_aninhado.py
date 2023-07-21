contatos = {
    "gilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333222"},
    "carla@gmail.com": {"nome": "Carla", "telefone": "34432222"},
    "jose@gmail.com": {"nome": "José", "telefone": "32244444" },
    "maria@gmail.com": {"nome": "Maria", "telefone": "334411111"}
}
print(contatos["jose@gmail.com"]["telefone"])  #para acessar valores

for chave in contatos:   #a forma mais comum para percorrer os dados de um dicionário é usando o comando for
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)