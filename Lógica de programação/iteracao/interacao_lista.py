# Exemplo pratico
frutas = ['Maçã', 'Banana', 'Cereja', 'Damasco', 'Figo']

# Utilizando o for
for fruta in frutas:
    print(fruta)

# Enumerate - Essa função retonar tanto o indice como o valor ao iterar
# sobre uma lista, isso é util quando queremos saber a posicao de um item
# na lista
for i, fruta in enumerate(frutas):
    print(f'Fruta no indice {i} é {fruta}')
