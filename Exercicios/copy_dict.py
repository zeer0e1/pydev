aluno = {
    'matricula': "A12345",
    'nome': 'Joaão Silva',
    'curso': 'Engenharia da computacao',
    'semestre': 5,
    'cr': 8.6,
    'idade': 26
}

# 1
aluno['hobies'] = ['Leitura', 'Corrida', 'Xadrez']


# 2
aluno['semestre'] = 6
aluno['cr'] = 8.7

# 3
del aluno['idade']

# 4
copia_1 = aluno.copy()
copia_2 = dict(aluno)
