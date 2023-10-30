# Exemplo básico de list comprehencion
quadrados = [x ** 2 for x in range(10)]
print(quadrados)

# Exemplos tradicional

quadrados = []

for x in range(10):
    quadrados.append(x ** 3)
print(quadrados)

# Exemplo 2 de list comprehencion
quadrados_pares = [x ** 2 for x in range(10) if x % 2 == 0]

print(quadrados_pares)
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

conbinacoes = list((x, y) for x in a for y in b if x + y == 5)

# for
for x in a:
    for y in b:
        if x + 5 == 5:
            conbinacoes.append((x, y))
