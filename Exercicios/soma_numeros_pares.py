numero_escolha = int(input('Digite um número inteiro: '))
soma = 0
for numero in range(1, numero_escolha + 1):
    if numero % 2 == 0:
        soma += numero
print(f'A soma dos numeros pares de 1 até {numero_escolha} é: {soma}')
