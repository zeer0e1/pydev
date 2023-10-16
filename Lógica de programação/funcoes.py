def soma(a, b):
    return a + b


resultado = soma(2, 3)
print(resultado)


# n1 = int(input('Digite o primeiro numero: '))
# n2 = int(input('Digiteo segundo numero: '))

# resultado2 = soma(n1, n2)
# print('O resultado é', resultado)


def saudacao(nome):
    print(f'Seja bem vindo {nome}')


# varios argumentos

def soma2(*args):
    resultado = sum(args)
    print(resultado)


lista_numeros = (1, 2, 3, 4, 5, 6, 7)
soma2(1, 2, 3, 4, 5, 6)
