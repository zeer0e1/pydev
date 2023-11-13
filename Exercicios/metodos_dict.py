filmes = {
    'titulo': 'Inception',
    'diretor': 'Cristopher Nolan',
    'anor': 2010,
    'genero': 'Ficicao Cientifica'
}

# 1
print(filmes.keys())
print(filmes.values())
print(filmes.items())

# 2
copia_filmes = filmes.copy()
copia_filmes.clear()

# 3
filmes.setdefault('elenco', ['Leonado Dicarip', 'Ellen'])

# 4
atualizacoes = {
    'duracao': '148 minutos',
    'idioma': 'Ingles'
}
filmes.update(atualizacoes)

# 5

chaves = ['nome', 'idade', 'ocupacao']
new_dict = dict.fromkeys(chaves, 'Deconhecido')
