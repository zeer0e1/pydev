N = int(input('Digite um número inteiro não negativo: '))


soma = 1
for numero in range(N, 0, -1):
    soma *= numero
    print(soma)
