lagura = 5
altura = 3

for i in range(altura):
    for j in range(lagura):
        print('*', end=" ")
    print()


altura2 = 5
for i in range(altura2):
    espacos = altura2 - i - 1
    asteriscos = 2 * i + 1
    print(' ' * espacos + '*' * asteriscos)
