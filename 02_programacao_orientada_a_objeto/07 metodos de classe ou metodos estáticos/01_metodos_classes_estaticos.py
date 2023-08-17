class Pessoa:
    def __init__(self, nome=None, idade=None):
       self.nome = nome
       self.idade = idade

    @classmethod  #transforma em método de classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2023 - ano
        return Pessoa(nome, idade)

    @staticmethod #pra declarar um método estático 
    def e_maior_idade(idade): 
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1997, 4, 16, "Lilian")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(17))