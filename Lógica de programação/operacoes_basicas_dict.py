produto = {
    'id': 12345,
    'nome': 'Camisa Polo',
    "cor": 'Vermelha',
    'preco': 49.90,
    'estoque': 100
}

# adicionando itens
produto['marca'] = 'FashionBrandd'
produto['desconto'] = 10

# imprimindo o produto

print(produto)


# atualizando itens
produto['preco'] = 59.90
produto['desconto'] = 15


# removendo itens
del produto['desconto']  # remove o item 'desconto' do dicionario

cor_removida = produto.pop('cor')  # remove e retorna o elemento removido

item_removido = produto.popitem()  # remove o ultimo item do diconario


# copiando dicionarios

# meotod copy()
produto_copai1 = produto.copy()

# metodo dict
produto_copi2 = dict(produto)
