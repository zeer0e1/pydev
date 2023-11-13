livro = {
    "titulo": "O pequeno principe",
    'autor': "antoine de satin",
    'ano': 1943,
    'editora': 'Reynal e hichock',
    'preco': 20.50
}


# keys(), values() e items()

print('\nkeys(), values() e items()')
print('Chaves do dicionario', list(livro.keys()))
print('Valores do dicionario', list(livro.values()))
print('Itens do dicionario', list(livro.items()))

# clear()
print('\nClear')

copia_Livro = livro.copy()
copia_Livro.clear()  # limpas todos os dados do diconario
print(copia_Livro)

# setdefault()
# retonar o valor da chave especificada no primeirp parametro
# se a chave n existir insert a chave
# coim o valor especificado ( ou padro se nenhum valor for fornecido)
isbn = livro.setdefault('ISBN', '1231-3434-523')

# update

atulizacoes = {
    'preco': 18.5,
    'formato': 'capadura'
}

livro.update(atulizacoes)
# atualizada o dicionrio com elementos deoutro dicionari ou
# de um iteraval com pares chave-valor


# fromkeys()
print('\n from keys()')

chaves = ['Titulo', 'Autor', 'Sinopse']
novo_livro = dict.fromkeys(chaves, 'desconhecido')
print(novo_livro)
