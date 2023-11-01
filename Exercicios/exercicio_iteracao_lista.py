nomes = ['Alice', 'Bruno', 'Clara', 'Daniel', 'Eduarda']
for nome in nomes:
    print(nome)
for i, nome in enumerate(nomes):
    print(f'índice {i} Nome: {nome}')

notas = [85, 90, 78, 92, 88]

for i, nota in enumerate(notas):
    print(f'Aluno: {nomes[i]} Nota: {nota}')
