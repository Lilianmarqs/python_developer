class Estudante: 
    escola ="DIO"

    def __init__(self, nome, matricula): 
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def  mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)
aluno_1.matricula = 3
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Estacio"
mostrar_valores(aluno_1, aluno_2)

aluno_3 = Estudante("Lucas", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)

aluno_3.escola = "Pitagoras"
mostrar_valores(aluno_1, aluno_2, aluno_3)


#Lembre se que o "self" sempre é variável de instâcia, "escola" foi declarado como variável de classe



