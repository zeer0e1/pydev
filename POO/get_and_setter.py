class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self._preco = None
        self.set_preco(preco)

    def get_preco(self):
        return self._preco

    def set_preco(self, valor):
        if valor >= 0:
            self._preco = valor
        else:
            print('Preco deve ser maior que zero')

    def aplicar_desconto(self, desconto_porcentual):
        novo_preco = self._preco * (1 - desconto_porcentual / 100)

        self.set_preco(novo_preco)


p1 = Produto('Camiseta', 50)
print(f'Preço atual de {p1.nome}:R$ {p1.get_preco()}')
p1.set_preco(60)

print(f'Novo preço de {p1.nome}:R$  {p1.get_preco()}')
p1.set_preco(-10)

p1.aplicar_desconto(10)
print(f'Novo preço de {p1.nome} após desconto:R$ {p1.get_preco()}')
