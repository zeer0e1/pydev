saldo = 0

while True:
    print('Caixa Eletrõnico')
    print('1 - Verificar saldo')
    print('2 - Depositar dinheiro')
    print('3 - Sacar dinheiro')
    print('4 - Sair\n')
    escolha = input('Escolha uma das opções: ')
    if escolha == '1':
        print(f'Saldo {saldo}')
        continue
    elif escolha == '2':
        valor = float(input('Digite a quantia que você deseja depositar: '))
        saldo += valor
        print(f'Deposito de {valor} realizado')
        continue
    elif escolha == '3':
        valor = float(input('Digite a quantia que você deseja sacar: '))
        if saldo < valor:
            print('Valor indisponivel')
        else:
            saldo = saldo - valor
            print(f'Saque de {saldo} realizado ')
    elif escolha == '4':
        print('Saindo')
        break
    else:
        print('Opcao invalida')
        continue
