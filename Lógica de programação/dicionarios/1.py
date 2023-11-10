livro = {
    "titulo": "1984",
    "autor": "Geroge Orwell",
    "ano": 1949
}

print(livro['autor'])

frutas = ['Maça', 'Banana', 'Cereja']
print(frutas[1])


coordenadas = (4.5, 6.9)
print(coordenadas[0])

contatos = {
    'Alice': '555-334',
    'Bob': '555-887'
}

print(contatos['Alice'])


# Criando dicionário

carro = {
    'marca': "Ford",
    "modelo": "Mustang",
    "ano": 1964
}


print(carro)

# dicionarios vazio

pessoa = {}

# Dicionario com multiplos itens

pessoa = {
    'nome': 'maria',
    'idade': 30,
    'profissao': 'Developer',
    'nacionalidade': 'Brasileira'
}

# Dicionario aninhados
familia = {
    "pai": {
        'nome': 'Roberto',
        'idade': 40
    },

    'mae': {
        'nome': 'Clara',
        'idade': 48
    },

    'filho': {
        'nome': 'Pedro',
        'idade': 22
    }

}

print(familia['pai']['nome'])
