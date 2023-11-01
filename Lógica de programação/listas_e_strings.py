# Conversão de strings para listas

# Exemplo pratico

# Usando list()
# ao utilizar a função list() em uma string cada caractere da string
# Será um elemento da lista
s = 'Olá'
lista_s = list(s)
print(lista_s)

# Usando o split() para dividir uma string em uma lista com base
# em delimitador especificado, se nenhum delimitador for passado para funcao
# Por padrão ela vai ser dividida por espaços em branco
frase = 'Python é divertido'
palavras = frase.split()
print(palavras)

data = '12/10/2023'
elementos_data = data.split('/')
print(elementos_data)

# Conversão de listas para string

# Usando o join conseguimos converter uma lista em uma string
# Ela une os elementos de uma lista em uma única string com base no
# delimitador específicado
frase_juntado = ' '.join((palavras))
print(frase_juntado)

lista_data = ['25', '12', '2023']
data_juntada = '/'.join(lista_data)
print(lista_data)
print(data_juntada)
