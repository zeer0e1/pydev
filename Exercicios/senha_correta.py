senha_padrao = 123
contagem = 0
while True:
    senha = int(input('Digite a senha para sair: '))
    if senha == senha_padrao:
        print(f'Saindo após {contagem} tentativas')
        break
    else:
        contagem += 1
        print(f'Senha incorreta, tente novamente, vc já tentou {contagem} vezes')
        continue
