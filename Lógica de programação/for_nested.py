for linha in range(1, 4):
    for j in range(1, 4):
        print(linha, '*', j, linha * j)


# List comprehencio

quadrados_impares = [x**2 for x in range(10) if x % 2 != 0]
print(quadrados_impares)

# Em um for "normal" ficaria assim:

quadrado_x = []
for x in range(10):
    if x % 2 != 0:
        quadrado_x.append(x**2)
print(quadrado_x)


texto = 'hello world'
consoantes2 = []

# list comprehencion
consoantes = [char for char in texto if char.lower() not in 'aeiou']


# for tradicional
for char in texto:
    if char.lower() not in 'aeiou':
        consoantes2.append(char.lower())

print(consoantes)
print(consoantes2)
