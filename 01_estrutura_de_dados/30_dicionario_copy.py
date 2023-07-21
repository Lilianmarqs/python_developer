contatos = {
    "lilian@gmail.com": {"nome": "Lilian", "telefone": "3333222"}
}

copia = contatos.copy()
copia["lilian@gmail.com"] = {"nome": "Lila"}

print(contatos["lilian@gmail.com"])
print(copia["lilian@gmail.com"])