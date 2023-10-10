# Input  é a função que permite o usuário inserir dados no programa

nome = input('Digite seu nome: ')
print(f'O seu nome é :{nome}')

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2) / 2

print('Media final: ', format(media, '.2f'))
