print('Responda com sim ou não')

convite_VIP = input('Vc possui um convite VIP ? ')

if convite_VIP.lower() == 'sim':
    'Bem vindo a festa'
else:
    lista_convidados = input('Vc está na lista de convidados ? ')
    if lista_convidados.lower() == 'sim':
        print('Bem vindo a festa')
    else:
        membro_clube = input('Vc faz parte do clube? ')
        if membro_clube.lower() == 'sim':
            print('Bem vindo a festa')
        else:
            'Vc n pode entrar'