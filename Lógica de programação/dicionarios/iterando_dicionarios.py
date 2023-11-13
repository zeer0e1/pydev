# usando for

notas = {
    'matematica': 8.5,
    'portugues': 9.0
}

# iteracao sobre as chaves do dicionarios
print('Materias cursadas pelo aluno')

for materia in notas:
    print(materia)

print('\nmateria usando .keys()')

for materia in notas.keys():
    print(materia)

# iterando sobre as notas
print('\nnotas do aluno')
total = 0
for nota in notas.values():
    print(nota)
    total += nota

media = total / len(notas)

print('\nmedia das notas:', media)

# iterando sobre chaves e valores simutalneamte

print('\nrealatorio de ntoas:')

for materia, nota in notas.items():
    print(f'{materia}: {nota}')
