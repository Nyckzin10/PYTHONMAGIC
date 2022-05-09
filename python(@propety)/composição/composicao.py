class Clientes:
    def __init__(self, nome, idade, cpf):
        self.nome = nome 
        self.idade = idade 
        self.enderecos = []
        self.cpf = cpf 



    def inser_cpf(self, cpf):
        self.cpf.append(RegistroNumber(cpf, data))



    def inserir_enderecos(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_ederecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

class Endereco:
    def __init__(self,cidade,estado):
        self.cidade = cidade 
        self.estado = estado 


class RegistroNumber:
    def __init__(self, cpf , data):
        self.cpf = cpf 
        self.data = data 