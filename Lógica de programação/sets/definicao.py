# desordenada
# n permite duplicatas

#
lista = [1, 2, 1, 3, 4, 5, 5, 6, 6]

# eliminando as duplicatas da lista
conjunto = set(lista)
print(conjunto)

# exemplo  2
conjunto = {1, 2, "Python", (4, 5)}

# exemplos

try:
    conjunto.add([6, 7])

except TypeError as e:
    print(f'Erro: {e}')

# Criando conjunto
s_cahves = {1, 2, 3, 3, 4}

print(s_cahves)

# usando a função set
s_funcao = set([1, 2, 3, 3, 4, 4, 5])
print(s_funcao)

# comparando 2  métodos

print(s_cahves == s_funcao)
