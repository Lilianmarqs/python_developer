class Passaro:
    def voar(self):
        print("Voando... ")


class Pardal(Passaro): 
    def voar(self):
        return super().voar()
    

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar!")


#FIXME exemplo ruim de herança pra "Ganhar" o método voar: 
class Aviao(Passaro):
    def voar(self):
        print("O avião está decolando.... ")


def plano_voo(obj):  #polimorfismo ocorre aqui!
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())