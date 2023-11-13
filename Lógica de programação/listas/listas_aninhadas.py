# Vamos considerar que queremos representar uma matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessar o item 5

elemento = matriz[1][1]

print(elemento)


# Iterando sobre uma matriz

for linha in matriz:
    for coluna in linha:
        print(coluna, end=' ')

    print()

# Vamos calcular a transposta da matriz
# Transposta é quando trocamos as colunas pelas linhas
transposta = []


for i in range(len(matriz[0])):
    linha_temporary = []

    for j in range(len(matriz)):
        linha_temporary.append(matriz[j][i])

    transposta.append(linha_temporary)
print(transposta)
