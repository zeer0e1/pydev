import os

lista_compras = []


def adicionar_item_lista(lista: list):
    clear()
    print('Digite o item para ser adicionado na lista:')
    while True:
        item: str = input()
        if item == '0':
            break
        else:
            lista.append(item)
            continue


def remover_item_lista(lista: list):
    clear()
    for i, item in enumerate(lista):
        print(f'{i} Item {item} ')

    print('Digite o número do item que você deseja excluir: ')
    numero = int(input())
    lista.pop(numero)


def clear():
    os.system('cls')


while True:
    print('Escolha uma das opções')
    print('Adicionar item a lista: 1')
    print('Remover item da lista: 2')
    print('Exibir lista de compras: 3')
    print('Sair: 4')
    print()
    escolha = input()
    if escolha == '4':
        print('Saindo...')
        break
    elif escolha == '1':
        adicionar_item_lista(lista_compras)
        continue
    elif escolha == '2':
        remover_item_lista(lista_compras)
    elif escolha == '3':
        clear()
        for i, item in enumerate(lista_compras):
            print(f'{i} {item}')
        continue
    else:
        print('Opção inválida')
        continue
