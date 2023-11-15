M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

for i in range(4):
    for j in range(4):
        print(f'{M[i][j]}', end=' ')
    print()

coluna_especifica = 0
soma_coluna = 0

for linha in range(4):
    soma_coluna += M[linha][coluna_especifica]

print(f'\nA soma dos valores {coluna_especifica} é: {soma_coluna}')

# somar os valores da terceira linha

linha_especifica = 2
soma_linha = 0

for coluna in range(4):
    soma_linha += M[linha][coluna]

print(f'\nA soma dos valores {linha_especifica} é: {soma_linha}')
