alunos = {
    'Joao': {
        'matematica': 8.5,
        'portugues': 10,
        'geografia': 7,
        'fisica': 6.5
    },
    'Paulo': {
        'matematica': 10,
        'portugues': 10,
        'geografia': 5.8,
        'fisica': 8
    }
}

# acessando
notas_joao_matematica = alunos['Joao']['matematica']
print(notas_joao_matematica)


# modificando
alunos['Paulo']['fisica'] = 10
print(alunos['Paulo']['fisica'])

# adicionando
alunos['Paulo']['quimica'] = 8.8
