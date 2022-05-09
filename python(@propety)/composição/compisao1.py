from composicao import * 

print("\nPRIMEIRO CADASTRO\n")
user1 = Clientes('Hedris', 23)
user1.inserir_enderecos('Belo Horizonte', 'MG')
print(user1.nome, user1.idade)
user1.lista_ederecos()
print("ULITMO CADASTRO")


print("\nPRIMEIRO CADASTRO\n")
user2 = Clientes('Joao', 22)
user2.inserir_enderecos('Brasilia' ,'df')
print(user2.nome, user2.idade)
user2.lista_ederecos()
print("\nULITMO CADASTRO\n")


print("\nPRIMEIRO CADASTRO\n")
user3 = Clientes('Fernando', 30)
user3.inserir_enderecos('Bahia', 'BA')
user3.inser_cpf('02222222222')
print(user3.nome, user3.idade, user3.cpf)

print("\nULITMO CADASTRO\n")