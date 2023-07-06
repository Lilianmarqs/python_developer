nome = "Lilian"
idade = 26
profissao = "programadora"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Lilian", "idade": 26}

print("Nome: %s  Idade: %d" % (nome, idade))

print("Nome: {}  Idade: {}".format(nome, idade))

print("Nome: {1}  Idade: {0}".format(idade, nome))
print("Nome: {1}  Idade: {0} Nome: {1} {1}".format(idade, nome))  

print("Nome: {nome}  Idade: {idade}".format(idade = idade, nome = nome))
print("Nome: {name}  Idade: {age}".format(age = idade, name = nome))
print("Nome: {nome}  Idade: {idade}".format(**dados     ))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:0.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")

 



