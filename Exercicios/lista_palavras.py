palavras = input('Digite as palavras separadas por virgula: ')
lista = palavras.split(',')

for palavra in lista:
    if len(palavra) > 4:
        print(palavra)
