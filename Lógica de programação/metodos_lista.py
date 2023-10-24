numeros = [23, 1, 45, 6, 12]
frutas = ['banana', 'Maça', 'banana', 'Cereja', 'Maça', 'damasco']


# Ordenad a lista  sort()
# Para numeros ele ordena em ordem crescente e para strings ordena por ordem
# Alfabética
numeros.sort()
frutas.sort()
print(numeros)

# reverse é uma parametro da função sorted que faz que a ordenação seja inversa
# Para numeros a ordem fica descrecente
# Para strings fica alfabetica porém começa do z

numeros.sort(reverse=True)
print(numeros)

# reverse() faz a inversão da ordem
numeros.reverse()
print(numeros)

# count() conta o número de cocorrencia de um elemento passado por parametro
ocorrencias_banana = frutas.count('banana')
print(ocorrencias_banana)

# index() retorna o indice da primeira ocorrencia do elemento
indice_banana = frutas.index('banana')
print(indice_banana)
