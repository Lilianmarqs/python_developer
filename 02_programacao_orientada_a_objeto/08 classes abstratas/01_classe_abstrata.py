from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class Controle_tv(ControleRemoto):
    def ligar(self):
        print("Ligando a TV.... ")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV.... ")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o ar condicionado.... ")
        print("Ligado!")

    def desligar(self):
        print("Desligando o ar condicionado.... ")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"

controle = Controle_tv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
