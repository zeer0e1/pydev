# Adicionar itens em uma lista
frutas = ['maça', 123, 'banana']

# apeend () adiciona um item no final da lista
frutas.append('cereja')

# insert() adicionar um local específico
frutas.insert(0, 'abacate')

# pop() remove um elemento de um local especfico
frutas.pop(2)

# remove() remove o primeiro item da lista que tem o valor espeficicado
frutas.remove('banana')

# COncatenar listas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

unicao = lista1 + lista2
print(unicao)

# extendete() adiciona os elmentos de uma lista (ou qualquer iterevél) ao final da lista atual
lista3 = [1, 2, 3, 5]
lista4 = [444, 33, 44, 55]
lista3.extend(lista4)
print(lista3)

# repetindo listas um numero especifico de vezes
repeticao = ['a', 'b'] * 10
print(repeticao)


# verificando se um item está na lista
print('2' in lista1)
