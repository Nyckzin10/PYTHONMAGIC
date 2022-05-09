class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
        self.nomeclasses = self.__class__.__name__


    def falar(self):
        print(f'{self.nomeclasses} Falando..')



class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasses} Comprando...')
    


class Aluno(Pessoa):
    def estudando(self):
        print(f'{self.nomeclasses} Estudando...')

