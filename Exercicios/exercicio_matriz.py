matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print('\nMatriz')

for i in range(4):
    for j in range(4):
        print(f'{matriz[i][j]}', end=" ")

    print()

soma = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]

print(soma)
