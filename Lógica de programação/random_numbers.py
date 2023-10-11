# Números randomicos = números aleatórios

import random

# numeros inteiros
print(random.randrange(10, 20))


# Números quebrrados entre 0 e 1
print(random.random())

# Gerar um número itneiro aleatório entre dois valores (inclusive)
# Gera um número aleatório entre 10 e 20, inslusive
print(random.randint(10, 20))


# Escolher aletoriamente um elemento da lista
frutas = ["maça", 'banana', 'cereja']
print(random.choice(frutas))


# Embaralhar aleatoriamente uma lista
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros)  # Lista embaralhada


# Gerar um número de ponto flutuante aleatṕrio em um intervalo especifico:
# Gera um número de ponto flutuante entre 5.5 e 9.5
print(random.uniform(5.5, 9.5))
