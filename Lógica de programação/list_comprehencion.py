# Exemplo básico de list comprehencion
quadrados = [x ** 2 for x in range(10)]
print(quadrados)

# Exemplos tradicional

quadrados = []

for x in range(10):
    quadrados.append(x ** 3)
print(quadrados)

# Exemplo 2 de list comprehencion
quadrados_pares = []
