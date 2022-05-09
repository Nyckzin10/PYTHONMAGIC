from Eletronico import *


class Smartphone(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False


    def conectar(self):
        #verficação se não estiver ligado
        if not self._ligado:
            print(f'{self._nome} Não está ligado')
            return

        # verificação de está conectado
        if self._conectado:
            print(f'{self._nome} JÁ ESTÁ CONECTADO')
            return
        print(f'{self._nome} Está conectado')
        self._conectado = True 


    def desconectar(self):
        if not self._conectado:
            print(f'{self._nome}NÃO ESTÁ CONECTADO..')
            return 
        self._ligado = False 



