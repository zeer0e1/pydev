def adicionar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


list_number = list(
    map(int, input('Digite dois numero separados por "," para realizar os '
        'cálculos: ').split(',')))
print(list_number)
choice = input('Escolha qual operação você deseja'
               'fazer com os números: 1 - [adicionar] 2 - [subtrair] '
               '3 - [multiplicar] 4 - Diividir: ')

match choice:
    case '1':
        print(adicionar(list_number[0], list_number[1]))
    case '2':
        print(subtrair(list_number[0], list_number[1]))
    case '3':
        print(multiplicar(list_number[0], list_number[1]))
    case '4':
        print(dividir(list_number[0], list_number[1]))
