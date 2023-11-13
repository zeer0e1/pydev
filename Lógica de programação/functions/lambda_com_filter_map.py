lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando filter() e lambda

numeros_pares = list(filter(lambda x: x % 2 == 0, lista_numeros))
print(numeros_pares)

# Usando filter() e lambda em strings

nomes = ['Lucas', 'Ana', 'Bob', 'Charles', 'Afonso']

nomes_com_a = list(filter(lambda nome: nome[0] == 'A', nomes))

print(nomes_com_a)

# Utilizando map() e lambda

lista_numeros2 = [1, 2, 3, 4, 5]

numeros_quadrados = list(map(lambda x: x ** 2, lista_numeros2))
print(numeros_quadrados)

# Exemplo com string
palavras = ['Abacate', 'Porta', 'geladeira', 'carro']
comprimento_palavra = list(map(lambda palavra: len(palavra), palavras))
print(comprimento_palavra)
