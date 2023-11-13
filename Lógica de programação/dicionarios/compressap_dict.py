
# criando um dicionario com comprehencion

quadrado = {x: x ** 2 for x in range(1, 6)}

# maneirra normal
quadrados = {}

for x in range(1, 6):
    quadrado[x] = x ** 2

# exemplo 2

original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: chave for chave, valor in original.items()}

# filtrando itens

precos = {
    'laptop': 1000,
    'mouse': 25,
    'monitor': 200,
    'teclado': 30
}

caros = {produto: preco for produto, preco in precos.items() if preco > 50}
print(caros)
