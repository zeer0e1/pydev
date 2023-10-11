soma = 0
while True:
    numero = int(input('Digite um numero ou 0 para sair: '))
    if numero != 0:
        soma = soma + numero
        continue
    else:
        print(f'Total: {soma}')

