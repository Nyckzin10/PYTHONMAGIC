from agregacao import *

carrinho = Carinhodecompras()


p1 = Produto("Camiseta", 100)
p2 = Produto("Bermuda", 75)
p3 = Produto("Sandalia", 50)


carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)


carrinho.lista_produto()
print(carrinho.soma())