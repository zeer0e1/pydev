usuario = {
    'nome': 'Jojo',
    'idade': 25,
    'email': 'lucas@gmail.com'

}

# passando como parametro


def exibir_perfil(perfil):

    for chave, valor in perfil.items():
        print(f'{chave}:{valor}')


exibir_perfil(usuario)

#  retornando dicionarios de funcoes


def criar_perfil(nome, idade, email):
    return {
        'nome': nome,
        'idade': idade,
        'email': email
    }


novo_usuario = criar_perfil('ana', 30, 'ana@gmail.com')
print(novo_usuario)
