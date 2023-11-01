palavra = 'Python'
list_p = list(palavra)
print(palavra)
print(list_p)
print('-' * 5)
frase = 'Aprendendo Python é divertido!'
frase_lista = frase.split()
print(frase)
print(frase_lista)
print('-' * 5)
print('Ajuntando a frase')
frase_juntada = ''.join(list_p)
print(frase_juntada)
print('-' * 5)
lista_frutas = ['Maça', 'Banana', 'Cereja']
frase_frutas = ', '.join(lista_frutas)
print(lista_frutas)
print(frase_frutas)
