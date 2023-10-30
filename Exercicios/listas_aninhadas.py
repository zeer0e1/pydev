matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

valor_pesquisado = matriz[1][2]

print(valor_pesquisado)

soma = 0
for linha in matriz:
    for numero in linha:
        soma += numero
print(soma)

for linha in matriz:
    for numero in linha:
        print(numero, end="\t")
    print()
