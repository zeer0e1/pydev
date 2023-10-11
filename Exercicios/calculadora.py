while True:
    print('Escolha uma das operações: ')
    print('1 - Multiplicação\n2 - Divisão\n3 - Soma\n4 - Subtração\n5- Sair')
    escolha = int(input('Escolha uma opção: '))

    if escolha == 5:
        print('Saindo...')
        break

    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))

    if escolha == 5:
        if escolha == 1:
            print(f'A Multiplicação entre {n1} e {n2} é {n1 * n2}')
            continue
    elif escolha == 2:
        print(f'A Divisão entre {n1} e {n2} é {n1 / n2}')
        continue
    elif escolha == 3:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
        continue
    elif escolha == 4:
        print(f'A Subtração entre {n1} e {n2} é {n1 - n2}')
        continue
    else:
        print('Escolha inválida')
        continue
