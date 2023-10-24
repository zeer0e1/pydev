numeros = [23, 11, 89, 34, 11, 56, 78, 90, 23, 45]
print('Antes de ordenar', numeros)
numeros.sort()
print('Depois de ordenar', numeros)
numeros.reverse()
print('Invertendo a ordem', numeros)
print(f'O número 11 aparece {numeros.count(11)} vezes na lista')
print(f'O primeiro indice do número 78 na lista é {numeros.index(78)}')

try:
    numeros.index(100)
except ValueError:
    print('O numero não existe na lista')
